#!/usr/bin/env python3
"""
Построение канонического справочника регионов для research-wiki.

Задача: свести ~530 вариантов написания имён гео-сущностей из шести SQLite-баз
к единому справочнику с иерархией country -> federal_district -> region.

Подход (три прохода):
  1. Точное совпадение по явной таблице алиасов (исторические сущности,
     двусмысленные случаи, английские слоги ФНС).
  2. Нормализация: латинские омоглифы -> кириллица, пунктуация, регистр,
     сноски вида '2)', '4', хвосты 'без автономного округа'.
  3. Нечёткое сопоставление (difflib) с порогом; всё ниже порога — в отчёт
     «требует ручного решения».

Выход:
  data/regions_canonical.csv   — канонический справочник (уровни, иерархия)
  data/region_aliases.csv      — карта: сырое значение -> канонический код
  data/region_unmatched.txt    — не сопоставленное (на ревью)
"""
import os, re, sqlite3, csv, json, unicodedata, collections, difflib
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
os.chdir(REPO)

# ──────────────────────────────────────────────────────────────────────
# 1. КАНОНИЧЕСКИЙ СПРАВОЧНИК: 89 субъектов + РФ + 8 федеральных округов
#    code: латиница, lowercase — машинный ключ
#    okato: официальный код (где применим), parent — код родителя
# ──────────────────────────────────────────────────────────────────────

FD = {  # федеральные округа
    "cfd": "Центральный федеральный округ",
    "szfd": "Северо-Западный федеральный округ",
    "ufd": "Южный федеральный округ",
    "skfd": "Северо-Кавказский федеральный округ",
    "pfd": "Приволжский федеральный округ",
    "urfd": "Уральский федеральный округ",
    "sfd": "Сибирский федеральный округ",
    "dfd": "Дальневосточный федеральный округ",
}

# Агрегаты, публикуемые источниками наравне с округами:
#   ntd — свод новых территорий (ДОМ.РФ публикует отдельной строкой)
#   *_nao/_ao — варианты «регион ВКЛЮЧАЯ автономные округа» (агрегат, не база)
# Формат: код -> (название, уровень, родитель, признак агрегации, состав через ;)
AGGREGATES = {
    "ntd":             ("Новые территории (свод)", "aggregate", "ufd",
                        "sum_of_new_territories", "dnr;lnr;zaporozhye;kherson"),
    "arkhangelsk_nao": ("Архангельская область (с НАО)", "region", "szfd",
                        "with_ao_included", "arkhangelsk;nenets_ao"),
    "tyumen_ao":       ("Тюменская область (с ХМАО и ЯНАО)", "region", "urfd",
                        "with_ao_included", "tyumen;khanty;yamal"),
}

# Города (не субъекты) — выделены отдельным уровнем
CITIES = {"sochi": ("Сочи", "krasnodar")}

# code: (название, okato, parent_fd)
REGIONS = {
 # ── Центральный ФО ──
 "belgorod":      ("Белгородская область", "14", "cfd"),
 "bryansk":       ("Брянская область", "15", "cfd"),
 "vladimir":      ("Владимирская область", "17", "cfd"),
 "voronezh":      ("Воронежская область", "20", "cfd"),
 "ivanovo":       ("Ивановская область", "24", "cfd"),
 "kaluga":        ("Калужская область", "29", "cfd"),
 "kostroma":      ("Костромская область", "34", "cfd"),
 "kursk":         ("Курская область", "38", "cfd"),
 "lipetsk":       ("Липецкая область", "42", "cfd"),
 "moscow_obl":    ("Московская область", "46", "cfd"),
 "oryol":         ("Орловская область", "54", "cfd"),
 "ryazan":        ("Рязанская область", "61", "cfd"),
 "smolensk":      ("Смоленская область", "66", "cfd"),
 "tambov":        ("Тамбовская область", "68", "cfd"),
 "tver":          ("Тверская область", "28", "cfd"),
 "tula":          ("Тульская область", "70", "cfd"),
 "yaroslavl":     ("Ярославская область", "78", "cfd"),
 "moscow":        ("Москва", "45", "cfd"),
 # ── Северо-Западный ФО ──
 "karelia":       ("Республика Карелия", "86", "szfd"),
 "komi":          ("Республика Коми", "87", "szfd"),
 "arkhangelsk":   ("Архангельская область (без НАО)", "11", "szfd"),
 "nenets_ao":     ("Ненецкий автономный округ", "11", "szfd"),
 "vologda":       ("Вологодская область", "19", "szfd"),
 "kaliningrad":   ("Калининградская область", "27", "szfd"),
 "leningrad":     ("Ленинградская область", "41", "szfd"),
 "murmansk":      ("Мурманская область", "47", "szfd"),
 "novgorod":      ("Новгородская область", "49", "szfd"),
 "pskov":         ("Псковская область", "58", "szfd"),
 "spb":           ("Санкт-Петербург", "40", "szfd"),
 # ── Южный ФО ──
 "adygea":        ("Республика Адыгея", "79", "ufd"),
 "kalmykia":      ("Республика Калмыкия", "85", "ufd"),
 "crimea":        ("Республика Крым", "35", "ufd"),
 "krasnodar":     ("Краснодарский край", "03", "ufd"),
 "astrakhan":     ("Астраханская область", "12", "ufd"),
 "volgograd":     ("Волгоградская область", "18", "ufd"),
 "rostov":        ("Ростовская область", "60", "ufd"),
 "sevastopol":    ("Севастополь", "67", "ufd"),
 # ── Северо-Кавказский ФО ──
 "dagestan":      ("Республика Дагестан", "82", "skfd"),
 "ingushetia":    ("Республика Ингушетия", "26", "skfd"),
 "kabardino":     ("Кабардино-Балкарская Республика", "83", "skfd"),
 "karachaevo":    ("Карачаево-Черкесская Республика", "91", "skfd"),
 "north_ossetia": ("Республика Северная Осетия — Алания", "90", "skfd"),
 "chechnya":      ("Чеченская Республика", "96", "skfd"),
 "stavropol":     ("Ставропольский край", "07", "skfd"),
 # ── Приволжский ФО ──
 "bashkortostan": ("Республика Башкортостан", "80", "pfd"),
 "marij_el":      ("Республика Марий Эл", "88", "pfd"),
 "mordovia":      ("Республика Мордовия", "89", "pfd"),
 "tatarstan":     ("Республика Татарстан", "92", "pfd"),
 "udmurtia":      ("Удмуртская Республика", "94", "pfd"),
 "chuvashia":     ("Чувашская Республика", "97", "pfd"),
 "perm":          ("Пермский край", "57", "pfd"),
 "kirov":         ("Кировская область", "33", "pfd"),
 "nizhni":        ("Нижегородская область", "22", "pfd"),
 "orenburg":      ("Оренбургская область", "53", "pfd"),
 "penza":         ("Пензенская область", "56", "pfd"),
 "samara":        ("Самарская область", "36", "pfd"),
 "saratov":       ("Саратовская область", "63", "pfd"),
 "ulyanovsk":     ("Ульяновская область", "73", "pfd"),
 # ── Уральский ФО ──
 "kurgan":        ("Курганская область", "37", "urfd"),
 "sverdlovsk":    ("Свердловская область", "65", "urfd"),
 "tyumen":        ("Тюменская область (без ХМАО и ЯНАО)", "71", "urfd"),
 "khanty":        ("Ханты-Мансийский автономный округ — Югра", "71", "urfd"),
 "yamal":         ("Ямало-Ненецкий автономный округ", "71", "urfd"),
 "chelyabinsk":   ("Челябинская область", "75", "urfd"),
 # ── Сибирский ФО ──
 "altai_rep":     ("Республика Алтай", "84", "sfd"),
 "khakasia":      ("Республика Хакасия", "95", "sfd"),
 "tuva":          ("Республика Тыва", "93", "sfd"),
 "altai_terr":    ("Алтайский край", "01", "sfd"),
 "krasnoyarsk":   ("Красноярский край", "04", "sfd"),
 "irkutsk":       ("Иркутская область", "25", "sfd"),
 "kemerovo":      ("Кемеровская область — Кузбасс", "32", "sfd"),
 "novosibirsk":   ("Новосибирская область", "50", "sfd"),
 "omsk":          ("Омская область", "52", "sfd"),
 "tomsk":         ("Томская область", "69", "sfd"),
 # ── Дальневосточный ФО ──
 "buryatia":      ("Республика Бурятия", "81", "dfd"),
 "sakha":         ("Республика Саха (Якутия)", "98", "dfd"),
 "zabaikalsk":    ("Забайкальский край", "76", "dfd"),
 "kamchatka":     ("Камчатский край", "30", "dfd"),
 "primorsky":     ("Приморский край", "05", "dfd"),
 "khabarovsk":    ("Хабаровский край", "08", "dfd"),
 "amur":          ("Амурская область", "10", "dfd"),
 "magadan":       ("Магаданская область", "44", "dfd"),
 "sakhalin":      ("Сахалинская область", "64", "dfd"),
 "jewish_ao":     ("Еврейская автономная область", "99", "dfd"),
 "chukotka":      ("Чукотский автономный округ", "77", "dfd"),
 # ── новые территории (2022) ──
 "dnr":           ("Донецкая Народная Республика", "", "ufd"),
 "lnr":           ("Луганская Народная Республика", "", "ufd"),
 "zaporozhye":    ("Запорожская область", "", "ufd"),
 "kherson":       ("Херсонская область", "", "ufd"),
}

# ──────────────────────────────────────────────────────────────────────
# 2. ТОЧНЫЕ АЛИАСЫ: исторические сущности и двусмысленные случаи
#    Исторические АО влились в регионы в 2005–2008 (референдумы 2003–2007).
# ──────────────────────────────────────────────────────────────────────
EXACT = {
 # исторические автономные округа (упразднены 2005–2008)
 "агинский бурятский округ": "zabaikalsk",
 "агинский бурятский округ (забайкальский край)": "zabaikalsk",
 "коми-пермяцкий округ": "perm",
 "коми-пермяцкий округ, входящий в состав пермского края": "perm",
 "корякский округ": "kamchatka",
 "корякский округ, входящий в состав камчатского края": "kamchatka",
 "таймырский (долгано-ненецкий) автономный округ": "krasnoyarsk",
 "таймырский (долгано-ненецкий) автономный округ (красноярский край)": "krasnoyarsk",
 "эвенкийский автономный округ": "krasnoyarsk",
 "эвенкийский автономный округ (красноярский край)": "krasnoyarsk",
 "усть-ордынский бурятский округ": "irkutsk",
 # Архангельская область: варианты с/без НАО
 "архангельская область": "arkhangelsk",
 "архангельская область (без ао)": "arkhangelsk",
 "архангельская область (без автономного округа)": "arkhangelsk",
 "архангельская область (кроме ненецкого ао)": "arkhangelsk",
 "архангельская область (кроме ненецкого автономного округа)": "arkhangelsk",
 "архангельская область без авт. округа": "arkhangelsk",
 "архангельская область без авт. округа.": "arkhangelsk",
 "архангельская область без автономного округа": "arkhangelsk",
 "архангельская область без данных по ненецкому автономному округу": "arkhangelsk",
 "архангельская без нао": "arkhangelsk",
 "архангельская область (с автономным округом)": "arkhangelsk_nao",
 # Тюменская область: варианты с/без ХМАО и ЯНАО
 "тюменская область (без ао)": "tyumen",
 "тюменская область (без авт.округов)": "tyumen",
 "тюменская область (без автономных округов)": "tyumen",
 "тюменская область без авт. округов": "tyumen",
 "тюменская область без автономных округов": "tyumen",
 "тюменская область \\nбез автономных округов": "tyumen",
 "тюменская область(без ханты-мансийского -югры и ямало-ненецкого автономных округов)": "tyumen",
 "тюменская область (кроме ханты-мансийского автономного округа - югры и ямало-ненецкого автономного округа)": "tyumen",
 "тюменская область (кроме ханты-мансийского автономного округа-югры и ямало-ненецкого автономного округа)": "tyumen",
 "тюменская область без данных по ханты-мансийскому автономному округу - югре и ямало-ненецкому автономному округу": "tyumen",
 "тюменская область (с автономными округами)": "tyumen_ao",
 # Северная Осетия — варианты тире
 "республика северная осетия": "north_ossetia",
 # сдвоенные названия «Республика X (X)», «X - Y»
 "республика татарстан (татарстан)": "tatarstan",
 "чувашская республика - чувашия": "chuvashia",
 "чувашская республика-чувашия": "chuvashia",
 "республика адыгея (адыгея)": "adygea",
 "республика саха (якутия)": "sakha",
 "респуб калмыкия": "kalmykia",
 "город санкт-петербург город федерального значения": "spb",
 "город москва столица российской федерации город федерального значения": "moscow",
 "еврейская ао": "jewish_ao", "еврейская авт.область": "jewish_ao",
 "еврейская авт. область": "jewish_ao", "еврейская авт. округ": "jewish_ao",
 "чукотский ао": "chukotka", "чукотский авт.округ": "chukotka", "чукотский авт. округ": "chukotka",
 "ненецкий ао": "nenets_ao", "ямало-ненецкий ао": "yamal", "ямало-ненецкий авт. округ": "yamal",
 "ямало-ненецкий авт.округ": "yamal", "ямало-ненецкий аo": "yamal",
 "ханты-мансийский ао": "khanty", "ханты-мансийский ао - югра": "khanty",
 "ханты-мансийский ао-югра": "khanty", "ханты-мансийский авт. округ - югра": "khanty",
 "ханты-мансийский автономный округ - югра": "khanty",
 "ханты-мансийский автономный округ – югра": "khanty",
 "ханты-мансийский автономный округ — югра": "khanty",
 "ханты-мансийский автономный округ-югра": "khanty",
 # агрегаты уровня страны
 "всего": "ru", "итого": "ru", "итого по рф": "ru", "итого по российской федерации": "ru",
 # прочее
 "малороссийский фо": "ntd",  # свод новых территорий у ДОМ.РФ (проверено по xlsx: строка 380)
 # родительный падеж составных названий (единичные случаи из росстата)
 "приволжского федерального округа": "pfd",
 "северо-каваказского федерального округа": "skfd",  # опечатка в источнике
 "северо-кавказского федерального округа": "skfd",
 "сибирского федерального округа": "sfd",
 "уральского федерального округа": "urfd",
 "дальневосточного федерального округа": "dfd",
 "южного федерального округа": "ufd",
 "чукотского автономного округа": "chukotka",
 "ямало-ненецкого автономного округа": "yamal",
 "ханты-мансийского автономного округа - югра": "khanty",
 "тюменской области без ханты-мансийского и ямало-ненецкого автономных округов": "tyumen",
 "сочи": "sochi",
 "всего введено в действие жилых домов — смешанная — удельный вес в общем объеме ввода, процентов": "NON_REGION",
 "крым": "crimea", "байконур": "baikonur",
 "чукотский автономный": "chukotka",
 # составные «регион — входящий АО» (Росреестр)
 "архангельская область — ненецкий автономный округ": "arkhangelsk",
 "архангельская область без авт.округа": "arkhangelsk",
 "тюменская область — ханты-мансийский автономный округ – югра": "tyumen",
 "тюменская область — ямало-ненецкий автономный округ": "tyumen",
 # агрегаты/подписи в росреестре — склейка уровней заголовков при парсинге
 "всего введено в действие жилых домов — удельный вес в общем объеме ввода, процентов": "NON_REGION",
 "всего введено в действие жилых домов — из общего итога - жилищно- строительные кооперативы — удельный вес в общем объеме ввода, процентов": "NON_REGION",
 "всего введено в действие жилых домов — населением за счет собственных и привлеченных средств — удельный вес в общем объеме ввода, процентов": "NON_REGION",
 "всего введено в действие жилых домов — государственная — удельный вес в общем объеме ввода, процентов": "NON_REGION",
 "всего введено в действие жилых домов — муниципальная — удельный вес в общем объеме ввода, процентов": "NON_REGION",
 "всего введено в действие жилых домов — собственность субъектов российской федерации — удельный вес в общем объеме ввода, процентов": "NON_REGION",
 "всего введено в действие жилых домов — федеральная — удельный вес в общем объеме ввода, процентов": "NON_REGION",
 "всего введено в действие жилых домов — частная — удельный вес в общем объеме ввода, процентов": "NON_REGION",
 "всего введено в действие жилых домов — российская — удельный вес в общем объеме ввода, процентов": "NON_REGION",
 "системы здравоохранения": "NON_REGION",
 "газовые, ед": "NON_REGION",
 "котлов паровых на теплоэлектроцентралях, т в час": "NON_REGION",
 "приостановленные или законсервированные": "NON_REGION",
 "республика северная осетия - алания": "north_ossetia",
 "республика северная осетия — алания": "north_ossetia",
 "республика северная осетия-алания": "north_ossetia",
 "республика северная  осетия - алания": "north_ossetia",
 # Кемерово
 "кемеровская область": "kemerovo",
 "кемеровская область - кузбасс": "kemerovo",
 "кемеровская область-кузбасс": "kemerovo",
 # федеральные округа — все варианты
 "дальневосточный фо": "dfd", "дальневосточный федеральный округ": "dfd",
 "дальневосточный федеральный округ 2)": "dfd", "дальневосточный федеральный округ2)": "dfd",
 "дальневосточный федеральный округ3": "dfd", "дальневосточный федеральный округ": "dfd",
 "приволжский фо": "pfd", "приволжский федеральный округ": "pfd",
 "приволжский               федеральный округ": "pfd",
 "северо-западный фо": "szfd", "северо-западный федеральный округ": "szfd",
 "северо-кавказский фо": "skfd", "северо-кавказский федеральный округ": "skfd",
 "северо-кавказский федер. округ": "skfd",
 "северо-кавказский                 федеральный округ": "skfd",
 "сибирский фо": "sfd", "сибирский федеральный округ": "sfd",
 "сибирский федеральный округ 2)": "sfd", "сибирский федеральный округ2)": "sfd",
 "сибирский           федеральный округ3": "sfd",
 "уральский фо": "urfd", "уральский федеральный округ": "urfd",
 "уральский             федеральный округ": "urfd",
 "центральный фо": "cfd", "центральный федеральный округ": "cfd",
 "южный фо": "ufd", "южный федеральный округ": "ufd",
 "южный федеральный округ (по 2009 год)": "ufd", "южный федеральный округ (с 2010 года)": "ufd",
 "южный федеральный округ (с 29.07.2016)": "ufd", "южный федеральный округ1)": "ufd",
 "южный                   федеральный округ2": "ufd",
 # уровень страны
 "российская федерация": "ru", "россия": "ru",
 "российская федерация (без г. москва)": "RU_EXCL_MOSCOW",
 # ── английские слоги ФНС (Точно-ст) ──
 "moscow city": "moscow", "moscow reg.": "moscow_obl", "moscow region": "moscow_obl",
 "sankt-petersburg": "spb", "st. petersburg": "spb", "saint-petersburg": "spb", "adygeya": "adygea", "altai rep.": "altai_rep",
 "altai terr.": "altai_terr", "amur": "amur", "arkhangelsk": "arkhangelsk",
 "astrakhan": "astrakhan", "bashkortostan": "bashkortostan", "belgorod": "belgorod",
 "bryansk": "bryansk", "buryatia": "buryatia", "chechnya": "chechnya",
 "chelyabinsk": "chelyabinsk", "chukotka": "chukotka", "chuvashia": "chuvashia",
 "crimea": "crimea", "dagestan": "dagestan", "donetsk": "dnr",
 "ingushetia": "ingushetia", "irkutsk": "irkutsk", "ivanovo": "ivanovo",
 "jewish ao": "jewish_ao", "kabardino-balkaria": "kabardino",
 "kaliningrad": "kaliningrad", "kalmykia": "kalmykia", "kaluga": "kaluga",
 "kamchatka": "kamchatka", "karachaevo-chercessia": "karachaevo",
 "karelia": "karelia", "kemerovo": "kemerovo", "khabarovsk": "khabarovsk",
 "khakasia": "khakasia", "khanty-mansijsk": "khanty", "kherson": "kherson",
 "kirov": "kirov", "komi": "komi", "kostroma": "kostroma",
 "krasnodar": "krasnodar", "krasnoyarsk": "krasnoyarsk", "kurgan": "kurgan",
 "kursk": "kursk", "leningrad": "leningrad", "lipetzk": "lipetsk",
 "luhansk": "lnr", "magadan": "magadan", "marij el": "marij_el",
 "mordovia": "mordovia", "murmansk": "murmansk", "nenets ao": "nenets_ao",
 "nizhni novgorod": "nizhni", "north ossetia": "north_ossetia",
 "novgorod": "novgorod", "novosibirsk": "novosibirsk", "omsk": "omsk",
 "orenburg": "orenburg", "oryol": "oryol", "penza": "penza", "perm": "perm",
 "primorsky terr.": "primorsky", "pskov": "pskov", "rostov": "rostov",
 "ryazan": "ryazan", "sakhalin": "sakhalin", "samara": "samara",
 "saratov": "saratov", "sevastopol": "sevastopol", "smolensk": "smolensk",
 "stavropol": "stavropol", "sverdlovsk": "sverdlovsk", "tambov": "tambov",
 "tatarstan": "tatarstan", "tomsk": "tomsk", "tula": "tula", "tuva": "tuva",
 "tver": "tver", "tyumen": "tyumen", "udmurtia": "udmurtia",
 "ulyanovsk": "ulyanovsk", "vladimir": "vladimir", "volgograd": "volgograd",
 "vologda": "vologda", "voronezh": "voronezh", "yakutia": "sakha",
 "yamal-nenets ao": "yamal", "yaroslavl": "yaroslavl",
 "zabaikalsk terr.": "zabaikalsk", "zaporizhzhia": "zaporozhye",
 "baikonur": "BAIKONUR",  # арендуемый у Казахстана
}

# ──────────────────────────────────────────────────────────────────────
# 3. НОРМАЛИЗАЦИЯ
# ──────────────────────────────────────────────────────────────────────
# Латинские омоглифы, встречающиеся в кириллических названиях
HOMOGLYPHS = str.maketrans({
 'A':'А','B':'В','C':'С','E':'Е','H':'Н','K':'К','M':'М','O':'О','P':'Р',
 'T':'Т','X':'Х','a':'а','c':'с','e':'е','o':'о','p':'р','x':'х','y':'у',
})
# явные пары, которые омоглиф-таблица не ловит
LATIN_FIX = {
 'аpхангельская': 'архангельская', 'бpянская': 'брянская',
 'владимиpская': 'владимирская', 'киpовская': 'кировская',
 'костpомская': 'костромская', 'ленингpадская': 'ленинградская',
 'муpманская': 'мурманская', 'новгоpодская': 'новгородская',
 'оpловская': 'орловская', 'тверская': 'тверская', 'твеpская': 'тверская',
 'яpославская': 'ярославская', 'маpий': 'марий', 'моpдовия': 'мордовия',
 'федеpация': 'федерация', 'сpедний': 'средний',
}

def normalize(s: str) -> str:
    """Нормализация сырого названия к виду для сопоставления.

    Омоглиф-замена применяется ТОЛЬКО к строкам с кириллицей: иначе английские
    слоги ФНС ('moscow city') разрушаются (латинские o, c, e заменяются на
    кириллические двойники).
    """
    s = s.strip()
    s = s.replace('\u00a0', ' ')
    s = re.sub(r'\s+', ' ', s)                       # схлопнуть пробелы/переносы
    s = s.replace('–', '-').replace('—', '-')        # длинные тире -> дефис
    s = re.sub(r'(\d)\)?\s*$', '', s)                # сноски: '2)', '4', '1)'
    s = s.lower().strip(' .,;:')
    # служебные префиксы, засоряющие названия
    s = re.sub(r'^(город|г\.)\s*', '', s)
    s = re.sub(r'^(в том числе|в т\.ч\.?)[:\s]*', '', s)
    s = s.strip(' .,;:')
    # омоглифы — только если в строке есть кириллица и нет слов латиницей
    has_cyr = any('\u0400' <= ch <= '\u04ff' for ch in s)
    has_latin_word = bool(re.search(r'[a-z]{3,}', s))
    if has_cyr and not has_latin_word:
        s = s.translate(HOMOGLYPHS)
        for bad, good in LATIN_FIX.items():
            s = s.replace(bad, good)
    # единая форма для вариантов «автономный округ» / «АО» / «авт.округ»
    s = re.sub(r'\bавт\.\s*округ\b|\bавт\.округ\b|\bавтономный\s+округ\b|\bао\b|\bаo\b', 'ао', s)
    # скобочные уточнения: срезаем ТОЛЬКО дублирующие название региона
    # («(Татарстан)», «(Адыгея)»); значимые («с автономным округом»,
    # «без автономного округа», «кроме Ненецкого АО») СОХРАНЯЕМ — иначе
    # варианты «с АО» и «без АО» схлопнутся в один код.
    _dup = ('татарстан','адыгея','якутия','чувашия','крым','алтай','мордовия','хакасия','тыва','карелия','коми','марий')
    def _paren(m):
        inner = m.group(1).strip().lower()
        if any(d in inner for d in _dup):
            return ''                      # дубль названия — убираем
        if inner in ('архангельская область','тюменская область'):
            return ''                      # дубль родителя — убираем
        return f' ({inner})'               # значимое уточнение — сохраняем
    s = re.sub(r'\s*\(([^)]*)\)\s*$', _paren, s)
    s = re.sub(r'\s+', ' ', s).strip(' .,;:-')
    # родительный падеж: «Алтайского края» -> «алтайский край» (приведение к основе)
    s = _derivative_fix(s)
    return s.strip()

GENITIVE = [
 ('республики ','республика '),
 ('автономной области','автономная область'),
 ('автономного округа','автономный округ'),
]
def _derivative_fix(s):
    for bad, good in GENITIVE:
        if s.endswith(bad): return s[:-len(bad)] + good
    # федеральный округ: 'дальневосточного федерального округа' -> 'дальневосточный федеральный округ'
    m = re.match(r'^(.*?)(ого|его)\s+федерального\s+округа$', s)
    if m:
        return f"{m.group(1) + ('ый' if m.group(2) == 'ого' else 'ий')} федеральный округ"
    # 'забайкальского края' -> 'забайкальский край'
    m = re.match(r'^(.*?)(ого|его)\s+(края|округа|автономного округа)$', s)
    if m:
        adj = m.group(1) + ('ый' if m.group(2) == 'ого' else 'ий')
        noun = {'края':'край','округа':'округ','автономного округа':'автономный округ'}[m.group(3)]
        return f"{adj} {noun}"
    # 'вологодской области' -> 'вологодская область'; 'чеченской республики' -> 'чеченская республика'
    m = re.match(r'^(.*?)(ой|ей|ая|яя)\s+(области|республики|область|республика)$', s)
    if m:
        stem = m.group(1) + m.group(2)
        if m.group(2) in ('ой','ей'):
            adj = stem[:-2] + ('ая' if m.group(2) == 'ой' else 'яя')
        else:
            adj = stem
        noun = {'области':'область','республики':'республика'}.get(m.group(3), m.group(3))
        return f"{adj} {noun}"
    return s

# ──────────────────────────────────────────────────────────────────────
# 3b. НЕ-РЕГИОНАЛЬНЫЕ ЗНАЧЕНИЯ: подписи строк, попавшие в колонку «регион»
#     Это не гео-сущности, а мусор в данных. Помечаем типом, чтобы исключить
#     из справочника и не считать «ошибкой канонизации».
# ──────────────────────────────────────────────────────────────────────
NON_REGION_PATTERNS = [
 (r'^(продано|не продано|продажи не открыты)', 'row_label_sales'),
 (r'^(объем|объём|в стадии|введено|их общая|их средний|число|количество)', 'row_label_volume'),
 (r'^(уровень строительной готовности|уровень стройготовности|плановый срок|в том числе с)', 'row_label_readiness'),
 (r'^(строительство|работы строительные|производство электромонтажных|разборка|разработка строительных)', 'row_label_okved'),
 (r'^(затраты|материальные затраты|амортизация|все затраты|прочие затраты|единый социальный налог)', 'row_label_cost'),
 (r'^\d{4}\.0$|^\d{4}1?\)?$', 'year_artifact'),
 (r'^(i|ii|iii|iv) квартал$', 'quarter_artifact'),
 (r'^% от|^от \d|^до \d|^от 1 млн|^и более$', 'bucket_artifact'),
 (r'^(административные|коммерческие|промышленные|сельскохозяйственные|учебные|другие)$', 'building_type'),
 (r'^(однокомнатные|двухкомнатные|трехкомнатные|тpехкомнатные|четырехкомнатные|четыpехкомнатные)$', 'apartment_type'),
 (r'^(жилого назначения|нежилого назначения)$', 'object_purpose'),
 (r'в сельской местности|в городской местности', 'census_dimension'),
 (r'^(-+|—|–|\s*)$', 'empty_dash'),
 (r'(дорог|мостов|тоннелей|линий|станций|подстанций|хранилищ|сооружений|элеваторов|птицефабрик|предприятий|фабрик|газопровод|нефтепровод|метрополитен)', 'infra_object'),
 (r'(цемент|кирпич|стали|стальных|проката|пиломатериал|плит|линолеум|пленк|красок|лаков|удобрений|угля|нефти|газа|руды|сахара|мяса|сыра|масла|трикотаж|лекарственн|кондитерск|хлебобулочн|цельномолочн|резинотехническ|теплоизоляционн|керамическ|санитарных|железобетонн|нерудных|стеновых|минеральных)', 'material'),
 (r'(проведены работы|электрифицировано)', 'other'),
 (r'^всего введено в действие жилых домов\s*—', 'row_label_stacked'),
 (r'—\s*(всего|удельный вес|из общего итога)', 'row_label_stacked'),
 (r'^(жилищно-|населением за счет|государственная|муниципальная|частная|смешанная|российская|собственность субъектов)', 'row_label_stacked'),
 # общий признак подписи строки: единица измерения в хвосте
 (r',\s*(тыс\.|млн\.|млрд\.|м2|м3|км|га|ед\.|шт\.|кв\.\s*м|чел\.|%|кВт|кВ\.А|номеров|мест|голов)', 'row_label_unit'),
 (r'^(тыс\.|млн\.|млрд\.)\s', 'row_label_unit'),
]

def classify_non_region(name: str):
    n = normalize(name)
    if not n: return 'empty'
    for pat, kind in NON_REGION_PATTERNS:
        if re.search(pat, n, re.I): return kind
    return None

# ──────────────────────────────────────────────────────────────────────
# 4. СБОР СЫРЫХ ЗНАЧЕНИЙ
# ──────────────────────────────────────────────────────────────────────
DB_COLS = [
 ('data/rosstat_construction.db','domrf_indicators','region_name'),
 ('data/rosstat_construction.db','observations','region_name'),
 ('data/rosstat_construction.db','cbr_mortgage_monthly','region_name'),
 ('data/rosstat_construction.db','cbr_corporate_monthly','region_name'),
 ('data/rosstat_construction.db','cbr_escrow_monthly','region_name'),
 ('data/rosstat_construction.db','average_wage_monthly_regional','region_name'),
 ('data/rosstat_construction.db','real_wage_index_annual_regional','region_name'),
 ('data/rosstat_construction.db','building_completions_regional','region_name'),
 ('data/rosstat_construction.db','construction_employment','region_name'),
 ('data/rosstat_construction.db','construction_machinery','region_name'),
 ('data/rosstat_construction.db','housing_prices_quarterly','region_name'),
 ('data/rosstat_construction.db','housing_prices_regional','region_name'),
 ('data/rosstat_construction.db','housing_input_operational_monthly','region_name'),
 ('data/regions_panel.db','panel','region_name'),
 ('data/cbr_lending.db','mortgage_monthly','region_name'),
 ('data/cbr_lending.db','escrow_monthly','region_name'),
 ('data/cbr_lending.db','corporate_monthly','region_name'),
 ('data/rosreestr_deals.db','deals_by_region_quarter','region'),
 ('data/rosreestr_deals.db','rents_by_region_quarter','region'),
 ('data/rosreestr_deals.db','housing_input_annual','region'),
 ('data/rosreestr_deals.db','ikv_region_quarter','region'),
 ('data/rosreestr_deals.db','housing_backlog_ratio_annual','region'),
 ('data/rosreestr_deals.db','rosstat_buildings_yearbook','region'),
 ('data/rosreestr_deals.db','rosstat_housing_avg_price_q','region'),
 ('data/rosreestr_deals.db','domrf_price_index','region'),
 ('data/fns_tochno_sectors.db','firms_F_2021','region'),
]

raw = collections.Counter()
raw_src = collections.defaultdict(set)
for db, tbl, col in DB_COLS:
    if not os.path.exists(db): continue
    try:
        c = sqlite3.connect(db)
        for v, n in c.execute(f'SELECT "{col}", COUNT(*) FROM "{tbl}" GROUP BY 1'):
            if v is None: continue
            k = str(v)
            raw[k] += n
            raw_src[k].add(Path(db).stem)
        c.close()
    except Exception as e:
        print(f"  ! {db}/{tbl}: {e}")

print(f"Сырых уникальных значений: {len(raw)}")

# ──────────────────────────────────────────────────────────────────────
# 5. СОПОСТАВЛЕНИЕ
# ──────────────────────────────────────────────────────────────────────
def match(name: str):
    """-> (code, method) или (None, reason)"""
    n = normalize(name)
    if not n: return None, "empty"
    # 0. не-региональный мусор (подписи строк и т.п.)
    kind = classify_non_region(name)
    if kind: return None, f"non_region:{kind}"
    if n in EXACT: return EXACT[n], "exact"
    # ключи EXACT тоже нормализуем (в них есть точки, регистр, аббревиатуры)
    for k, v in EXACT.items():
        if normalize(k) == n: return v, "exact-norm"
    # прямое совпадение с каноническим названием
    for code, (canon, okato, fd) in REGIONS.items():
        if normalize(canon) == n: return code, "canonical"
    # по короткому имени региона (без скобочных уточнений)
    for code, (canon, okato, fd) in REGIONS.items():
        base = re.sub(r'\s*\(.*?\)\s*', '', normalize(canon))
        if base == n: return code, "base"
    # базовое имя с отбрасыванием 'область / край / республика' — только как
    # подстраховка для неполных написаний, с нечётким сравнением
    best, score = None, 0.0
    for code, (canon, okato, fd) in REGIONS.items():
        base = re.sub(r'\s*\(.*?\)\s*', '', normalize(canon))
        for cand in (normalize(canon), base):
            r = difflib.SequenceMatcher(None, n, cand).ratio()
            if r > score: best, score = code, r
    if score >= 0.90: return best, f"fuzzy:{score:.2f}"
    return None, f"unmatched:{score:.2f}"

alias_rows, unmatched = [], []
for name, cnt in raw.items():
    code, how = match(name)
    if code and not code.isupper():
        if code in FD:
            canon, lvl, agg = FD[code], "federal_district", "base"
        elif code == "ru":
            canon, lvl, agg = "Российская Федерация", "country", "base"
        elif code in AGGREGATES:
            canon, lvl, _, agg, members = AGGREGATES[code]
        elif code in CITIES:
            canon, lvl, agg = CITIES[code][0], "city", "base"
        else:
            canon, lvl, agg = REGIONS[code][0], "region", "base"
        alias_rows.append({
            "raw_name": name, "count": cnt, "region_code": code,
            "canonical_name": canon, "level": lvl, "aggregation": agg,
            "aggregate_of": members if code in AGGREGATES else "",
            "method": how, "sources": ",".join(sorted(raw_src[name])),
        })
    else:
        unmatched.append((name, cnt, code or how, ",".join(sorted(raw_src[name]))))

print(f"Сопоставлено: {len(alias_rows)} | не сопоставлено: {len(unmatched)}")

# ──────────────────────────────────────────────────────────────────────
# 6. ЗАПИСЬ
# ──────────────────────────────────────────────────────────────────────
with open(DATA/"region_aliases.csv","w",newline="",encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["raw_name","count","region_code","canonical_name","level","aggregation","aggregate_of","method","sources"])
    w.writeheader(); w.writerows(sorted(alias_rows, key=lambda r:-r["count"]))

canon_rows = [{"region_code":"ru","name":"Российская Федерация","level":"country",
               "okato":"","parent_code":"","aggregation":"base","aggregate_of":""}]
canon_rows += [{"region_code":c,"name":n,"level":"federal_district","okato":"",
                "parent_code":"ru","aggregation":"base","aggregate_of":""} for c,n in FD.items()]
canon_rows += [{"region_code":c,"name":n,"level":"region","okato":o,"parent_code":p,
                "aggregation":"base","aggregate_of":""} for c,(n,o,p) in REGIONS.items()]
# агрегаты («с АО», свод новых территорий) — отдельные записи с признаком агрегации
canon_rows += [{"region_code":c,"name":n,"level":lvl,"okato":"","parent_code":par,
                "aggregation":agg,"aggregate_of":members}
               for c,(n,lvl,par,agg,members) in AGGREGATES.items()]
# города
canon_rows += [{"region_code":c,"name":n,"level":"city","okato":"","parent_code":par,
                "aggregation":"base"} for c,(n,par) in CITIES.items()]
with open(DATA/"regions_canonical.csv","w",newline="",encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["region_code","name","level","okato","parent_code","aggregation","aggregate_of"])
    w.writeheader(); w.writerows(canon_rows)

with open(DATA/"region_unmatched.txt","w",encoding="utf-8") as f:
    for name, cnt, how, srcs in sorted(unmatched, key=lambda x:-x[1]):
        f.write(f"{cnt:>9}  {name!r}  [{how}] [{srcs}]\n")

print(f"\nКанонических записей: {len(canon_rows)} (1 страна + {len(FD)} ФО + {len(REGIONS)} регионов)")
print("Записано: data/regions_canonical.csv, data/region_aliases.csv, data/region_unmatched.txt")

#!/usr/bin/env python3
"""
Генератор кодов метрик.

Правило (согласовано с владельцем):
  * если в источнике есть готовый код — используем его
    (например panel.indicator_code = 'Y477030001');
  * иначе — короткий код из первых букв слов названия:
    каждое слово транслитерируется, берётся первая буква,
    результат склеивается.

Функции:
    translit(text)            — русское слово → латиница
    code_from_name(name)      — первые буквы слов
    make_code(name, given)    — итоговый код с учётом готового
    uniquify(code, used)      — разрешение коллизий суффиксом
"""
import re

# ── транслитерация (ГОСТ-подобная, практичная) ────────────────────
_TR = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
    'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
    'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
    'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
    'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya',
}
# слова, не несущие смысла в названии показателя
_STOP = {
    'в', 'на', 'и', 'с', 'по', 'из', 'для', 'от', 'до', 'к', 'о', 'об',
    'за', 'при', 'не', 'или', 'а', 'то', 'же', 'the', 'of', 'and', 'to',
    'общей', 'общий', 'всего', 'прочие', 'прочее',
}


def translit(text: str) -> str:
    """Русский/английский текст → латиница (нижний регистр)."""
    out = []
    for ch in text.lower():
        if ch in _TR:
            out.append(_TR[ch])
        elif ch.isalnum():
            out.append(ch)
        # пробелы и пунктуация отбрасываются
    return ''.join(out)


def _words(name: str):
    """Значимые слова названия (без стоп-слов и чисел)."""
    words = re.findall(r'[А-Яа-яЁёA-Za-z]+', name)
    return [w for w in words if w.lower() not in _STOP and len(w) > 1]


MIN_LEN = 3


def code_from_name(name: str, max_len: int = 16) -> str:
    """
    Код из первых букв слов: 'Площадь квартир в жилых зданиях' → 'pkzz'.

    Слишком короткие результаты дополняются вторыми буквами слов:
    'Ввод жилья' → 'vzh' (а не 'vzh'), 'Реализация' → 'real'.
    Однобуквенные коды хрупки: любой новый показатель с той же буквой
    вытеснит их в суффиксную нумерацию.
    """
    words = _words(name)
    initials = [translit(w)[0] for w in words if translit(w)]
    code = ''.join(initials)[:max_len]

    # добираем длину: добавляем вторые буквы слов, пока код короткий
    if len(code) < MIN_LEN:
        for w in words:
            t = translit(w)
            if len(t) > 1:
                code += t[1]
                if len(code) >= MIN_LEN:
                    break
    # всё ещё коротко — берём начало первого слова
    if len(code) < MIN_LEN and words:
        t = translit(words[0])
        for ch in t:
            if ch not in code:
                code += ch
                if len(code) >= MIN_LEN:
                    break
    if not code:
        code = translit(name)[:8] or 'metric'
    return code[:max_len]


def make_code(name: str, given: str = None, fallback_name: str = None) -> str:
    """
    Итоговый код: готовый из источника, если он есть; иначе из названия.

    fallback_name — подстраховка для случаев, где поле названия содержит
    число (артефакт парсинга листов Excel), а осмысленный текст лежит
    в соседней колонке.
    """
    n = (name or '').strip()
    if (not n or n.isdigit()) and fallback_name:
        n = str(fallback_name).strip()
    name = n
    if given and str(given).strip():
        g = str(given).strip()
        # буквенно-цифровые коды вида Y477030001 оставляем как есть
        if re.fullmatch(r'[A-Za-z0-9_\-\.]{2,32}', g):
            return g.lower()
        # если это длинное описание — не годится, строим из названия
    return code_from_name(name)


def uniquify(code: str, used: set, max_len: int = 32) -> str:
    """Разрешить коллизию: добавить числовой суффикс."""
    if code not in used:
        used.add(code)
        return code
    i = 2
    while f'{code}_{i}' in used:
        i += 1
    out = f'{code}_{i}'
    used.add(out)
    return out


if __name__ == '__main__':
    # демонстрация на реальных названиях
    samples = [
        ('Площадь квартир в жилых зданиях, находящихся в незавершённом строительстве', None),
        ('Количество зданий и сооружений, находящихся в незавершённом строительстве', None),
        ('Введено в действие общей площади жилых домов на 1000 человек', None),
        ('Структура работ, выполненных организациями собственными силами', None),
        ('Ввод в действие нежилых зданий по типам в Российской Федерации', None),
        ('Объём выданных ипотечных кредитов', None),
        ('Задолженность по ипотечным кредитам', None),
        ('Средневзвешенная ставка по ипотечным кредитам', None),
        ('Количество действующих договоров долевого участия', None),
        ('Стоимость строительства', 'Y477030001'),
        ('Ввод жилья', 'Y477030002'),
        ('Индикатор бизнес-климата', None),
    ]
    used = set()
    print(f"{'название':<62} {'код':<18}")
    print('-' * 82)
    for name, given in samples:
        c = uniquify(make_code(name, given), used)
        print(f"{name[:60]:<62} {c:<18}")

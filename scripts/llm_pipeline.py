#!/usr/bin/env python3
"""
LLM Pipeline для research-wiki: переключение моделей Ollama Cloud.

Использование:
    from llm_pipeline import LLMPipeline
    pipe = LLMPipeline()
    
    # Рутина (извлечение, перевод, форматирование)
    summary = pipe.run("Переведи аннотацию...", model="routine")
    
    # Анализ (сущности, гипотезы, концепции)
    analysis = pipe.run("Выдели ключевые экономические сущности...", model="analysis")
    
    # Конкретная модель
    result = pipe.run("...", model="deepseek-v4-pro:0813")

Модели:
    routine  → glm-5.2 (быстрая, дешёвая, текущая)
    analysis → deepseek-v4-pro:0813 (reasoning, академический стиль)
    vision   → nemotron-3-ultra (анализ, мультиязычный)
    fast     → deepseek-v4-flash:0731 (быстрый, для больших объёмов)

Все модели доступны через Ollama Cloud OpenAI-compatible API.
"""

import os
import json
import requests
from typing import Optional, Dict, Any

# Конфигурация
OLLAMA_API_KEY = os.environ.get(
    "OLLAMA_API_KEY",
    "c18db817e828495bbfe47ed179e3e4b6.ZvREBiCcWIGEKbiSOnkOs9yY"
)
OLLAMA_BASE_URL = "https://ollama.com/v1"

# Пресеты моделей
MODEL_PRESETS = {
    "routine": {
        "model": "glm-5.2",
        "description": "Быстрая модель для рутины: извлечение, перевод, форматирование",
        "temperature": 0.3,
        "max_tokens": 4096,
    },
    "analysis": {
        "model": "deepseek-v4-pro:0813",
        "description": "Reasoning для анализа сущностей, гипотез, концепций",
        "temperature": 0.5,
        "max_tokens": 8192,
    },
    "vision": {
        "model": "nemotron-3-ultra",
        "description": "Nous Research — анализ, мультиязычный, длинный контекст",
        "temperature": 0.4,
        "max_tokens": 8192,
    },
    "fast": {
        "model": "deepseek-v4-flash:0731",
        "description": "Быстрый DeepSeek для больших объёмов текста",
        "temperature": 0.3,
        "max_tokens": 4096,
    },
    "hypothesis": {
        "model": "deepseek-v4-pro:0813",
        "description": "Формирование исследовательских гипотез",
        "temperature": 0.7,
        "max_tokens": 8192,
    },
    "translation": {
        "model": "glm-5.2",
        "description": "Перевод EN→RU (быстрая, хороший русский)",
        "temperature": 0.2,
        "max_tokens": 8192,
    },
    "extraction": {
        "model": "deepseek-v4-flash:0731",
        "description": "Извлечение структурированных данных из текста",
        "temperature": 0.1,
        "max_tokens": 4096,
    },
}

# Системные промпты по типам задач
SYSTEM_PROMPTS = {
    "analysis": """Ты — исследователь-аналитик в области экономики жилья и макроэкономики.
Задача: проанализировать академический текст и выделить:
1. Ключевые экономические сущности и переменные
2. Методологию и подход
3. Связь с исследовательскими вопросами (эластичность предложения жилья, ДКП, демография)
4. Потенциальные гипотезы для проверки на российских данных

Отвечай на русском языке, академическим стилем, с цитированием конкретных значений.""",

    "hypothesis": """Ты — исследователь-аналитик. Сформулируй проверяемые гипотезы
на основе предоставленного текста. Для каждой гипотезы укажи:
- Формулировку
- Ожидаемый результат
- Какие данные нужны для проверки
- Связь с существующей литературой

Отвечай на русском языке.""",

    "extraction": """Ты — система извлечения структурированных данных.
Извлеки из текста:
- Авторы, год, издание
- Ключевые переменные и их定义tions
- Методология (модель, данные, период)
- Основные количественные результаты
- Ограничения

Формат: JSON. Отвечай на русском языке.""",

    "translation": """Переведи академический текст с английского на русский язык.
Сохраняй терминологию, формулы и ссылки. Академический стиль.""",

    "routine": """Ты — ассистент исследователя. Выполняй задачи точно и кратко.
Отвечай на русском языке.""",
}


class LLMPipeline:
    """Переключатель моделей Ollama Cloud для research-wiki пайплайна."""

    def __init__(self, api_key: str = None, base_url: str = None):
        self.api_key = api_key or OLLAMA_API_KEY
        self.base_url = base_url or OLLAMA_BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        })

    def run(
        self,
        prompt: str,
        model: str = "routine",
        system: str = None,
        temperature: float = None,
        max_tokens: int = None,
        context: str = None,
    ) -> Dict[str, Any]:
        """
        Выполнить запрос к LLM.

        Args:
            prompt: Текст запроса
            model: Пресет ("routine", "analysis", "hypothesis", ...)
                   или конкретное имя модели ("deepseek-v4-pro:0813")
            system: Системный промпт (по умолчанию берётся из пресета)
            temperature: Переопределение температуры
            max_tokens: Переопределение лимита токенов
            context: Дополнительный контекст (текст статьи, данные)

        Returns:
            dict с ключами: content, model, usage, preset
        """
        # Определить пресет или конкретную модель
        if model in MODEL_PRESETS:
            preset = MODEL_PRESETS[model]
            model_name = preset["model"]
            temp = temperature if temperature is not None else preset["temperature"]
            tokens = max_tokens or preset["max_tokens"]
            sys_prompt = system or SYSTEM_PROMPTS.get(model, SYSTEM_PROMPTS["routine"])
        else:
            # Конкретное имя модели
            model_name = model
            temp = temperature if temperature is not None else 0.3
            tokens = max_tokens or 4096
            sys_prompt = system or SYSTEM_PROMPTS.get("routine")

        # Собрать сообщения
        messages = [{"role": "system", "content": sys_prompt}]
        if context:
            messages.append({"role": "user", "content": f"Контекст:\n{context}\n\nЗапрос:\n{prompt}"})
        else:
            messages.append({"role": "user", "content": prompt})

        # API вызов
        try:
            resp = self.session.post(
                f"{self.base_url}/chat/completions",
                json={
                    "model": model_name,
                    "messages": messages,
                    "stream": False,
                    "temperature": temp,
                    "max_tokens": tokens,
                },
                timeout=120,
            )

            if resp.status_code == 200:
                data = resp.json()
                return {
                    "content": data["choices"][0]["message"]["content"],
                    "model": data.get("model", model_name),
                    "usage": data.get("usage", {}),
                    "preset": model,
                    "status": "ok",
                }
            else:
                error_msg = ""
                try:
                    error_msg = resp.json().get("error", {}).get("message", "")
                except Exception:
                    error_msg = resp.text[:200]
                return {
                    "content": "",
                    "model": model_name,
                    "error": f"HTTP {resp.status_code}: {error_msg}",
                    "status": "error",
                }

        except requests.exceptions.Timeout:
            return {
                "content": "",
                "model": model_name,
                "error": "Timeout (120s)",
                "status": "error",
            }
        except Exception as e:
            return {
                "content": "",
                "model": model_name,
                "error": str(e),
                "status": "error",
            }

    def analyze_paper(self, text: str, model: str = "analysis") -> Dict[str, Any]:
        """
        Анализ статьи: сущности, методология, гипотезы.

        Args:
            text: Текст статьи (или аннотация + ключевые разделы)
            model: Пресет модели (по умолчанию "analysis")

        Returns:
            dict с результатом анализа
        """
        prompt = """Проанализируй следующий академический текст и выдели:

1. **Ключевые сущности**: экономические переменные, индикаторы, каналы передачи
2. **Методология**: модель, данные, период, идентификация
3. **Количественные результаты**: конкретные значения, эластичности, отклики
4. **Гипотезы**: какие гипотезы можно проверить на российских данных?
5. **Связь с литературой**: как соотносится с Baum-Snow & Han (2024), Saiz (2010),
   Iacoviello (2005), Yang & Zha (2026)?

Текст для анализа:"""
        return self.run(prompt, model=model, context=text)

    def extract_metadata(self, text: str) -> Dict[str, Any]:
        """
        Извлечение структурированных метаданных из текста статьи.
        """
        return self.run(
            "Извлеки метаданные из текста статьи.",
            model="extraction",
            context=text,
        )

    def translate(self, text: str, model: str = "translation") -> Dict[str, Any]:
        """
        Перевод английского текста на русский.
        """
        return self.run(
            f"Переведи следующий текст на русский язык:\n\n{text}",
            model=model,
        )

    def list_models(self) -> list:
        """Список доступных моделей."""
        try:
            resp = self.session.get(f"{self.base_url}/models", timeout=30)
            if resp.status_code == 200:
                return [m["id"] for m in resp.json().get("data", [])]
        except Exception:
            pass
        return list(MODEL_PRESETS.keys())


# CLI для тестирования
if __name__ == "__main__":
    import sys

    pipe = LLMPipeline()

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        print("=== Тест пресетов ===\n")
        for preset_name in ["routine", "analysis", "fast"]:
            print(f"--- {preset_name} ({MODEL_PRESETS[preset_name]['model']}) ---")
            result = pipe.run(
                "Назови 3 ключевые переменные для анализа рынка жилья. Кратко.",
                model=preset_name,
            )
            if result["status"] == "ok":
                print(f"OK: {result['content'][:200]}")
                u = result.get("usage", {})
                print(f"Tokens: {u.get('total_tokens', '?')}")
            else:
                print(f"ERROR: {result.get('error', '?')}")
            print()

    elif len(sys.argv) > 1 and sys.argv[1] == "analyze":
        # Анализ статьи из файла
        if len(sys.argv) > 2:
            with open(sys.argv[2], "r") as f:
                text = f.read()
        else:
            text = sys.stdin.read()

        result = pipe.analyze_paper(text)
        if result["status"] == "ok":
            print(result["content"])
            u = result.get("usage", {})
            print(f"\n--- Tokens: {u.get('total_tokens', '?')} ---")
        else:
            print(f"ERROR: {result.get('error', '?')}")

    elif len(sys.argv) > 1 and sys.argv[1] == "models":
        print("Доступные пресеты:")
        for name, cfg in MODEL_PRESETS.items():
            print(f"  {name:15s} → {cfg['model']:30s} {cfg['description']}")
        print("\nДоступные модели Ollama Cloud:")
        models = pipe.list_models()
        for m in models:
            print(f"  {m}")

    else:
        print("Usage:")
        print("  python llm_pipeline.py test      — тест пресетов")
        print("  python llm_pipeline.py analyze FILE — анализ статьи")
        print("  python llm_pipeline.py models    — список моделей")
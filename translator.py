import json
import os

class Translator:
    def __init__(self, translations_dir="translations", dfl="en"):
        self.translations_dir = translations_dir
        self.dfl = dfl
        self.current_language = dfl
        self.translations = {}
        self.load_translations(self.dfl)

    def load_translations(self, language):
        """Загружает JSON-файл с переводами для указанного языка."""
        filepath = os.path.join(self.translations_dir, f"{language}.json")
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                self.translations = json.load(f)
            self.current_language = language
        except FileNotFoundError:
            print(f"Translation file not found: {filepath}")
            if language != self.dfl:
                self.load_translations(self.dfl)
            else:
                self.translations = {}
        except json.JSONDecodeError:
            print(f"Error decoding JSON file: {filepath}")
            self.translations = {}

    def translate(self, key):
        """Возвращает перевод для указанного ключа. Если ключ не найден, возвращает сам ключ."""
        return self.translations.get(key, key)

    def set_language(self, language):
        """Устанавливает текущий язык."""
        if language != self.current_language:
            self.load_translations(language)

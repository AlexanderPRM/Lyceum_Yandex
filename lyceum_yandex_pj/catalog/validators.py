from __future__ import annotations

import re

import django.core.exceptions
import django.utils.deconstruct


@django.utils.deconstruct.deconstructible
class ContainsOneOfWorldValidator:
    def __init__(self, *words: list[str]):
        self.words_for_pattern = "|".join(words)
        self.words = words
        self.regexp = re.compile(rf"\b({self.words_for_pattern})\b", re.I)

    def __call__(self, value: str):
        if not self.regexp.search(value):
            raise django.core.exceptions.ValidationError(
                "Обязательно использовать слова: " f'{"".join(self.words)}'
            )

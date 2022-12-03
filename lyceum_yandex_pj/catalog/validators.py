from __future__ import annotations

import re

import django.core.exceptions
import django.utils.deconstruct


@django.utils.deconstruct.deconstructible
class ContainsOneOfWorldValidator:
    def __init__(self, *words: list[str]):
        self._words_for_pattern = '|'.join(words)
        self._regexp = re.compile(
            fr'\b({self._words_for_pattern})\b', re.I
        )

    def __call__(self, value: str):
        if not self._regexp.search(value):
            raise django.core.exceptions.ValidationError(
                f'Обязательно использовать слова: {" ".join(self._words)}')

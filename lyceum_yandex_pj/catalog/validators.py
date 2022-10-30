from django.core.exceptions import ValidationError
import pymorphy2
from functools import wraps


def validate_text(*words):
    @wraps(validate_text)
    def sub_validator(value):
        morph = pymorphy2.MorphAnalyzer(lang='ru')
        value = value.lower()
        for word in words:
            parse_word = morph.parse(word)[1]
            if any([
                parse_word.word in value,
                parse_word.normal_form in value,
                parse_word.inflect({'nomn'}).word in value,
               parse_word.inflect({'gent'}).word in value,
               parse_word.inflect({'datv'}).word in value,
               parse_word.inflect({'loct'}).word in value,
               parse_word.inflect({'ablt'}).word in value,
               parse_word.inflect({'accs'}).word in value,
               parse_word.inflect({'acc2'}).word in value,
               parse_word.inflect({'gen2'}).word in value]):
                return value
        raise ValidationError(
                        f'В описании обязательно должно быть - '
                        f'{" & ".join(words)}')
    return sub_validator

# На будущее :)
# class ValidateText:
#     def __init__(self, *words):
#         self.words = words

#     def __call__(self, value):
#         morph = pymorphy2.MorphAnalyzer(lang='ru')
#         value = value.lower()
#         for word in self.words:
#             parse_word = morph.parse(word)[1]
#             if any([
#                 parse_word.word in value,
#                 parse_word.normal_form in value,
#                 parse_word.inflect({'nomn'}).word in value,
#                parse_word.inflect({'gent'}).word in value,
#                parse_word.inflect({'datv'}).word in value,
#                parse_word.inflect({'loct'}).word in value,
#                parse_word.inflect({'ablt'}).word in value,
#                parse_word.inflect({'accs'}).word in value,
#                parse_word.inflect({'acc2'}).word in value,
#                parse_word.inflect({'gen2'}).word in value]):
#                 return value
#         raise ValidationError(
#                         f'В описании обязательно должно быть - '
#                         f'{" & ".join(self.words)}')

from django.core.validators import BaseValidator, RegexValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class ErrorValidator(BaseValidator):
    message = 'Value "%(value)s" has length of %(show_value)d! It should be at least %(limit_value)d symbols long!'
    code = 'too_short'

    def compare(self, a, b):
        return a <= b

    def clean(self, x):
        return len(x)


@deconstructible
class Validator(BaseValidator):
    message = 'Нельзя вводить вот эти символы %(limit_value)s '
    code = 'too_short'

    def compare(self, a, b):
        for i in a:
            if i in b:
                return True
        return False







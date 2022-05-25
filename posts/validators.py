from django.core.exceptions import ValidationError

def validate_symbols(value):
    if ("@" in value) or ("#" in value):
        raise ValidationError("'@'와 '#'은 사용할 수 없습니다.", code='symbol-err')
import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^\d+]', '', phone_number.strip())
    
    if cleaned_number.startswith('+'):
        return cleaned_number
    elif cleaned_number.startswith('380'):
        return '+' + cleaned_number
    else:
        return '+38' + cleaned_number

phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

normalized_numbers = [normalize_phone(number) for number in phone_numbers]
print(normalized_numbers)
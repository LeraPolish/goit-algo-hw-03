"""
HOME_WORK_3
NUM_1
"""


from datetime import datetime

def get_days_from_today(date):
    try:
        requested_day = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        difference_days = current_date - requested_day
        return difference_days.days
    except ValueError:
        return "Неправильний формат вхідних даних"

print(get_days_from_today("2020-10-09"))


"""
HOME_WORK_3
NUM_2
"""


import random

def get_numbers_ticket(min, max, quantity):

    if min < 0 or max > 1000:
        return []
    else:
        numbers = set()
        while len(numbers) < quantity:
            numbers.add(random.randint(min, max))

        return sorted(numbers)
min = 1
max = 1000
quantity = 20
print(get_numbers_ticket(min, max, quantity))


"""
HOME_WORK_3
NUM_3
"""


import re

def normalize_phone(phone_number):
    sanitized_numbers = []
    for phone in phone_number:
        sanitized_number = re.sub(r'\D', '', phone)
        if not sanitized_number.startswith('+'):
            if sanitized_number.startswith('380'):
                sanitized_number = '+' + sanitized_number
            else:
                sanitized_number = '+38' + sanitized_number
        sanitized_numbers.append(sanitized_number)

    return sanitized_numbers

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

print(normalize_phone(raw_numbers))
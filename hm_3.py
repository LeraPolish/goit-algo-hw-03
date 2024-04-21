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

def get_numbers_ticket(min_value, max_value, quantity):
    if not (1 <= min_value <= max_value <= 1000) or quantity > (max_value - min_value + 1):
        return []
    else:
        numbers = set()
        while len(numbers) < quantity:
            numbers.add(random.randint(min_value, max_value))
        return sorted(numbers)

min_value = 10
max_value = 14
quantity = 6
print(get_numbers_ticket(min_value, max_value, quantity))


"""
HOME_WORK_3
NUM_3
"""


import re

def normalize_phone(phone_number):
    sanitized_number = re.sub(r'\D', '', phone_number)
    if not sanitized_number.startswith('+'):
        if sanitized_number.startswith('380'):
            sanitized_number = '+' + sanitized_number
        else:
            sanitized_number = '+38' + sanitized_number
    return sanitized_number

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

for number in raw_numbers:
    print(normalize_phone(number))
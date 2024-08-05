import random

min = 1
max = 100
quantity = 6

def get_numbers_ticket(min, max, quantity):
    if not (isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int)):
        return []
    if min >= max or quantity <= 0 or quantity > (max - min):
        return []
    
    try:
        result = random.sample(range(min, max), quantity)
        return sorted(result)
    except ValueError:
        return []

print (get_numbers_ticket(min, max, quantity))

# Приклади некоректних даних
print(get_numbers_ticket(1, 100, 200))  # quantity більше ніж різниця між min та max
print(get_numbers_ticket(100, 1, 6))    # min більше або рівне max
print(get_numbers_ticket(1, 100, -5))   # quantity менше або рівне нулю
print(get_numbers_ticket('1', 100, 6))  # min не є цілим числом
print(get_numbers_ticket(1, '100', 6))  # max не є цілим числом
print(get_numbers_ticket(1, 100, '6'))  # quantity не є цілим числом

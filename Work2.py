import random

min = 1
max = 100
quantity = 6

def get_numbers_ticket(min, max, quantity):
    result = random.sample(range(min, max), quantity)
    return result

print (get_numbers_ticket(min, max, quantity))
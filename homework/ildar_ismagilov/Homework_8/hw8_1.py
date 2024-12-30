import random

salary = int(input('Enter your salary: '))
bonus = random.choice([True, False])
if bonus:
    salary += random.randint(10, 5000)

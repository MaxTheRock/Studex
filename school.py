import random


def dice():
    number1 = random.randint(1, 6)
    number2 = random.randint(1, 6)
    number = number1 + number2
    return number


dice()

number = dice()
print(number)

import random

def roll(): #creating roll function for rolling the die
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll
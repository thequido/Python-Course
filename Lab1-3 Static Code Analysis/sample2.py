"""
This code contains and tests the add function
"""

def add(number1, number2):
    """Function docstring"""
    return number1 + number2

NUM1 = 4
NUM2 = 5
TOTAL = add(NUM1, NUM2)
print("The sum of {} and {} is {}".format(NUM1, NUM2, TOTAL))

# BASIC ARITHMETIC OPERATIONS


# ADDITION

def add(a, b):
    return a + b


# SUBTRACTION

def subtract(a, b):
    return a - b


# MULTIPLICATION 

def multiply(a, b):
    return a * b


# DIVISION

def divide(a, b):
    if b == 0:
        return float('inf')
    else:
        return a / b


# EXPONENTIATION

def power(a, b):
    return a ** b


# FLOOR DIVISION

def floor_division(a, b):
    if b == 0:
        return float('inf')
    else:
        return a // b


# MODULUS 

import math
def modulus(a, b):
     if b == 0:
        return math.nan
     else:
        return a % b
# GREATER THAN

def is_greater(a, b):
    if a > b:
        return True
    else:
        return False
    

# EQUAL

def is_equal(a, b):
    if a == b:
        return True
    else:
        return False
    

# LESSER THAN

def is_lesser(a, b):
    if a < b:
        return True
    else: 
        return False
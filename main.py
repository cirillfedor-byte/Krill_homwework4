def square_number(a):
    return a ** 2

def cube_number(number):
    return number ** 3

def average_digit(number):
    number = abs(number)
    digits = [int(digit) for digit in str(number)]
    return sum(digits) / len(digits)


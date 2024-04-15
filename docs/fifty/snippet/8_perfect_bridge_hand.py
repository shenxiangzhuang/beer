# --8<-- [start:solution1]
from math import factorial
from fractions import Fraction


def calc_prob():
    prob = 4
    for i in range(13):
        print(i, 13-i)
        numerator = (13 - i) * Fraction(factorial(39 - 3 * i), factorial(3) * factorial(36 - 3 * i))
        denominator = Fraction(factorial(52 - 4 * i), factorial(4) * factorial(48 - 4 * i))
        prob *= Fraction(numerator, denominator)
    return prob

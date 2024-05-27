# --8<-- [start:solution1]
from math import factorial
from fractions import Fraction


def calc():
    prob = Fraction(factorial(12) * factorial(39), factorial(51))
    print(f"prob = {prob} = {float(prob)}")
    return prob


calc()
# --8<-- [end:solution1]


# --8<-- [start:solution2]
def combination_number(n: int, m: int) -> Fraction:
    """
    组合数计算
    """
    return Fraction(factorial(n), factorial(m) * factorial(n - m))


def calc_prob():
    prob = 4
    for i in range(13):
        numerator = combination_number(13-i, 1) * combination_number(39 - 3 * i, 3) * factorial(3)
        denominator = combination_number(52 - 4 * i, 4) * factorial(4)
        prob *= Fraction(numerator, denominator)
    print(f"prob = {prob} = {float(prob)}")
    return prob


calc_prob()
# --8<-- [end:solution2]


if __name__ == '__main__':
    prob = calc_prob()
    print(prob, float(prob))

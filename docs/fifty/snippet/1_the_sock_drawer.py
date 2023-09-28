# --8<-- [start:find_numbers]
import math


def is_square(n: int) -> bool:
    for i in range(n // 2 + 1):
        if i * i == n:
            return True
    return False


def is_odd(n: int) -> bool:
    return n % 2 == 1


def find_numbers(r_limit: int = 20):
    for r in range(1, r_limit):
        under_sqrt = 1 - 8 * r * (1 - r)
        if is_square(under_sqrt) and is_odd(int(math.sqrt(under_sqrt))):
            n = int((1 + int(math.sqrt(under_sqrt))) / 2)
            print(f"R = {r}, N = {n}, B = N - R = {n-r}")


if __name__ == "__main__":
    find_numbers()
# --8<-- [end:find_numbers]

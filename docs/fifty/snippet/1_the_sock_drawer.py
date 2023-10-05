# --8<-- [start:solution1]
import math


def is_square(n: int) -> bool:
    for i in range(n // 2 + 1):
        if i * i == n:
            return True
    return False


def is_odd(n: int) -> bool:
    return n % 2 == 1


def find_numbers(r_limit: int = 50) -> None:
    for r in range(1, r_limit):
        under_sqrt = 1 - 8 * r * (1 - r)
        if is_square(under_sqrt) and is_odd(int(math.sqrt(under_sqrt))):
            n = int((1 + int(math.sqrt(under_sqrt))) / 2)
            print(f"R = {r}, N = {n}, B = N - R = {n - r}")


# --8<-- [end:solution1]


# --8<-- [start:solution2]
def is_close(f1: float, f2: float) -> bool:
    return abs(f1 - f2) < 1e-6


def simulation(r_limit: int = 50, n_limit: int = 50) -> None:
    for r in range(1, r_limit):
        for n in range(r + 1, n_limit):
            if is_close(1 / 2, (r / n) * ((r - 1) / (n - 1))):
                print(f"R = {r}, N = {n}, B = N - R = {n - r}")


# --8<-- [end:solution2]

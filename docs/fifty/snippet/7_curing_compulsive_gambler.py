# --8<-- [start:solution1]


def binomial_coefficient(n: int, k: int) -> int:
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1

    result: float = 1
    for i in range(1, k + 1):
        result *= (n - i + 1) / i

    return int(result)


def calc_expectation() -> float:
    e = 0.0
    for i in range(36 + 1):
        e_i = (
            (36 * (i - 1))
            * binomial_coefficient(36, i)
            * (37 / 38) ** (36 - i)
            * (1 / 38) ** i
        )
        e += e_i
    return e


def calc_expectation_with_bet() -> float:
    e = 0.0
    for i in range(36 + 1):
        if i == 0:
            e_i = (
                -56
                * binomial_coefficient(36, i)
                * (37 / 38) ** (36 - i)
                * (1 / 38) ** i
            )
        else:
            e_i = (
                (20 + 36 * (i - 1))
                * binomial_coefficient(36, i)
                * (37 / 38) ** (36 - i)
                * (1 / 38) ** i
            )
        e += e_i
    return e


print(f"Expectation: {calc_expectation()}\n")
print(f"Expectation with bet: {calc_expectation_with_bet()}")
# --8<-- [end:solution1]

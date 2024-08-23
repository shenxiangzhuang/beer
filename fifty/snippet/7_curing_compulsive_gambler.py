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


# --8<-- [start:solution2]
import random  # noqa


def one_round_roulette_earn() -> int:
    """
    We denote one round as 36 times roulette games
    """
    n_times = 36
    target_number = 13

    pay = 1 * n_times
    earn = 0
    for i in range(n_times):
        number = random.randint(1, 38)
        if number == target_number:
            earn += 1 + 35
    return earn - pay


def with_earn_bet(earn: int) -> int:
    if earn < 0:
        return earn - 20
    else:
        return earn + 20


def simulation(run_nums: int = 1000000, with_bet: bool = False) -> float:
    total_earn = 0
    for i in range(run_nums):
        earn = one_round_roulette_earn()
        if with_bet:
            earn = with_earn_bet(earn)
        total_earn += earn
    return total_earn / run_nums


print(f"Expectation: {simulation()}\n")
print(f"Expectation with bet: {simulation(with_bet=True)}")
# --8<-- [end:solution2]

# --8<-- [start:solution2]
import random


def is_a_win() -> bool:
    return random.uniform(0, 1) < 0.5


def run_once() -> bool:
    money_a, money_b = 1, 10
    # run until a or b has no money
    while money_a != 0 and money_b != 0:
        if is_a_win():
            money_a += 1
            money_b -= 1
        else:
            money_a -= 1
            money_b += 1

    if money_a == 11 and money_b == 0:
        return True
    else:
        return False


def simulation(run_nums: int = 1000000):
    a_win_count = 0
    for _ in range(run_nums):
        a_win_count += run_once()
    prob = a_win_count / run_nums
    print(f"A win prob in simulation: {prob}\n")
    print(f"1/11 = {1/11}\n")
    return prob


simulation()
# --8<-- [end:solution2]

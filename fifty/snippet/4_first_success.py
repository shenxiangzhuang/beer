# --8<-- [start:solution3]
import random


def roll() -> int:
    return random.randint(1, 6)


def roll_6_count() -> int:
    count = 1
    r = roll()
    while r != 6:
        r = roll()
        count += 1
    return count


def simulation(run_nums: int = 100000) -> None:
    roll_counts = [roll_6_count() for _ in range(run_nums)]
    print(f"Expectation times to got a 6: {sum(roll_counts) / run_nums}")


simulation()

# --8<-- [end:solution3]

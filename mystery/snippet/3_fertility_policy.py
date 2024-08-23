# --8<-- [start:solution]
import random

from enum import Enum


class Gender(int, Enum):
    MALE = 0
    FEMALE = 1


def birth_event() -> Gender:
    if random.randint(0, 1) == 0:
        return Gender.MALE
    else:
        return Gender.FEMALE


def family_event() -> int:
    female_count = 0
    while birth_event() != Gender.MALE:
        female_count += 1
    return female_count


def simulation(run_nums: int = 100000) -> None:
    male_count, female_count = 0, 0
    for _ in range(run_nums):
        female_count += family_event()
        male_count += 1
    print(f"Males: {male_count}, Females: {female_count}\n")
    print(f"Males/Female: {male_count / female_count}\n")


simulation()

# --8<-- [end:solution]

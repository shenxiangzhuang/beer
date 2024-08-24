# --8<-- [start:solution]
import math
import random


def random_point() -> float:
    return random.uniform(0, 1)


def run_once() -> int:
    pre_point = random_point()
    sequence_length = 1
    while True:
        next_point = random_point()
        if next_point <= pre_point:
            break
        else:
            sequence_length += 1
            pre_point = next_point
    return sequence_length


def simulation(run_nums: int = 1000000):
    total_length = 0
    for _ in range(run_nums):
        sequence_length = run_once()
        total_length += sequence_length
    avg_length = total_length / run_nums
    print(f"Average length: {avg_length}\n")
    print(f"e - 1 = {math.e-1}\n")
    return avg_length


simulation()
# --8<-- [end:solution]

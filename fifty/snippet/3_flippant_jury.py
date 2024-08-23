# --8<-- [start:solution2]
import random


def get_prob_prior() -> float:
    p = random.random()
    return p


def judge(right_prob: float) -> bool:
    r = random.random()
    if r < right_prob:
        return True
    else:
        return False


def decision(p: float) -> bool:
    decisions = [judge(p), judge(p), judge(0.5)]
    if sum(decisions) >= 2:
        return True
    else:
        return False


def simulation(run_nums: int = 1000000) -> None:
    p = get_prob_prior()
    right_decision_count = 0
    for _ in range(run_nums):
        if decision(p) is True:
            right_decision_count += 1
    right_decision_prob = right_decision_count / run_nums
    print(f"One jury got right decision probability: {p}\n")
    print(f"Three jury got right decision probability: {right_decision_prob}\n")


simulation()

# --8<-- [end:solution2]

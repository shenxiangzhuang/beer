# --8<-- [start:solution2]
import random

from typing import Literal, Tuple


def get_prior_prob() -> Tuple[float, float]:
    f = random.randint(6, 8) / 10
    c = random.randint(3, 5) / 10
    return f, c


def play(win_prob: float) -> bool:
    r = random.random()
    if r < win_prob:
        return True
    else:
        return False


def play_simulation(
    f: float, c: float, mode: Literal["FCF", "CFC"], run_num: int = 10000
) -> float:
    win_count = 0
    for _ in range(run_num):
        if mode == "FCF":
            s1, s2, s3 = play(f), play(c), play(f)
        else:
            s1, s2, s3 = play(c), play(f), play(c)
        if all([s1, s2]) or all([s2, s3]):
            win_count += 1
    win_prob = win_count / run_num
    return win_prob


def simulation(run_num: int = 10000) -> None:
    f, c = get_prior_prob()
    fcf_win_prob = play_simulation(f, c, mode="FCF", run_num=run_num)
    cfc_win_prob = play_simulation(f, c, mode="CFC", run_num=run_num)
    print(f"FCF: {fcf_win_prob}, CFC: {cfc_win_prob}")


simulation()

# --8<-- [end:solution2]


# --8<-- [start:solution2-extend]
def simulation_extend(run_num: int = 10000) -> None:
    count = 0
    for _ in range(100):
        f, c = get_prior_prob()
        fcf_win_prob = play_simulation(f, c, mode="FCF", run_num=run_num)
        cfc_win_prob = play_simulation(f, c, mode="CFC", run_num=run_num)
        if cfc_win_prob > fcf_win_prob:
            count += 1
    print(f"(CFC win prob > FCF win prob)'s prob: {count / 100}")


simulation_extend()

# --8<-- [end:solution2-extend]

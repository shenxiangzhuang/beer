# --8<-- [start:solution2]
import random

from typing import Dict, List, Tuple


def bet() -> Tuple[float, int]:
    """
    A bet action
    :return: the bet amount(stake) and the guess number
    """
    stake = 1.0
    guess = random.randint(1, 6)
    return stake, guess


def toss_three() -> List[int]:
    """
    A toss action
    :return: the three dice number
    """
    dices = [random.randint(1, 6) for _ in range(3)]
    return dices


def calc_loss(stake: float, guess: int, dices: List[int]) -> float:
    """
    Calculate the loss amount
    :param stake: the stake amount
    :param guess: the guess number
    :param dices: the dice numbers
    :return: the loss amount
    """
    guess_count = dices.count(guess)
    if guess_count == 0:
        return stake
    else:
        return -stake * guess_count


def play() -> float:
    """
    Play a game
    :return: the final amount
    """
    stake, guess = bet()
    dices = toss_three()
    loss = calc_loss(stake, guess, dices)
    return loss


def simulation(run_nums: int = 1000000, verbose: bool = True) -> float:
    amounts: Dict[str, List] = {"amounts": []}
    final_amount = 0.0
    for _ in range(run_nums):
        final_amount += play()
        amounts["amounts"].append(final_amount)

    expected_amount = final_amount / run_nums

    if verbose:
        print(f"Simulation expect loss amount: {expected_amount}\n")
        print(f"Theory expect loss amount: 17/216 = {17 / 216}\n")
    return expected_amount


simulation()

# --8<-- [end:solution2]

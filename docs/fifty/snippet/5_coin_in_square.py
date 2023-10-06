# --8<-- [start:solution2]
import random

from io import StringIO
from typing import Dict, List, Tuple

import matplotlib.colors as colors
import matplotlib.pyplot as plt


def toss() -> Tuple[float, float]:
    """
    A toss action
    :return: the position of the coin center
    """
    x, y = random.random(), random.random()
    return x, y


def is_win(x: float, y: float) -> bool:
    """
    Judge the position is in the win-area or not
    :param x: the x-axis position
    :param y: the y-axis position
    :return: win or not
    """
    if (3 / 8 < x < 5 / 8) and (3 / 8 < y < 5 / 8):
        return True
    return False


def simulation(
    run_nums: int = 1000000,
    verbose: bool = True,
) -> Dict[str, List]:
    positions: Dict[str, List] = {"xs": [], "ys": [], "win": []}
    win_count = 0
    for _ in range(run_nums):
        x, y = toss()
        positions["xs"].append(x)
        positions["ys"].append(y)
        win = is_win(x, y)
        if win:
            win_count += 1
            positions["win"].append(1)
        else:
            positions["win"].append(0)

    win_prob = win_count / run_nums
    if verbose:
        print(f"Win probability: {win_prob}\n")
        print(f"1/16 in float: {1 / 16}\n")
    return positions


simulation()

# --8<-- [end:solution2]


# --8<-- [start:solution2-plot]


def plot_simulation():
    fig, ax = plt.subplots()

    positions = simulation(10000, verbose=False)

    cmap = colors.ListedColormap(["pink", "lightgreen"])
    bounds = [0, 0.5, 1]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    # Create the plot
    ax.scatter(
        positions["xs"], positions["ys"], s=1, c=positions["win"], cmap=cmap, norm=norm
    )
    # Set labels and title
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Simulation")
    ax.grid(True)
    fig.tight_layout()

    buffer = StringIO()
    plt.savefig(buffer, format="svg")
    print(buffer.getvalue())


plot_simulation()


# --8<-- [end:solution2-plot]

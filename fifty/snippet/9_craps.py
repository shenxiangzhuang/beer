# --8<-- [start:solution2]
import random


def roll_dice():
    """Roll two dice and return the sum."""
    return random.randint(1, 6) + random.randint(1, 6)


def play_craps():
    """Play one game of Craps."""
    first_roll = roll_dice()

    if first_roll in [7, 11]:
        return 1  # Win
    elif first_roll in [2, 3, 12]:
        return 0  # Lose
    else:
        point = first_roll
        while True:
            next_roll = roll_dice()
            if next_roll == point:
                return 1  # Win
            elif next_roll == 7:
                return 0  # Lose


def simulation(num_games=1000000):
    """Run a simulation of Craps games."""
    wins = sum(play_craps() for _ in range(num_games))
    win_probability = wins / num_games
    print(f"Simulated probability of winning: {win_probability:.5f}\n")
    print(f"Theoretical probability of winning: 244/495 ≈ {244 / 495:.5f}\n")


# Run the simulation
simulation()
# --8<-- [end:solution2]


if __name__ == "__main__":
    simulation(num_games=1000000)

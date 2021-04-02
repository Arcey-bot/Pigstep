import random as r


class Dice:

    def __init__(self, sides=6, seed=0):
        self.sides = sides
        self.seed = seed
        r.seed(seed)

    # Roll a specified number of dice
    # Returns a list of dice
    def roll(self, dice=1):
        return [r.randint(1, self.sides) for i in range(dice)]

from Player import Player


# Each Pig game contains its own distinct players
class Pig:

    # Number of names passed in must be equal to number of players passed
    # Ex: 3 Players require 3 names [Bob, Tom, Jon]
    def __init__(self, player_count=2, names=None, goal=100):
        self.player_count = player_count
        self.names = names if names is not None else [f"Player {i + 1}" for i in range(player_count)]
        self.goal = goal
        self.players = [Player(name) for name in self.names]
        self.active = True

    # Determine what to do based on the player's roll
    # Roll is valid if it can continue round, >1
    # Roll is invalid if it ends round, ==1
    @staticmethod
    def valid_roll(player, roll):
        # The player rolled a above a 1
        if roll > 1:
            player.add_round_score(roll)
            print(f"{player.name}'s score: round - {player.round_score}, total - {player.total_score}\n")
            return True
        else:
            print(f"{player.name} lost this round's points!")
            player.reset_score()
            return False

    # Update the score of the player if they chose to hold/won
    @staticmethod
    def update_score(player):
        player.add_total_score(player.round_score)
        print(f"{player.name}'s total score - {player.total_score}\n")
        player.reset_score()

    # Show the game/instructions ("Welcome Screen")
    def show_welcome(self):
        pass

    # Get a player
    # Takes indice (int) or name (str)
    def get_player(self, val):
        # Did we get a name or indice
        if type(val) is int:
            return self.players[val]
        # Players are created in the same name order, so the arrays are parallel
        return self.players[self.names.index(val)]

    # Determine if win condition was met for active player
    def check_player_won(self, player):
        if player.total_score + player.round_score >= self.goal:
            player.add_total_score(player.round_score)
            print(f"{player.name} won with a score of {player.total_score}")
            return True
        return False


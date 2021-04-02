from Dice import Dice
from Pig import Pig


def main():
    game = Pig(goal=20)
    die = Dice()

    # First-time setup for game
    game.show_welcome()
    print(f"{game.players[0].name}'s turn! They have {game.players[0].total_score} points")
    play(game, die)


def play(game, dice, player_count=2):
    i = 0
    valid = True

    while game.active:
        active_player = game.get_player(i)

        # Turn continues
        if valid:
            inp = input("(R)oll or (H)old? ").lower()
            if inp == 'r':
                roll = dice.roll()[0]
                print(f"{active_player.name} rolled {roll}")
                valid = game.valid_roll(active_player, roll)

            elif inp == "h":
                game.update_score(active_player)
                i = 0 if i == player_count - 1 else i + 1
                print(f"{game.get_player(i).name}'s turn! They have {game.get_player(i).total_score} points")
        # Turn ends
        else:
            game.update_score(active_player)
            i = 0 if i == player_count - 1 else i + 1
            print(f"{game.get_player(i).name}'s turn! They have {game.get_player(i).total_score} points")
            valid = True
        game.active = False if game.check_player_won(active_player) else game.active


if __name__ == '__main__':
    main()

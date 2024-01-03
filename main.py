from classes.Game import Game


def main():
    players_count = int(input("Enter number of players: "))
    board_size = int(input("Enter the size of board: "))
    dice_count = 1

    game = Game(board_size, players_count)
    game.initialize_game()
    game.play_game()


main()

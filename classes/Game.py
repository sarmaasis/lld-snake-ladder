import time
from classes.Dice import Dice
from classes.Board import Board
from classes.Jumper import Jumper
from classes.Player import Player
import queue


class Game:

    def __init__(self, board_size, number_of_players):
        self.board_size = board_size
        self.number_of_players = number_of_players
        self.board = Board(self.board_size)
        self.players = queue.Queue()
        self.dice = Dice(1)
        self.ladders = []
        self.snake = []
        self.players_position = dict()

    def initialize_game(self):

        for player in range(0, self.number_of_players):
            player_name = input(f"Enter {player} player name: ")
            player_id = input(f"Enter {player} player id: ")
            self.players.put(Player(player_id, player_name))
            self.players_position[player_id] = 0

        snake_1 = Jumper(5, 2)
        snake_2 = Jumper(7, 3)
        ladder_1 = Jumper(4, 9)

        self.ladders.append(ladder_1)
        self.snake.append(snake_1)
        self.snake.append(snake_2)

    def play_game(self):
        while not self.players.empty():
            time.sleep(2)
            player = self.players.get()
            next_move = self.dice.roll_dice()
            print(f"Dice rolled: {next_move} for player {player.player_id}")
            player_id = player.player_id
            current_position = self.players_position[player_id]
            final_position = current_position + next_move
            if final_position >= self.board_size:
                print(f"Winner is: {player.player_name}")
                break

            for snake in self.snake:
                if snake.start_point == final_position:
                    print("Player bitten by snake.")
                    final_position = snake.end_point

            for ladder in self.ladders:
                if ladder.start_point == final_position:
                    print("Player raiser by ladder")
                    final_position = ladder.end_point

            print(f"New final position is {final_position}")
            self.players_position[player_id] = final_position
            self.players.put(player)

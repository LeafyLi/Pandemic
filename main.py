from pandemic import Pandemic
import sys

# TODO: Allow user to choose how many players/epidemic cards.
NUM_PLAYERS, NUM_EPIDEMIC_CARDS = 2, 4


def play_game():
    game = Pandemic(NUM_PLAYERS, NUM_EPIDEMIC_CARDS)

    game.characters = game.create_characters()
    game.set_up_board()
    winner = None
    while not winner:
        for i in range(game.num_players):
            print('Starting round {}'.format(game.round_number))
            winner = game.take_player_turn(i)
            if winner == 'Player':
                print('Game over!\n', game)
                print('Players have won!')
                sys.exit(0)
            if winner == 'Diseases':
                print('Game over!\n', game)
                print('Players have lost!')
                sys.exit(0)
        game.round_number += 1


if __name__ == "__main__":
    play_game()

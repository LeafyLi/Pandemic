from collections import namedtuple

TESTING_RANDOM_SEED = 1000

Disease = namedtuple('Disease', ['is_cured', 'is_eradicated'])


# TODO: Check upper/lower casing on disease types
class Pandemic:
    """Class for holding all the actions, given player classes"""

    def __init__(self, num_players: int, num_epidemics: int):
        self.num_players = num_players
        self.num_epidemics = num_epidemics
        self.outbreaks_so_far = 0
        self.infection_marker = 0
        self.infection_mapping = {0: 2, 1: 2, 2: 2, 3: 3, 4: 3, 5: 4, 6: 4}

        # TODO: Add default arguments for the disease type.
        self.disease_statuses = {'red': Disease(False, False), 'black': Disease(False, False),
                                 'yellow': Disease(False, False), 'blue': Disease(False, False)}
        self.characters = []
        self.infection_deck = []
        self.discarded_infection_pile = []
        self.player_deck = []
        self.board_cities = {}
        self.round_number = 1

        # TODO: Deal with cube counts
        self.disease_cubes_remaining = {'black': 24, 'blue': 24, 'yellow': 24, 'red': 24}

    def set_up_board(self):
        """Investigate combining these two functions (Might have mutability issues)"""
        self.infection_deck = self.create_infection_cards()
        self.player_deck = self.create_player_deck()

        self.board_cities = self.create_board_cities()
        self.run_initial_infections()

    def take_player_turn(self, player_number: int) -> str:
        cur_player = self.characters[player_number]
        num_actions = 4

        while num_actions > 0:
            next_action = input(
                "Please input the next action, options: 'Move', 'Build', 'Treat', 'Share', 'Discover', 'Special', 'Help', 'Rearrange Hand', 'Operations Expert Special Move', 'Dispatcher Special Move Another Pawn', 'Dispatcher Special Teleport', 'Pass'(to skip turn) ")
            cur_player.process_next_action(next_action)
            if self.is_player_win():
                return 'Player'
            num_actions -= 1

        cur_player.draw_cards(self)
        if self.is_player_loss():
            return 'Diseases'
        cur_player.check_hand_limit()
        self.infect_cities()
        if self.is_player_loss():
            return 'Diseases'


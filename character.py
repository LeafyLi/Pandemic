from typing import List

import pandemic


# TODO: Create an enum for character roles?
class Character:
    def __init__(self, role: str, player_number: int):
        self.role = role
        self.cur_location_name = 'Atlanta'  # All players start at Atlanta.
        self.hand = []  # List[card.PlayerCityCard]
        self.player_number = player_number

    def player_move(self, game: pandemic.Pandemic, move_type: str, next_city_name: str):
        if move_type == 'Drive':
            if not self.has_card(next_city_name, game):
                raise ValueError('You can not Drive to {} from {}'.format(next_city_name, self.location))
        elif move_type == 'Direct Flight':
            if not self.has_card(next_city_name, game):
                raise ValueError(
                    'Player can not make a direct flight to {} because they do not have the card in their hand'.format(
                        next_city_name))
            self.remove_card_by_name(next_city_name)
        elif move_type == 'Charter Flight':
            if not self.has_card(self.location, game):
                raise ValueError(
                    'Player can not make a charter flight because they do not have the {} card in their hand'.format(
                        self.location))
            self.remove_card_by_name(self.cur_location_name)
        elif move_type == 'Shuttle Flight':
            if not (game.board_cities[self.location].has_research_station and game.board_cities[
                next_city_name].has_research_station):
                raise ValueError(
                    'At most one of {} and {} have research stations'.format(next_city_name, self.location))
        else:
            raise ValueError('Invalid move type has been specified')
        self.cur_location_name = next_city_name

    def has_card(self, next_city_name: str, game: pandemic.Pandemic):
        return next_city_name in game.board_cities[self.location].neighbours

    def remove_card_by_name(self, target_city_name: str):
        for player_city_card in self.hand:
            if player_city_card.name == target_city_name:
                self.hand.remove(player_city_card)
                return
        raise ValueError('{} not found in the hand of player {}!'.format(target_city_name, self.player_number))


def create_character(remaining_roles: List[str], player_number: int) -> Character:
    """Creates a character from the remaining roles."""
    role_type = None
    while role_type not in remaining_roles:
        role_type = input("Choose character type, {} remain".format(', '.join(remaining_roles)))
        if role_type not in remaining_roles:
            raise ValueError('Invalid role chosen, please try again.')
    remaining_roles.remove(role_type)
    return Character(role_type, player_number)

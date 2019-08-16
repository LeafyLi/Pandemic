from typing import List


# TODO: Create an enum for character roles?
class Character:
    def __init__(self, role: str, player_number: int):
        self.role = role
        self.location = 'Atlanta'  # All players start at Atlanta.
        self.hand = []  # List[card.PlayerCityCard]
        self.player_number = player_number


def create_character(remaining_roles: List[str], player_number: int) -> Character:
    """Creates a character from the remaining roles."""
    role_type = None
    while role_type not in remaining_roles:
        role_type = input("Choose character type, {} remain".format(', '.join(remaining_roles)))
        if role_type not in remaining_roles:
            raise ValueError('Invalid role chosen, please try again.')
    remaining_roles.remove(role_type)
    return Character(role_type, player_number)

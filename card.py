from enum import Enum


class DiseaseColour(Enum):
    Black = 0
    Blue = 1
    Red = 2
    Yellow = 3
    NoneColour = 4


class Card:
    def __init__(self, name: str, colour_index: int = 4):
        self.name = name
        self.colour = DiseaseColour(colour_index)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.name


class InfectionCityCard(Card):
    def __init__(self, city_name, colour_index: int):
        super(InfectionCityCard, self).__init__(city_name, colour_index)


class PlayerCityCard(Card):
    def __init__(self, city_name: str, colour_index: int):
        super(PlayerCityCard, self).__init__(city_name, colour_index)


# TODO: Create enum for event cards.
class PlayerEventCard(Card):
    def __init__(self, effect: str, colour_index: int):
        super(PlayerCityCard, self).__init__(effect, colour_index)


class EpidemicCard(Card):
    def __init__(self):
        super(EpidemicCard, self).__init__('Epidemic')

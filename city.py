from typing import List


class City:
    def __init__(self, name: str, colour: str, neighbours: List[str]):
        self.name = name
        assert colour in ['black', 'blue', 'red', 'yellow']
        self.colour = colour
        self.neighbours = neighbours
        self.disease_cubes = {'black': 0, 'blue': 0, 'red': 0, 'yellow': 0}
        self.has_research_station = False

    def __repr__(self):
        return '{}: {}'.format(self.name, self.colour)

    def has_cubes_to_outbreak(self, colour):
        """We assume this is the source of an outbreak"""
        return self.disease_cubes[colour] > 3

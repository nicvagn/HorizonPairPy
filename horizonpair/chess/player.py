#  player is a part of HorizonPair
#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

from horizonpair.chess.colour import Colour


class Player:
    """A chess player in a tournament."""

    def __init__(self, name: str, cfc_id: str) -> None:
        self.name = name
        self.cfc_id = cfc_id

        # history of the matches this player has been in. Empty to start.
        self.match_history = list()

    def __str__(self) -> str:
        return f"""Player with name: { self.name }
CFC ID: { self.cfc_id }
match history: { self.match_history }"""

    def __repr__(self) -> str:
        return self.__str__()

    def __lt__(self, other) -> bool:
        return self.name < other.name

    def colour_preferance(self) -> Colour:
        pass

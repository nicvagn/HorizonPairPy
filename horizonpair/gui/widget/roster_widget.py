#  roster is a part of HorizonPair
#  HorizonPair is free software: you can redistribute it and/or modify it under the terms of the gnu general public license as published by the free software foundation, either version 3 of the license, or (at your option) any later version.
#
#  HorizonPair is distributed in the hope that it will be useful, but without any warranty; without even the implied warranty of merchantability or fitness for a particular purpose. see the gnu general public license for more details.
#
#  you should have received a copy of the gnu general public license along with HorizonPair. if not, see <https://www.gnu.org/licenses/>.

from time import sleep
from tkinter import *
from tkinter import ttk

from horizonpair.chess.colour import Colour
from horizonpair.chess.match import Match
from horizonpair.chess.player import Player
from horizonpair.chess.result import Result
from horizonpair.gui.widget import PlayerWidget
from horizonpair.tournament import Tournament
from horizonpair.tournament.roster import Roster
from horizonpair.tournament.round import Round


class RosterWidget(ttk.Frame):
    """A visual reperesentation of a chess roster."""

    def __init__(self, parent, roster: Roster) -> None:
        """arguments:
        parent[ttk.Widget] -- The parent widget in the hierarchy
        roster[Roster] -- The Roster this widget is displaying
        """
        super().__init__(parent, width=500, height=500, padding="3 3 12 12")

        self.grid(column=0, row=0, sticky=(N, W, E, S))

        i = 0
        # for player in roster.get_playes() display the player in a widget
        while i < len(roster.get_playes()):
            player = roster.get_playes()[i]
            # display the widget
            PlayerWidget(self, player).grid(row=i, column=0)
            i += 1

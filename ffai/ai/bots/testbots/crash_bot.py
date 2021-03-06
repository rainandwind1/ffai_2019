"""
==========================
Author: Niels Justesen
Year: 2018
==========================
This module contains an example bot that takes random actions.
"""
from ffai.core.model import Agent
from ffai.ai.registry import register_bot


class ChrashBot(Agent):

    def __init__(self, name, seed=None):
        super().__init__(name)
        
    def new_game(self, game, team):
        pass
        
    def act(self, game):
        v = 1 / 0
        return None

    def end_game(self, game):
        pass


# Register bot
register_bot('crash', ChrashBot)

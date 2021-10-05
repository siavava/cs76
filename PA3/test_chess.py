#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module is a driver function for the Chess Game.
"""
__author__ = "Amittai"
__copyright__ = "Copyright 2021"
__credits__ = ["Amittai"]
__email__ = "Amittai.J.Wekesa.24@dartmouth.edu"
__github__ = "@siavava"

# pip3 install python-chess


import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame


import sys


player1 = HumanPlayer()
player2 = RandomAI()

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()


#print(hash(str(game.board)))
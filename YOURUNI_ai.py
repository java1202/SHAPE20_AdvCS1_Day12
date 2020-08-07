#!/usr/bin/env python3
# -*- coding: utf-8 -*

#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
COMS W4701 Artificial Intelligence - Programming Homework 2

An AI player for Othello. This is the template file that you need to  
complete and submit. 

@author: YOUR NAME AND UNI 
"""

import random
import sys
import time
import math
# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move

def compute_utility(board, color):
  a = get_score(board)
  if color ==1:
   b = a[color]- a[1]
  else:
    b= a[color] -a[2]
  return b


############ MINIMAX ###############################

def minimax_min_node(board, color):
    oppColor = 1 if color == 2 else 2  
    possibleMoves = get_possible_moves(board, opp_color) 

    if not possibleMoves: 
      return compute_utility(board, color)

    bestMove = None
    bestScore = math.inf

    for x in possibleMoves: 
      new_board = play_move(board, opp_color, x[0], x[1])
      score = minimax_max_node(new_board, color)
      if score < bestScore: 
        bestMove = move
        bestScore = score

    return bestScore 
      





def minimax_max_node(board, color):
    possibleMoves = get_possible_moves(board, color)

    if not possibleMoves: 
      return compute_utility(board, color) 

    bestMove = None
    bestScore = -math.inf

    for y in possibleMoves: 
      newBoard = play_move(board, color, y[0], y[1])
      score = minimax_min_node(newBoard, oppColor)
      if score > bestScore: 
        bestMove = move
        bestScore = score

    return bestScore 




    
def select_move_minimax(board, color):
    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board. 
    """
    possibleMoves = get_possible_moves(board, color) 

    bestMove = None
    bestScore = -math.inf
    for z in possibleMoves: 
      newBoard = play_move(board, color, z[0], z[1])
      score = minimax_min_node(new_board, color)
      if score > bestScore: 
        bestMove = moves
        bestScore = score

    return best_move 
############ ALPHA-BETA PRUNING #####################

def alphabeta_min_node(board, color, alpha, level, limit):

  level += 1
  if level >= limit: 
    return heuristic_evaluation(board, color)
  opp_color = 1 if color == 2 else 2
  moves = get_possible_moves(board, color)
  if not moves:
    return compute_utility(board, color)
  beta = math.inf
  for x in moves:
    one, two = x
    testBoard = play_move(board, color, one, two)
    maxNode = alphabeta_max_node(testBoard, opp_color, beta, level, limit)
    if maxNode <= alpha:
      return maxNode
    beta = min(beta, maxNode)
  return beta 
def alphabeta_max_node(board, color, beta, level, limit):
  level += 1
  if level >= limit: 
    return heuristic_evaluation(board, color)
  opp_color = 1 if color == 2 else 2
  moves = get_possible_moves(board, color)
  if not moves:
    return compute_utility(board, color)
  alpha = -math.inf
  for x in moves:
    one,two = x
    testBoard = play_move(board, color, one,two)
    minNode = alphabeta_min_node(testBoard, opp_color, alpha, level, limit)
    if minNode >= beta:
      return minNode
      alpha = max(alpha, minNode)
  return alpha
def heuristic_evaluation(board, color):

  playerOne, playerTwo = get_score(board)
  if color == 1:
    if board[0][0] == 1 or board[0][7] == 1 or board[7][0] == 1 or board[7][7] == 1:
      playerOne += 5
  elif color == 2:
    if board[0][0] == 2 or board[0][7] == 2 or board[7][0] == 2 or board[7][7] == 2:
      playerTwo += 5
  if color == 1:
    return playerOne - playerTwo
  if color == 2:
    return playerTwo-playerOne


def select_move_alphabeta(board, color): 

  alpha = -math.inf
  beta = math.inf
  bestMove = (None, None)
  bestUtil = -math.inf
  opp_color = 1 if color == 2 else 2
  limit = 5
  level = 1
    
  #starting is max 
  for move in get_possible_moves(board, color):
    i,j = move
    new_board = play_move(board, color, i,j)
    utility = alphabeta_min_node(new_board, opp_color, alpha, level, limit)
    if utility > bestUtil:
      bestMove = move
      bestUtil = utility
       # select the move that gives the highest utility

  return bestMove

####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Minimax AI") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            # Select the move and send it to the manager 
            movei, movej = select_move_alphabeta(board, color)
            #movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
    run_ai()

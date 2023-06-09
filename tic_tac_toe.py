# -*- coding: utf-8 -*-
"""Tic tac toe

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/131iqm8LVbiRzmXh08XrsnHqLvMvDBXcQ
"""

def printBoard():
  zero = {'x' if xState[0] else ('0'if zState[0] else 0)
  one = {'x' if xState[1] else ('0'if zState[1] else 1)
  two = {'x' if xState[2] else ('0'if zState[2] else 2)
  three = {'x' if xState[3] else ('0'if zState[3] else 3)}
  four = {'x' if xState[4] else ('0'if zState[4] else 4)}
  five = {'x' if xState[5] else ('0'if zState[5] else 5)}
  six = {'x' if xState[6] else ('0'if zState[6] else 6)}
  seven = {'x' if xState[7] else ('0'if zState[7] else 7)}
  eight = {'x' if xState[8] else ('0'if zState[8] else 8)}

  print(f"{zero} | {one} | {two}")
  print(f"--|---|--")
  print(f"{three} | {four} | {five}")
  print(f"--|---|--")
  print(f"{six} | {seven} | {eight}")
  
if __name__ == "__main__":
  xState = [0,0,0,0,0,0,0,0,0]
  zState = [0,0,0,0,0,0,0,0,0]
  turn = 1
  print("Welcome to Tic Tac Toe")
  while(True):
    if (turn == 1):
      print("X's Chance")
      value = int(input("please enter a value"))
      xState[value] = 1
    else:
      print("X's Chance")
      value = int(input("ple)ase enter a value")
      zState[value] = 1

  printBoard()
# Program: dice.py
# Developer: Eduardo Pulido

# The game is played with five dice.
# The player is asked, "Roll dice?" at the beginning of each turn.
# If the player answers "n" or no, the game is over.
# If the player answers "y" or yes, the points are added to their score.
# The player scores 100 points for each one that is rolled.
# The player scores 50 points for each five that is rolled.
# The dice values and player score are displayed on the screen.
# If the player does not roll any ones or fives the game is over.
#
# Object: Dice
# Attribute: number selected
# Method: Random number between 1 and 6
#
# Object: Score
# Attribute: Value
# Method: calculation

from os import system, name
from pickle import FALSE
from re import I
import random

line0 = f'____________'
dice = [1,2,3,4,5,6]
dice_score = []
winner = 0

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
class dice:
    def __init__(self):
      self.dice_number = 0
    def roll_number(self):
      self.dice_number = random.randint(1, 6)
    def get_number(self):
      return self.dice_number
class score:
    def __init__(self):
      self.sum_number = 0
    def value_number(self, magic_number):
      if self.magic_number == 1:
        self.sum_number = 100
      if self.magic_number == 5:
        self.sum_number = 50
def main():
  
  dice1 = dice()
  dice.roll_number(self=0)
  #dice1 = dice.get_number()
  print(f'{dice1}')

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


if __name__ == "__main__":
    main()

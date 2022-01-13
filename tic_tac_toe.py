# Program: tic_tac_toe.py
# Developer: Eduardo Pulido

# The game is played on a grid that is three squares by three squares.
# Player one uses x's. Player two uses o's.
# Players take turns putting their marks in empty squares.
# The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
# If all nine squares are full and neither player has three in a row, the game ends in a draw.

from os import system, name
from pickle import FALSE
from re import I

line0 = f'____________'
cube_image = [1,2,3,4,5,6,7,8,9]
cube_control = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cube_player1 = []
cube_player2 = []
cube_rows = [6, 12, 15, 18, 24]
winner = 0

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def print_cube():  
    clear()
    i = 0
    line = '|'
    print(f'{line0}')
    while i < len(cube_image):
        line = line + str(cube_image[i]) + ' | '
        if i == 2 or i == 5 or i == 8:
            print(f'{line}')
            line = '|'
        i += 1
    print(f'{line0}')
    pass

def select_square(player, cube_value):  
    i = 0
    for i in cube_image:
        if i == cube_value:
            index = cube_image.index(i)
            if player == 1:
                cube_image[index] = 'X'
            else:
                cube_image[index] = 'O'
    pass

def main():
    print_cube()
    def input_cube(player):
        control = True
        not_found = False
        while control:
            try:
                print(f'Player {player}')
                cube_value = int(input('Input your square: '))  
                for i in cube_control:
                    select_square(player, cube_value)
                    print_cube()
                    if(i == cube_value):
                         if player == 1:
                            cube_player1.append(cube_value)
                         else:
                             cube_player2.append(cube_value)
                         cube_control.remove(cube_value)
                         not_found = False
                         break
                    else:
                          not_found = True
                if not_found:
                    print(f'Square not valid or already used')
                else:
                   control = False
            except ValueError:
                print('Sorry that is not a valid input')               
        pass

    def check_rows():
        i = 0
        sum_row1 = 0
        sum_row2 = 0
        for i in cube_player1:
            sum_row1 = sum_row1 + i              
        for i in cube_player2:
            sum_row2 = sum_row2 + i 
        i = 0
        for i in cube_rows:
            if i == sum_row1:
                winner = 1
                break
            if i == sum_row2:
                winner = 2
        return winner
    i = 1
    while i <= 3:
        player = 1
        input_cube(player)
        player = 2
        input_cube(player)
        i += 1
    winner = check_rows()
    if winner != 0:
        text = f'The winner is player {winner}'
        text = colored(0,255,0, text) 
        print(f'{text}')
    else:
        text = f'No winner'
        text = colored(255,0,0, text)
        print(f'{text}')

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


if __name__ == "__main__":
    main()

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
            break
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
                    if(i == cube_value):
                         if player == 1:
                            cube_player1.append(cube_value)
                         else:
                             cube_player2.append(cube_value)
                         cube_control.remove(cube_value)
                         select_square(player, cube_value)
                         print_cube()
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
        winner = 0
        if cube_image[0] == 'X' and cube_image[1] == 'X' and cube_image[2] == 'X':
            winner = 1
        if cube_image[3] == 'X' and cube_image[4] == 'X' and cube_image[5] == 'X':
            winner = 1
        if cube_image[6] == 'X' and cube_image[7] == 'X' and cube_image[8] == 'X':
            winner = 1
        if cube_image[0] == 'O' and cube_image[1] == 'O' and cube_image[2] == 'O':
            winner = 2
        if cube_image[3] == 'O' and cube_image[4] == 'O' and cube_image[5] == 'O':
            winner = 2
        if cube_image[6] == 'O' and cube_image[7] == 'O' and cube_image[8] == 'O':
            winner = 2
        if cube_image[0] == 'X' and cube_image[3] == 'X' and cube_image[6] == 'X':
            winner = 1
        if cube_image[1] == 'X' and cube_image[4] == 'X' and cube_image[7] == 'X':
            winner = 1
        if cube_image[2] == 'X' and cube_image[5] == 'X' and cube_image[8] == 'X':
            winner = 1
        if cube_image[0] == 'O' and cube_image[3] == 'O' and cube_image[6] == 'O':
            winner = 2
        if cube_image[1] == 'O' and cube_image[4] == 'O' and cube_image[7] == 'O':
            winner = 2
        if cube_image[2] == 'O' and cube_image[5] == 'O' and cube_image[8] == 'O':
            winner = 2
        if cube_image[0] == 'X' and cube_image[4] == 'X' and cube_image[8] == 'X':
            winner = 1
        if cube_image[2] == 'X' and cube_image[4] == 'X' and cube_image[6] == 'X':
            winner = 1
        if cube_image[0] == 'O' and cube_image[4] == 'O' and cube_image[8] == 'O':
            winner = 2
        if cube_image[2] == 'O' and cube_image[4] == 'O' and cube_image[6] == 'O':
            winner = 2
        return winner

    games = 0
    while games <= 9:
        if games <= 9:
            player = 1
            input_cube(player)
            games += 1
            player = 2
            winner = check_rows()
            if games != 9:
                input_cube(player)
                games += 1
            winner = check_rows()
            if winner != 0:
                text = f'The winner is player {winner}'
                text = colored(0,255,0, text) 
                print(f'{text}')
                break
            else:
                if games == 9:
                    text = f'No winner this is a tie!'
                    text = colored(255,0,0, text)
                    print(f'{text}')
                    break

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


if __name__ == "__main__":
    main()

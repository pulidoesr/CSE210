# Developer : Team 10
# Program : areas_shapes
import os
import time
from math import pi
from os import system, name

# Function to clear the screen
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
def menu():      
    clear()   
    print(f'\n Welcome to the area calculation \n')
    print(f'Please select one of the following options:')
    print(f'1. Rectangle ')
    print(f'2. Square ')
    print(f'3. Circle ')
    print(f'4. Quit')
def compute_area_square(square):
    area = square ** 2
    area = compute_area_rectangle(square, square)
    return area
def compute_area_rectangle(length, width):
    area = length * width
    return area
def compute_area_circle(radius):
    area = pi * (radius ** 2)
    return area
def compute_area(form, length, width):
    if form == 'Rectangle':
        area = compute_area_rectangle(length,width)
    if form == 'Square':
        area = compute_area_rectangle(length, length)
    if form == 'Circle':
        area = compute_area_circle(length)
    return area

option=0
while option !=4:
    menu()
    option = int(input('Please enter an option:'))
    if option <=0 or option >=5:
        print(f'\033[1;31;40mInvalid option, please enter a valid one \033[0;37;40m')
        time.sleep(3)
    if option == 1:
        length = float(input('What is the length of the rectangle in centimeters? '))
        width  = float(input('What is the width of the rectangle in centimeters? '))
        form = 'Rectangle'
        area = compute_area_rectangle(length, width)
        area = compute_area(form,length,width)
    if option == 2:
        square = float(input('What is the length of a side of the square in centimeters? '))
        form = 'Square'
        area = compute_area_square(square)
        area = compute_area(form,square,0)
    if option == 3:
        radius = float(input('What is the radius of the circle in centimeters? '))
        form = 'Circle'
        area = compute_area_circle(radius)
        area = compute_area(form,radius,0)
    if option >= 1 and option <= 3:
        line = f'The area of the {form} is: {str(area)} sq cm or {str(area / 10000)} sq m\n'
        print (line)
        time.sleep(5)
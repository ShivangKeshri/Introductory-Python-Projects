import random
import time
import turtle

WIDTH, HEIGHT = 500,500 # constants so they are in capital.

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("enter the number of racers(2 - 10) : ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("invalid input, please try again!")
            continue # continue brings me back to the while loop in the function.

        if 2 <= racers <= 10:
            return racers
        else:
            print("number not in range 2-10. Try Again! ")
            continue # continue brings me back to the start of the loop.
racers = get_number_of_racers()
print(racers)

def turtle_racing():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")
turtle_racing()

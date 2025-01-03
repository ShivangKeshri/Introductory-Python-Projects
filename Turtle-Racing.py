
import time
import turtle
import random

WIDTH, HEIGHT = 500,500 # constants so they are in capital.
COLORS = ['red','green', 'blue','orange','yellow','black','purple','pink','brown','cyan']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("enter the number of racers(2 - 10) : ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("invalid input, please try again!")
            continue # continue brings me  back to the while loop in the function.

        if 2 <= racers <= 10:
            return racers
        else:
            print("number not in range 2-10. Try Again! ")
            continue # continue brings me back to the start of the loop.

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y >= HEIGHT //2-10:
                return colors[turtles.index(turtle)]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH//(len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def turtle_setup():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")

racers = get_number_of_racers()
turtle_setup()

random.shuffle(COLORS)
colors = COLORS[:racers]
create_turtles(colors)
race(colors)

winner = race(colors)
print(f"the winner is {winner}")
time.sleep(5)

from random import randint

# Set the screen size
WIDTH = 400
HEIGHT = 400

# Initialize the lists to store dots and lines
dots = []
lines = []

# Variable to keep track of which dot should be clicked on next
next_dot = 0

# Create and position the dots in a loop
for dot in range(0, 10):
    actor = Actor("dot")  # Create a new Actor using the dot image
    actor.pos = (randint(20, WIDTH - 20), randint(20, HEIGHT - 20))
    dots.append(actor)

def draw():
    screen.fill("black")  # Fill the screen with a black background
    number = 1

    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))  # Display the dot's number label
        dot.draw()
        number += 1


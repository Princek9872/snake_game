import turtle
import time
import random

# Setup screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake initial setup
snake = []
for i in range(3):
    segment = turtle.Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(-20 * i, 0)
    snake.append(segment)

# Food setup
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Score setup
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# Snake movement
movement = {"Up": (0, 20), "Down": (0, -20), "Left": (-20, 0), "Right": (20, 0)}
direction = "Right"

# Function to change direction

def change_direction(new_direction):
    global direction
    if (direction, new_direction) not in [("Up", "Down"), ("Down", "Up"), ("Left", "Right"), ("Right", "Left")]:
        direction = new_direction

screen.listen()
screen.onkey(lambda: change_direction("Up"), "Up")
screen.onkey(lambda: change_direction("Down"), "Down")
screen.onkey(lambda: change_direction("Left"), "Left")
screen.onkey(lambda: change_direction("Right"), "Right")

# Function to move the snake

def move_snake():
    for i in range(len(snake) - 1, 0, -1):
        snake[i].goto(snake[i - 1].xcor(), snake[i - 1].ycor())
    snake[0].setx(snake[0].xcor() + movement[direction][0])
    snake[0].sety(snake[0].ycor() + movement[direction][1])

# Game loop
running = True
while running:
    screen.update()
    time.sleep(0.1)
    move_snake()

    # Check for collision with food
    if snake[0].distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        score += 10
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

        # Add new segment to snake
        new_segment = turtle.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        snake.append(new_segment)

    # Check for collision with walls
    if not (-290 < snake[0].xcor() < 290 and -290 < snake[0].ycor() < 290):
        running = False

    # Check for collision with self
    for segment in snake[1:]:
        if snake[0].distance(segment) < 10:
            running = False

# End game
score_display.goto(0, 0)
score_display.write("Game Over", align="center", font=("Arial", 36, "normal"))

screen.mainloop()
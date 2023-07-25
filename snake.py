
import turtle
import time
import random


score = 0
high_score = 0
delay = 0.1


# Set up the screen
wn = turtle.Screen()
wn.title('Welcome, Snaker')
wn.bgcolor("black")
wn.setup(width=800, height=800)
wn.tracer(0)  # Turns off screen updates

# Outline of the playing field
pencil = turtle.Turtle()
pencil.color('yellow')
pencil.penup()
pencil.goto(300,300)
pencil.pendown()
pencil.goto(-300,300)
pencil.goto(-300,-300)
pencil.goto(300,-300)
pencil.goto(300,300)
pencil.penup()
pencil.hideturtle()


# Snake
head = turtle.Turtle()
head.speed(0) 
head.shape('circle')
head.color('purple')
head.penup() # no trail
head.direction = 'stop'

# Snake Food
food = turtle.Turtle()
food.shape("turtle")
food.color('red')
food.penup()
food.goto(random.randint(-290, 290),random.randint(-290,290))

# Contains information about snake body
segments = []

# scores
pen = turtle.Turtle()
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write('Score: 0 High Score: 0', align = 'center', font = ('Times New Roman', 25, 'normal'))

# score function
def update_score():
    pen.clear()
    pen.write('Score: {} High Score: {}'.format(score, high_score), align='center', font = ('Times New Roman', 25, 'normal'))

# direction of the snake
def go_up():
    head.direction = 'up'

def go_down():
     head.direction = 'down'

def go_left():
    head.direction = 'left'

def go_right():
    head.direction = 'right'

# movement of the snake
def move():
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    if head.direction == 'up':
        head.sety(head.ycor() + 10)
    if head.direction == 'down':
        head.sety(head.ycor() - 10)
    if head.direction == 'left':
        head.setx(head.xcor() - 10)
    if head.direction == 'right':
        head.setx(head.xcor() + 10)

# collision
def collision():
    time.sleep(0.5)
    head.goto(0,0)
    head.direction = 'stop'

    for segment in segments:
        segment.hideturtle()
    segments.clear()

# bindings
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')

while True:
    # Updates the window repeatedly
    wn.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        collision()
        score = 0
        update_score()

    # Check if the snake eats the food
    if head.distance(food) < 20:
        food.goto(random.randint(-290,290),random.randint(-290,290))
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('circle')
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)
        
        # Increase the score
        score += 10
        if score > high_score:
            high_score = score
        update_score()

    # Move the snake in the game
    move()

    for segment in segments:
        if segment.distance(head) < 10:
            collision()
            score = 0
            update_score()
    time.sleep(delay)

wn.mainloop()
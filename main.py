# Game Description:
# The player controls a basket at the bottom of the screen using the left and right arrow keys.
# Objects (like apples or stars) fall from the top at random horizontal positions.
# The goal is to catch the falling objects with the basket.
# If the player catches an object, they get a point.
# If an object hits the ground, the player loses a life.
# The game ends when the player runs out of lives.
import turtle
import time

import player
import lives

import score

import falling_objects

# Create screen
screen = turtle.Screen()
screen.setup(width=550, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

# Show score
scoreboard = score.Score()

# Create player
player = player.Player()
screen.onkey(player.move_right, "d")
screen.onkey(player.move_left, "a")

# Show life
life = lives.Lives()

# Create fall objects
fall_object = falling_objects.Object()

# Check if game is over
game_is_on = True

frame_count = 0
spawn_interval = 100
leveled_up = False

while game_is_on:
    screen.update()
    time.sleep(0.02)

    frame_count += 1
    if frame_count % spawn_interval == 0:
        fall_object.add_object()

    fall_object.move_object()

    for i in fall_object.all_objects:
        if i.distance(player) < 40:
            i.hideturtle()
            fall_object.remove_object(i)
            scoreboard.level_up()
            leveled_up = False
        elif i.ycor() < -290:
            life.lose_life()
            i.hideturtle()
            fall_object.remove_object(i)

    if scoreboard.score % 5 == 0 and not leveled_up:
        fall_object.level_up()
        leveled_up = True

    if life.lives == 0:
        life.game_over()
        game_is_on = False

screen.exitonclick()

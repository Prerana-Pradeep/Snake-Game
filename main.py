from turtle import Screen
import time
from snake import Snake
import food
from scoreboard import ScoreBoard




screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake_body = []
for i in range(3):
    snake_obj = Snake(snake_body)


snake_food = food.Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake_obj.up, 'Up')
screen.onkey(snake_obj.down, 'Down')
screen.onkey(snake_obj.left, 'Left')
screen.onkey(snake_obj.right, 'Right')

game_is_on = True
position_list = []

while game_is_on:
    screen.update()
    snake_obj.move()
    time.sleep(.1)
    d = snake_obj.head.distance(snake_food)
    if d < 15:
        snake_food.refresh()
        score.ate_food()
        snake_obj.new_body()
    if snake_obj.crash_wall():
        # game_is_on = False
        score.reset_score()
        score.game_over()
        snake_obj.snake_reset()
        snake_obj.move()
    if snake_obj.crash_tail():
        # game_is_on = False
        score.reset_score()
        score.game_over()
        snake_obj.snake_reset()
        snake_obj.move()

screen.exitonclick()

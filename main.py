import turtle as t
import time
from snake import Snake
from food import Food
from score import Score

screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")
snake = Snake(screen)
food = Food()
score = Score()

end_game = False
while not end_game:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect Collision with Food
    if food.distance(snake.get_turtle()) < 15:
        print("Collision")
        food.refresh()
        score.score += 1
        snake.increase_size()
        score.score_refresh()

    # Detect Collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        print("End of game")
        score.end_game()
        end_game = True

    # Detect tail collisions:
    # Using Slicing to get all segments
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            print("Hit tail")
            score.hit_tail()
            end_game = True

screen.exitonclick()

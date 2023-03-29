from turtle import Screen
from Snake import  Snake
from food import  Food
import  time
from scoreborard import  Scorebord

screen =Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


new_snake =Snake()
food =Food()
scoreborard = Scorebord()
screen.listen()
screen.onkey(new_snake.Up,"Up")
screen.onkey(new_snake.Down,"Down")
screen.onkey(new_snake.Left,"Left")
screen.onkey(new_snake.Right,"Right")


is_game_on =True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    new_snake.Move()

    #detect collision with food.
    if new_snake.head.distance(food)< 15:
        food.Refresh()
        new_snake.Extend()
        scoreborard.Increase_Score()

    #Detect collision with wall
    if new_snake.head.xcor()>280 or new_snake.head.xcor()<-280 or new_snake.head.ycor()>280 or new_snake.head.ycor()<-280:
        scoreborard.Reset()
        new_snake.Reset()


    #Detect collision with tall.
    for segment in new_snake.segments[1:]:
        if new_snake.head.distance(segment) <10:
            scoreborard.Reset()
            new_snake.Reset()








screen.exitonclick()
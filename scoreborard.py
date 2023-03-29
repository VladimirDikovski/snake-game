from turtle import  Turtle

class Scorebord(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score=0
        self.hight_score =self.Read_High_Score()
        self.color("White")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.Update_ScoreBord()

    def Update_ScoreBord(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.hight_score}" , False, "center", font=("Arial", 20, "normal"))

    def Reset(self):
         if self.current_score>self.hight_score:
            self.hight_score=self.current_score
            self.Write_High_Score()
         self.current_score =0
         self.Update_ScoreBord()
    def Game_Over(self):
        self.goto(0,0)
        self.write("Game Over",False,"center",font=("Arial", 20, "normal"))

    def Increase_Score(self):
        self.current_score +=1
        self.Update_ScoreBord()


    def Read_High_Score(self):
        with open("data.txt") as file:
            self.hight_score =int(file.read())
        return  self.hight_score

    def Write_High_Score(self):
        with open("data.txt",mode="w") as file:
           file.write(f"{self.hight_score}")
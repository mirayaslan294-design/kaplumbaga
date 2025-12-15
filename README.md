### kaplumbaga
import turtle,random
from re import fullmatch

ekran=turtle.Screen()
ekran.bgcolor("red")
kalem=turtle.Turtle()                   ### 144 derece yıldıuz

kalem.pensize(5)
kalem.color("white")
                             ### burası sey iste pensize kalınlık  color renk range de sey kenar for i in range (10):
for i in range (5):
   kalem.speed(5)
   kalem.forward (144)
   kalem.right(144)

kalem.goto(100,-200)
kalem.begin_fill()
kalem.circle(50)
                                             ######kalem_begin_fill()
turtle.done()

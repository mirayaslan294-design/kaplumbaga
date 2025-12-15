import turtle
ekran=turtle.Screen()
ekran.bgcolor("pink")
def cokgen(kenar,renk,kalınlık):
     kalem=turtle.Turtle()
     kalem.pensize(kalnlık)
     kalem.color(renk)
for i in range (kenar):                  ### burası sey iste pensize kalınlık  color renk range de sey kenar
            for i in range (kenar):
                    kalem.speed(5)
                    kalem.forward (50)
                    kalem.right(360/kenar)
                kalem.right(360/kenar)
    turtle.done()




cokgen(5,"white","10")        ### kalem.pensize(10)  kalem.color("white") kalem.speed()
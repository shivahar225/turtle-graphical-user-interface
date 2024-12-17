import turtle as turtle_module
import random
tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.speed("fast")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245),(150, 75, 49),(233, 201, 135), (52,93,124),(172, 154, 48),(140,30, 19),(141, 184, 162),
(132, 166,205),(221,148,106),(32,42,61),(199,135,148),(166,58,48),(141,184,162),(39,105,157),(237,212,90),(150,59,66),(216,82,71),(168,29,33),(235,165,157),(51,111,90)]
tim.setheading(250)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for dot_count in range (1, number_of_dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

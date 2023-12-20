import turtle as turtle_module
import random
tim = turtle_module.Turtle()
turtle_module.colormode(255)

color_list = [(209, 165, 125), (249, 234, 237), (140, 48, 106), (164, 169, 38), (244, 80, 56), (3, 143, 55), (233, 109, 162), (215, 234, 232), (241, 65, 140), (1, 143, 184), (162, 55, 52), (57, 202, 224), (254, 230, 0), (20, 166, 126), (211, 232, 236), (244, 223, 50), (27, 197, 219), (162, 184, 171), (233, 165, 191), (191, 191, 193), (141, 213, 225), (243, 170, 153), (159, 212, 181), (106, 45, 98), (9, 115, 37), (131, 45, 38)]
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(315)
tim.setheading(0)

number_of_dot = 100

for dot_count in range(1, number_of_dot + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

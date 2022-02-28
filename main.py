# import colorgram
#
# colors = colorgram.extract('image.jpg', 26)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
import random

color_list = [(200, 175, 117), (224, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120)]

timmy = turtle.Turtle()
timmy.hideturtle()
timmy.width(30)
timmy.speed(0)
turtle.colormode(255)

def homepostion(x,y):
    timmy.pu()
    begin_x_position = x
    begin_y_position = y
    timmy.setpos(begin_x_position, begin_y_position)
    return begin_x_position, begin_y_position

def draw(pos):
    begin_xy_pos = pos

    for rows in range(10):
        for column in range(10):
            timmy.pd()
            timmy.fd(1)
            timmy.pu()
            timmy.fd(49)
            timmy.pencolor(random.choice(color_list))
        current_xy_pos = timmy.pos()
        next_y_pos = current_xy_pos[1]+50
        next_xy_pos = (begin_xy_pos[0], next_y_pos)
        timmy.setpos(next_xy_pos)


homepostion(-230, -220)
draw(timmy.pos())


screen = turtle.Screen()
screen.exitonclick()

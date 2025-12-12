from turtle import Turtle, Screen
import colorgram

colors = colorgram.extract('hirst_painting.png', 50)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    rgb_colors.append((r, g, b))

print(rgb_colors)


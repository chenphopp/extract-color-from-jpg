import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 30)
print(colors)

rgb_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)

print(rgb_color)

###
color_list = [(209, 165, 125), (249, 234, 237), (140, 48, 106), (164, 169, 38), (244, 80, 56), (3, 143, 55), (233, 109, 162), (215, 234, 232), (241, 65, 140), (1, 143, 184), (162, 55, 52), (57, 202, 224), (254, 230, 0), (20, 166, 126), (211, 232, 236), (244, 223, 50), (27, 197, 219), (162, 184, 171), (233, 165, 191), (191, 191, 193), (141, 213, 225), (243, 170, 153), (159, 212, 181), (106, 45, 98), (9, 115, 37), (131, 45, 38)]

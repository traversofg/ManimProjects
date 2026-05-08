from manim import *

######################################

#   No estoy encontrando una forma directa
# para recorrer una lista de todos los colores
# existentes en la libreria de Manim.

######################################


# Get all colors
all_colors = manim_colors._all_manim_colors
# print(all_colors)

# Print the list of colors
# for color_name, rgb_value in all_colors:
    # print(color_name, ":", rgb_value)

# print(all_colors)

pos = [
    [-2, 0, 0],
    [-1, 0, 0],
    ORIGIN,
    [1, 0, 0],
    [2, 0, 0]
]

class colors(Scene):
    def construct(self):
        dots = VGroup(
            *[Dot(color=str(manim_colors._all_manim_colors[_])).move_to(pos[_])
              for _ in range(5)]
        )
        self.add(dots)


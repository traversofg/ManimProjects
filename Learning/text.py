from manim import *

class LetterByLetter(Scene):
    def construct(self):
        
        n_plane = NumberPlane(
            background_line_style={
                'stroke_color'   : TEAL,
                'stroke_width'   : 2,
                'stroke_opacity' : .45 
            }
        )
        blue_dot = Dot(
            [2,1,0], 
            radius = 0.5, 
            color = BLUE_C
            )

        text = Text('This is a blue dot :D').next_to(blue_dot, 2*UP).scale(.75)
        arrow = Arrow(ORIGIN, DOWN, stroke_width=15).next_to(text.get_center(), DOWN)


        self.play(Create(n_plane))
        self.play(FadeIn(blue_dot))
        self.wait()
        self.play(Write(text))
        self.play(Create(arrow))
        self.wait(3)

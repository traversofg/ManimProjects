from manim import *
from probando import Custom

class Custom_GPT(Animation):
    def __init__(self, mobject, side_length=2, radius=0.5, **kwargs) -> None:
        super().__init__(mobject, **kwargs)
        self.side_length = side_length
        self.radius = radius

    def begin(self):
        dot = Dot(radius=self.radius, color=BLUE)
        self.mobject.add(dot)
        self.dot = dot
        super().begin()
    
    def clean_up_from_scene(self, scene: Scene) -> None:
        super().clean_up_from_scene(scene)
    
    def interpolate_mobject(self, alpha) -> None:
        alpha = self.rate_func(alpha)
        self.mobject.move_to(alpha*(3*RIGHT+2*UP))

class PruebaCustom_GPT(Scene):
    def construct(self):
        s = Square(color=RED, fill_opacity=0.5)
        self.add(s)
        self.add(NumberPlane(
            background_line_style={
                'stroke_color' : TEAL,
                'stroke_width' : 2,
                'stroke_opacity' : .45 
            }
        ))
        self.wait()
        self.play(Custom(s, run_time=4))
from typing import Callable
from manim import *
from manim.animation.animation import DEFAULT_ANIMATION_LAG_RATIO, DEFAULT_ANIMATION_RUN_TIME
from manim.mobject.mobject import Mobject
from manim.scene.scene import Scene
from manim.utils.rate_functions import smooth

class PrimeraPrueba(Scene):
    def construct(self):
        blue_circle = Circle(radius=1.5, color=BLUE_C, fill_opacity=.35)
        self.play(DrawBorderThenFill(blue_circle))
        self.wait()

        red_square = Square(side_length=3, color=RED_A, fill_opacity=.4)
        red_square.next_to(blue_circle, RIGHT)
        self.play(ReplacementTransform(blue_circle, red_square, run_time=1.5))
        # self.play(Create(red_square))
        self.play(Rotate(red_square, PI/2))
        self.wait()

class Ploteos(Scene):
    def construct(self):
        
        ax = Axes(
            x_range=(-4, 4), 
            y_range=(-1, 1),
            ).add_coordinates()
                
        # self.add(NumberPlane())
        self.play(Create(ax), run_time=2)

        self.play(
            Create(
                FunctionGraph(
                    lambda x: np.sin(PI*x),
                    [-3,3]
                ),
                run_time = 5
            )
        )
        self.wait()

class Posiciones(Scene):
    def construct(self):
        
        plane = NumberPlane()
        self.add(plane)

        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)

        green_dot.next_to(red_dot, UP + RIGHT)
        self.add(red_dot, green_dot)

        red_dot.move_to(UP + RIGHT)
        green_dot.move_to([(-4,3,0)])

        sq = Square(side_length=1, color=ORANGE)
        self.add(sq)

        sq.move_to([(2,1,0)])
        sq.rotate(PI/4)

class PruebasVarias(Scene):
    def construct(self):
        pass

class Animations(Scene):
    def construct(self):

        number_plane = NumberPlane(
            background_line_style={
                'stroke_color' : TEAL,
                'stroke_width' : 2,
                'stroke_opacity' : .45 
            }
        )
        self.add(number_plane)
        
        s = Square(color=RED, fill_opacity=.6)
        c = Circle(color=GREEN, fill_opacity=.6)
        
        self.play(FadeIn(s,c,lag_ratio=.5))
        self.wait()
        self.play(
            s.animate.shift(UL),
            c.animate.shift(DR)
        )
        self.play(
            s.animate.shift(DOWN),
            c.animate.shift(UP)
        )
        self.play(
            Rotate(s, PI, about_point=c.get_center()),
            # Rotate(c, PI, about_point=c.get_left()),
            run_time=2.5
        )
        self.wait()

class InAndOut(Animation): # No me agrega los Mob a la animación
    def __init__(self, mobject, side_length=2, radius=0.25, **kwargs):
        super().__init__(mobject, **kwargs)

        self.side_length = side_length
        self.radius = radius
    
    def begin(self):
        s = Square(side_length=self.side_length) # Este va a ser mi Mob a pasarle a la anim
        # c = Circle(color=PURPLE,radius=self.radius).set_opacity(0)        
        self.mobject.add(s)
        # self.circle = c
        super().begin()

    def clean_up_from_scene(self, scene: Scene) -> None:
        super().clean_up_from_scene(scene)
        # scene.remove(self.square)
        
    def interpolate_mobject(self, alpha):
        alpha = self.rate_func(alpha)

        self.mobject.animate.shift((3*RIGHT + 2*UP)*alpha)

class Custom(Animation):
    def __init__(self, mobject, side_length=2, radius=0.5, **kwargs) -> None:
        super().__init__(mobject, **kwargs)
        self.side_length = side_length
        self.radius = radius

    def begin(self):
        dot = Dot(radius=self.radius, color=BLUE)
        self.mobject.add(dot)
        # self.mobject.add(NumberPlane(
            # background_line_style={
                # 'stroke_color' : TEAL,
                # 'stroke_width' : 2,
                # 'stroke_opacity' : .45 
            # }
        # ))
        self.dot = dot
        super().begin()
    
    def clean_up_from_scene(self, scene: Scene) -> None:
        super().clean_up_from_scene(scene)
    
    def interpolate_mobject(self, alpha) -> None:
        alpha = self.rate_func(alpha)
        self.mobject.move_to(alpha*(3*RIGHT+2*UP))
        # self.dot.move_to(alpha*(3*RIGHT+2*UP))

class PruebaCustom(Scene):
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

class Aux(Scene):
    def construct(self):
        s = Square(color = RED, side_length=2)
        s_shrinked = Square(color = RED, side_length=2).scale(1+0.25)
        self.add(s, s_shrinked)


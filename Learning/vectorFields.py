from manim import *

class VField(Scene):
    def construct(self):
        func = lambda pos: np.array([
            -pos[0],
            pos[1]
        ])

        field = ArrowVectorField(func)

        self.play(*[GrowArrow(vec) for vec in field], run_time = 5)


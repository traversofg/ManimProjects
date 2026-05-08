from manim import *

class Updater(Scene):
    def construct(self):
        teal_dot = Dot(color=TEAL).move_to(LEFT+DOWN)
        pointer = Arrow(ORIGIN, UP+RIGHT).next_to(teal_dot.get_center(), DL)
        
        def shift_and_rotate_pointer(mob, dt):
            mob.shift(dt*UR)
            mob.rotate(
                PI*dt,
                about_point = teal_dot.get_center()
                )
        pointer.add_updater(shift_and_rotate_pointer)
        
        teal_dot.add_updater(
            lambda mob, dt: mob.shift(dt*UR)
        )

        self.add(teal_dot, pointer)
        self.update_self(0)
        self.wait(2)



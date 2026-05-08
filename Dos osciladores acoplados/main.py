from manim import *
from numpy import sqrt, sin, cos

class Osciladores(Scene):
    def construct(self):
        
        t = ValueTracker(0)

        # Parametros del problema
        A = 1.
        mass = 1.
        k_walls = 10
        k_union = 2
        
        # Frecuencias naturales
        w1 = sqrt(k_walls/mass)
        w2 = sqrt((k_walls + 2*k_union)/mass)

        # Frecuencias de batido
        w_mod  = (w2 - w1) / 2
        w_prom = (w1 + w2) / 2

        # Valores iniciales
        x0_a = 2*LEFT
        x0_b = 2*RIGHT
        
        # Ecuaciones de movimiento
        def x_a(time):
            return A*sin(w_prom*time)*sin(w_mod*time) + x0_a
        
        def x_b(time):
            return A*cos(w_prom*time)*cos(w_mod*time) + x0_b
        
        ### Acá empieza lo manimatico ###

        # Le regalo existencia a las masitas (perdon masitas)
        masa1 = Dot(color=BLUE)
        masa2 = Dot(color=RED)
        
        # Agrego updaters para MOVER los puntos al resultado de las ecuaciones de movimiento        
        masa1.add_updater(
            lambda mobj: mobj.move_to(
                x_a(t.get_value()) * RIGHT
            )
        )

        masa2.add_updater(
            lambda mobj: mobj.move_to(
                x_b(t.get_value()) * RIGHT
            )
        )

        # Agrego los "resortes" (por ahora simples lineas)
        spring_left  = always_redraw(
            lambda: Line(4*LEFT, masa1.get_left())
        )

        spring_union = always_redraw(
            lambda: Line(masa1.get_right(), masa2.get_left(), color=YELLOW)
        )

        sprint_right = always_redraw(
            lambda: Line(masa2.get_right(), 4*RIGHT)
        )

        # Ahora traigo a la vida a estas cosas y armo evol temporal
        self.add(masa1, masa2, spring_left, spring_union, sprint_right)

        self.play(
            t.animate.set_value(30),
            run_time=30,
            rate_func=linear
        )

        """
        NOTA: acá lo que estoy haciendo es animar unicamente el valor de tiempo 't' y usar ese valor
        para las funciones updaters que se encargan de mover el Mobject (las masitas) al lugar indicado
        por la ecuacion de movimiento con el valor actual de 't' pasado como parametro
        """
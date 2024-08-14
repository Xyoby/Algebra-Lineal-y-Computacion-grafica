from manim import *


class Formula(Scene):
    def construct(self):
        t = MathTex(r"\int_a^b f'(x) dx = f(b)- f(a)"," Hola","{a","\over","b}")
        coef_a_eliminar = 5
        coef_pivote =3
        coef_nuevo = MathTex("{", str(coef_a_eliminar), "\over", str(coef_pivote), "}").set_color(YELLOW)
        self.add(t)
        self.add(coef_nuevo)

from manim import *

class MathTexExample(Scene):
    def construct(self):
        i_range = range(3)  # Valores de i: 0, 1, 2
        j_range = range(3)  # Valores de j: 0, 1, 2

        for i in i_range:
            for j in j_range:
                # Crea la expresión matemática con MathTex
                expression = MathTex("(-1)^{", str(i), "+", str(j), "}")
                expression.scale(2)  # Ajusta el tamaño

                # Ubica la expresión en diferentes posiciones según i y j
                expression.move_to(RIGHT * i + UP * j)

                # Agrega la expresión a la escena y muestra durante 1 segundo
                self.play(Create(expression), run_time=1)
                self.wait(0.5)  # Espera 0.5 segundos

                # Elimina la expresión de la escena
                self.play(FadeOut(expression))

        self.wait(1)  # Espera 1 segundo al final

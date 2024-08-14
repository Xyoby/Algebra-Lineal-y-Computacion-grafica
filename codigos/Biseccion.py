from manim import *

class BisectionMethod(Scene):
    def construct(self):
        # Definir la función y su derivada
        def func(x):
            return x**2 - 2

        # Definir los límites inicial y final para el intervalo
        a = 1
        b = 2
        tolerance = 0.01

        # Configuración del gráfico
        axes = Axes(
            x_range=[0, 3, 1],
            y_range=[-3, 3, 1],
            x_length=7,
            y_length=4,
            axis_config={"color": BLUE},
        )

        # Función para dibujar la curva
        graph = axes.plot(func, color=BLUE)
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # Agregar el gráfico a la escena
        self.play(Create(axes), Create(graph), Write(labels))
        self.wait(1)

        # Crear etiquetas y puntos para a y b
        a_dot = Dot(axes.c2p(a, func(a)), color=RED)
        b_dot = Dot(axes.c2p(b, func(b)), color=GREEN)
        a_label = MathTex("a", color=RED).next_to(a_dot, DOWN)
        b_label = MathTex("b", color=GREEN).next_to(b_dot, DOWN)

        self.play(Create(a_dot), Create(b_dot), Write(a_label), Write(b_label))

        # Iterar el método de la bisección
        for _ in range(10):
            c = (a + b) / 2
            c_dot = Dot(axes.c2p(c, func(c)), color=YELLOW)
            c_label = MathTex("c").next_to(c_dot, DOWN)
            self.play(Create(c_dot), Write(c_label))

            if func(c) * func(a) < 0:
                b = c
                self.play(b_dot.animate.move_to(axes.c2p(b, func(b))), b_label.animate.next_to(b_dot, DOWN))
            else:
                a = c
                self.play(a_dot.animate.move_to(axes.c2p(a, func(a))), a_label.animate.next_to(a_dot, DOWN))

            if abs(b - a) < tolerance:
                break
            self.wait(1)

        self.wait(2)

# Ejecutar escena
if __name__ == "__main__":
    scene = BisectionMethod()
    scene.render()

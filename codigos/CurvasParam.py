from manim import *

class FunctionGraph(Scene):
    def construct(self):
        # Crear los ejes coordenados
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-2, 2],
            axis_config={"color": BLUE},
        )

        # Agregar etiquetas a los ejes
        axes_labels = axes.get_axis_labels(
            x_label=MathTex("x"),
            y_label=MathTex("y"),
        )

        # Definir una función y=f(x)
        def func(x):
            return x**2

        # Graficar la función
        graph = axes.plot(lambda x: func(x), color=WHITE)

        # Agregar un punto P en la gráfica
        point = Dot().move_to(graph.points[25])  # Punto en (1, 1)
        point.set_color(YELLOW)

        # Mostrar el punto P y el mensaje
        self.play(Create(axes), Write(axes_labels))
        self.wait(1)
        self.play(Create(graph), Create(point))
        self.wait(2)
        self.play(
            point.animate.shift(2 * RIGHT),  # Desplazar el punto hacia la derecha
            Write(MathTex("Estas coordenadas t")))
        self.wait(2)

        # Mostrar las coordenadas en términos de un parámetro t
        param_coords = MathTex("=(t, f(t))", " \\text{ donde } x=t, y =f(t)").next_to(axes_labels, DOWN)
        self.play(Write(param_coords))
        self.wait(2)

class ParametricCurve(Scene):
    def construct(self):
        # Crear un título para la segunda escena
        title = Tex("Definición de una Curva Paramétrica").scale(1.5)
        title.to_edge(UP)

        # Crear una curva paramétrica
        curve = ParametricFunction(
            lambda t: [2 * np.cos(t), 2 * np.sin(t), 0],  # Definir la curva paramétrica
            t_range=[0, 2 * PI],
            color=WHITE,
        )

        # Mostrar la curva paramétrica
        self.play(Write(title))
        self.wait(1)
        self.play(Create(curve))
        self.wait(3)

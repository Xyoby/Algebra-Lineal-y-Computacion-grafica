from manim import *

# Definición de la función matemática fuera de la clase
def func(x):
    return 0.5 * x**2 - 2  # Ejemplo de función polinómica, una parábola

class FunctionAndTableScene(Scene):
    def construct(self):
        # Configuración de los ejes
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-10, 10, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": BLUE}
        )
        axes.to_edge(LEFT, buff=0.5)  # Posicionamiento de los ejes a la izquierda

        # Graficar la función utilizando la función definida externamente 'func'
        graph = axes.plot(func, color=PURPLE, x_range=[-5, 5])
        graph_label = axes.get_graph_label(graph, label='y = 0.5x^2 - 2', x_val=-3, direction=UP)

        # Crear la tabla de valores usando la misma función 'func'
        headers = ["x", "y = f(x)"]
        rows = [[str(x), str(func(x))] for x in range(-5, 6)]  # Genera valores de x de -5 a 5
        table = Table([headers] + rows, include_outer_lines=True)
        table.scale(0.5)  # Escala la tabla para ajustar tamaño
        table.to_edge(RIGHT, buff=0.5)  # Posiciona la tabla a la derecha

        # Mostrar todo en la escena
        self.play(Create(axes), Create(graph), Write(graph_label))
        self.play(Create(table))
        self.wait(2)


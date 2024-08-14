from manim import *


def func(x):
    return x * (x - 4) * (x + 4) + 2


class FunctionGraphScene(Scene):
    def construct(self):
        # Título de la animación
        title = Text("Funciones: Definición y creación del mundo matemático", font_size=24)
        title.to_edge(UP)
        self.play(Write(title))
        signature = MarkupText("<i><b>JGQ</b></i>", color=WHITE, font_size=14)
        signature.to_edge(DOWN + LEFT)
        self.play(Write(signature))
        self.wait(2)


        #        self.play(FadeOut(title))

        # Crear el rectángulo de la función y etiquetas
        func_box = Rectangle(width=3, height=2, color=BLUE)
        func_label = Text("f", color=WHITE).move_to(func_box)
        self.play(Create(func_box), Write(func_label))

        # Crear vectores de entrada y salida
        input_arrow = Arrow(start=3 * LEFT, end=func_box.get_left(), buff=0.1, color=BLUE)
        input_label = Text("x", color=GREEN).next_to(input_arrow, LEFT)
        output_arrow = Arrow(start=func_box.get_right(), end=3 * RIGHT, buff=0.1, color=BLUE)
        output_label = Text("y", color=RED).next_to(output_arrow, RIGHT)
        self.play(Write(input_label))
        self.wait(1)
        self.play(Create(input_arrow))
        self.wait(1)
        self.play(Create(output_arrow))
        self.wait(1)
        self.play(Write(output_label))
        self.wait(2)

        # Animación de valores de x y y
        for x in [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]:
            y = func(x)
            new_input_label = Text(f" {x}", color=GREEN).next_to(input_arrow, LEFT)
            new_output_label = Text(f" {y}", color=RED).next_to(output_arrow, RIGHT)
            self.play(Transform(input_label, new_input_label), Transform(output_label, new_output_label))
            self.wait(0.3)

        # Mover los elementos para hacer espacio para la tabla
        new_input_label = Text("x", color=GREEN).next_to(input_arrow, LEFT)
        new_output_label = Text("y", color=RED).next_to(output_arrow, RIGHT)
        self.play(Transform(input_label, new_input_label), Transform(output_label, new_output_label))
        self.wait(2)

        formula_label = MarkupText(
            '<span color="RED">y</span> = f(<span color="GREEN">x</span>)',
            color=WHITE
        ).next_to(func_box, DOWN, buff=0.2)
        self.play(Write(formula_label))

        all_elements_group = VGroup(func_box, input_arrow, output_arrow, input_label, output_label, func_label,
                                    formula_label)
        self.play(all_elements_group.animate.scale(0.5),
                  run_time=2)  # Ajusta el run_time para controlar la velocidad de la animación
        new_position = LEFT * 5 + UP * 0  # Ajusta esta posición según necesites
        self.play(all_elements_group.animate.move_to(new_position), run_time=1)
        self.wait(1)
        #################################################################################
        # Crear tabla de valores con colores y tamaños específicos
        # headers = [Text("x", weight=BOLD), Text("y = f(x)", weight=BOLD)]
        headers = ["x", "y=f(x)"]
        rows = [[str(x), str(func(x))] for x in range(-5, 5)]

        # Creamos la tabla, especificando el estilo de la cabecera y de las celdas
        table = Table([headers] + rows, include_outer_lines=True)
        table.scale(0.4)  # Escalamos la tabla para ajustar al tamaño deseado
        table.to_edge(UP+5.2*LEFT, buff=1)  # Posicionamos la tabla un poco por debajo del título


        # Aplicamos colores a las columnas
        self.color_table_columns(table)
        self.play(Create(table))
        self.wait(2)
        #####################################  Ploteo

        axes = Axes(
            x_range=[-6, 6, 1],  # Define el rango en x con un paso de 1
            y_range=[-50, 50, 10],  # Define el rango en y con un paso de 10
            x_length=5,  # Longitud visual de los ejes x en la escena
            y_length=6,  # Longitud visual de los ejes y en la escena
            axis_config={"color": WHITE}  # Color de los ejes
        )
        axes.to_edge(RIGHT)  # Alinea los ejes hacia el borde derecho de la escena

        x_label = Tex("x", color=GREEN).next_to(axes.x_axis.get_end(), DOWN)  # Etiqueta para el eje x
        y_label = Tex("y", color=RED).next_to(axes.y_axis.get_end(), RIGHT)  # Etiqueta para el eje y

        # Animaciones para crear los ejes y añadir las etiquetas
        self.play(Create(axes))  # Crea los ejes en la escena
        self.play(Write(x_label), Write(y_label))  # Animar la escritura de las etiquetas
        self.wait(2)

        # Mostrar los puntos en los ejes
        dots = VGroup()
        for i, row in enumerate(rows):
            x, y = float(row[0]), float(row[1])
            dot = Dot(axes.c2p(x, y), color=YELLOW)
            dots.add(dot)
            # Resaltar la fila correspondiente en la tabla
            self.play(table.get_rows()[i+1].animate.set_fill(YELLOW, opacity=0.5), FadeIn(dot), run_time=0.5)
            self.wait(0.5)
            self.play(table.get_rows()[i+1].animate.set_fill(opacity=1), run_time=0.5)


        self.color_table_columns(table)
        self.play(Create(table))

        # Graficar la función usando la función definida `self.func`
        graph = axes.plot(func, color=BLUE,
                          x_range=[-5, 5])  # Asegúrate de que el x_range cubre el rango visible de los ejes

         # Visualización lenta de la curva
        self.play(Create(graph), run_time=4)  # Anima la creación de la gráfica lentamente
        self.wait(4)

        # Marcar dominio y rango con llaves y etiquetas

        domain_brace = Brace(Line(axes.c2p(-5, 0), axes.c2p(5, 0)), DOWN, buff=0.1)
        domain_label = domain_brace.get_text("Dominio")
        range_brace = Brace(Line(axes.c2p(0, -43), axes.c2p(0, 43)), 1.2*LEFT+0.4*UP, buff=0.1)
        range_label = range_brace.get_text("Rango")
        self.play(GrowFromCenter(domain_brace), Write(domain_label))
        self.play(GrowFromCenter(range_brace), Write(range_label))
        self.wait(2)





        self.wait(4)



    def color_table_columns(self, table):
        # Colorear la primera columna de verde, excepto la cabecera
        for i in range(1, len(table.get_rows())):  # Evitamos la cabecera
            table.get_entries((i, 0)).set_color(RED)

        # Colorear la segunda columna de rojo, excepto la cabecera
        for i in range(1, len(table.get_rows())+1):  # Evitamos la cabecera
            table.get_entries((i, 1)).set_color(GREEN)

    def adjust_header(self, table):
        # Ajustar el tamaño del texto en la cabecera
        for i in range(table.get_columns()):
            header_cell = table.get_entries(position=(0, i))
            header_cell.scale(1.2)  # Escalar las celdas de la cabecera

# Para ejecutar el script asegúrate de tener la última versión de Manim y usar el comando adecuado:
# manim -pqh script.py FunctionGraphScene

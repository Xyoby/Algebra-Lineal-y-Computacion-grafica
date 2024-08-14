from manim import *

class AxesAndVectors(Scene):
    def construct(self):
        # Primera escena: R2
        axes_2d = Axes(
            x_range=(-5, 5),
            y_range=(-5, 5),
            axis_config={"color": BLUE},
            x_axis_config={"include_tip": True},
            y_axis_config={"include_tip": True},
        )

        # Punto blanco en el origen
        origin_point_2d = Dot(point=axes_2d.coords_to_point(0, 0), color=WHITE)

        # Vector en el origen
        vector_at_origin_2d = Arrow(axes_2d.c2p(0, 0), axes_2d.c2p(1, 1), color=GREEN)

        # Vector v
        vector_v_2d = Arrow(axes_2d.c2p(0, 0), axes_2d.c2p(2, 3), color=YELLOW)

        # Recta que pasa por el origen y tiene la misma dirección que v
        line_through_origin_2d = Line(axes_2d.c2p(-5, -5), axes_2d.c2p(5, 5), color=RED)

        self.play(Create(axes_2d))
        self.wait(1)
        self.play(Create(origin_point_2d))
        self.wait(1)
        self.play(Create(vector_at_origin_2d))
        self.wait(1)
        self.play(Create(vector_v_2d))
        self.wait(1)
        self.play(Create(line_through_origin_2d))
        self.wait(1)
        self.play(Uncreate(axes_2d), Uncreate(origin_point_2d), Uncreate(vector_at_origin_2d), Uncreate(vector_v_2d), Uncreate(line_through_origin_2d))
        self.wait(1)

        class VectorsInR3(Scene):
            def construct(self):
                # Crear ejes 3D
                axes_3d = ThreeDAxes()

                # Crear vector 1 (color rojo)
                vector1_start = np.array([0, 0, 0])  # Punto de inicio del vector
                vector1_end = np.array([2, 1, 3])  # Punto final del vector
                vector1 = Arrow3D(start=vector1_start, end=vector1_end, color=RED)

                # Crear vector 2 (color verde)
                vector2_start = np.array([1, 2, 1])  # Punto de inicio del vector
                vector2_end = np.array([3, 4, 5])  # Punto final del vector
                vector2 = Arrow3D(start=vector2_start, end=vector2_end, color=GREEN)

                # Visualizar vectores
                self.play(Create(axes_3d))
                self.wait(1)
                self.play(Create(vector1))
                self.wait(1)
                self.play(Create(vector2))

                # (Opcional) Agregar etiquetas a los vectores
                vector1_label = Text3D("Vector 1", vector1.get_center(), color=RED)
                vector2_label = Text3D("Vector 2", vector2.get_center(), color=GREEN)
                self.play(Write(vector1_label))
                self.play(Write(vector2_label))

                # Esperar y finalizar la escena
                self.wait(3)

        if __name__ == "__main__":
            module_name = os.path.basename(__file__)
            command_A = "manim -pql " + module_name + " VectorsInR3"
            os.system(command_A)

        # Resumen textual
        summary = Text("""
        Subespacios de R2:
        - El vector nulo.
        - Las rectas que pasan por el origen de coordenadas.
        - Todo el espacio R2.

        Subespacios de R3:
        - El vector nulo.
        - Las rectas que pasan por el origen de coordenadas.
        - Los planos que pasan por el origen de coordenadas.
        - Todo el espacio R3.
        """).scale(0.7)

        self.play(Write(summary))
        self.wait(3)

if __name__ == "__main__":
    module_name = os.path.basename(__file__)
    command_A = "manim -pql " + module_name + " AxesAndVectors"
    os.system(command_A)

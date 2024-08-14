from manim import *

class ThreeDGraph(ThreeDScene):
    def construct(self):
        # Etapa 1: Ejes coordenados (x, y, z)
        self.set_camera_orientation(phi=PI/3, theta=PI/3)
        axes = ThreeDAxes()
        labels = axes.get_axis_labels(
            Tex("x").scale(0.7), Tex("y").scale(0.7), Tex("z").scale(0.7)
        )
        self.add(axes, labels)
        self.wait()

        # Etapa 2: Punto P(x_0, y_0, z_0)
        point = Sphere(radius=0.08, color=BLUE).shift(2 * RIGHT + 1 * UP + 1 * OUT)
        self.play(Create(point))
        self.wait()

        # Etapa 3: Vector dirección desde el origen
        vector = Vector(direction=RIGHT+UP+2*OUT, color=RED)
        self.play(Create(vector))
        self.wait()

        # Etapa 4: Recta infinita que pasa por P con dirección V
        line = Line3D(start=point.get_center()-10*vector.get_end(), end=point.get_center()+10*vector.get_end(), color=GREEN)
        self.play(Create(line))
        self.wait()

        # Etapa 5: Vector dirección desde P
        p_vector = Vector(direction=UP, color=YELLOW).shift(point.get_center())
        self.play(Create(p_vector))
        self.wait()



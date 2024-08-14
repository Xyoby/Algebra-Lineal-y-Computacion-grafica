from manim import *


class SurfaceRotation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        # Agregar título y logro
        title = Text(" Superficies\n Cuádricas", font_size=20).to_edge(LEFT,buff=1)
        author = Text(" X Chávez", font_size=10).next_to(title, DOWN)

        # Configuración de la animación
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # Cargar imagen
        image = ImageMobject("logo.png")
        image.scale(0.05).next_to(author, DOWN)
        self.add(title, author,image)

        # Lista de superficies cuádricas para mostrar
        surfaces = [
            Sphere().scale(0.5),
            Surface(
                lambda u, v: np.array([
                    u,
                    v,
                    u ** 2 - v ** 2
                ]), resolution=(10, 10), u_range=(-2, 2), v_range=(-2, 2),
            ).scale(0.5),
            Surface(
                lambda u, v: np.array([
                    u,
                    v,
                    np.sqrt(u ** 2 + v ** 2)
                ]), resolution=(10, 10), u_range=(-2, 2), v_range=(-2, 2),
            ).scale(0.5),
            Surface(
                lambda u, v: np.array([
                    u,
                    v,
                    np.sqrt(u ** 2 + v ** 2 + 1)
                ]), resolution=(10, 10), u_range=(-2, 2), v_range=(-2, 2),
            ).scale(0.5),
            Surface(
                lambda u, v: np.array([
                    u,
                    v,
                    u ** 2 - v ** 2
                ]), resolution=(10, 10), u_range=(-2, 2), v_range=(-2, 2),
            ).scale(0.5),
            Surface(
                lambda u, v: np.array([
                    u,
                    v,
                    u ** 2 + v ** 2
                ]), resolution=(10, 10), u_range=(-2, 2), v_range=(-2, 2),
            ).scale(0.5),
        ]



        # Agregar ejes y superficies a la escena
        self.add(axes)
        for surface in surfaces:
            self.play(Create(surface))
            self.play(Rotate(surface, axis=OUT, run_time=2, turns=1))
            self.play(Uncreate(surface))
            self.play(Uncreate(surface))

        self.wait(1)

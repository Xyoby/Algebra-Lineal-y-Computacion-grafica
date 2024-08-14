from manim import *

class Escena2(ThreeDScene):
    def construct(self):
        cielo = "#C4DDFF"
        azul = "#001D6E"
        rojo = "#B20600"
        self.camera.background_color = cielo
        axes = ThreeDAxes().set_color(azul)
        x=MathTex("x", color=azul).move_to(np.array([5,0.5,0]))
        y=MathTex("y", color=azul).move_to(np.array([0.5,5,0]))
        self.set_camera_orientation(phi=65 * DEGREES, theta=60 * DEGREES)
        self.add(axes,x,y)
        Surf1 = Text("Esfera", color=BLACK).to_corner(UL)
        self.add_fixed_in_frame_mobjects(Surf1)

        esfera = Surface(
            lambda u, v: np.array([
                2 * np.cos(v) * np.cos(u),
                2 * np.sin(v) * np.cos(u),
                2 * np.sin(u)]),
            u_range=[-PI, PI],
            v_range=[0, 2 * PI],
            resolution=(15, 32)
            )
        esfera.set_fill_by_checkerboard(rojo, azul, opacity=0.5)
        self.play(Write(esfera))
        self.wait(5)

        Surf2 = Text("Toro", color=BLACK).to_corner(UL)
        self.play(FadeOut(Surf1))
        self.add_fixed_in_frame_mobjects(Surf2)

        toro = Surface(
            lambda u, v: np.array([
                (3 + 1 * np.cos(v)) * np.cos(u),
                (3 + 1 * np.cos(v)) * np.sin(u),
                1 * np.sin(v)]),
            v_range=[0, 2 * PI],
            u_range=[-PI, PI],
            resolution=(15, 32))
        self.play(Transform(esfera, toro))
        self.wait(5)

        Surf3 = Text("Catenoide", color=BLACK).to_corner(UL)
        self.play(FadeOut(Surf2))
        self.add_fixed_in_frame_mobjects(Surf3)

        catenoide = Surface(
            lambda u, v: np.array([
                0.5 * np.cosh(v / 0.5) * np.cos(u),
                0.5 * np.cosh(v / 0.5) * np.sin(u),
                v]),
            v_range=[-1, 1],
            u_range=[-PI, PI],
            resolution=(5, 32))
        catenoide.set_fill_by_value(
            axes=axes, colors=[(RED, -1), (YELLOW, 0), (GREEN, 1)], axis=2
        )
        self.play(Transform(esfera, catenoide))
        self.wait(10)

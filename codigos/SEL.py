from manim import *

class ParaSurface(ThreeDScene):
    def func(self, u, v):
        u1 = np.array([1, 1, 1])
        u2 = np.array([0, 1, 1])
        return np.array(u * u1 + v* u2)

    def construct(self):
        axes = ThreeDAxes(x_range=(-3, 3, 1), y_range=(-3, 3, 1), z_range=(-3, 3, 0.5))
        self.set_camera_orientation(theta=-30 * DEGREES, phi=75 * DEGREES)

        plano = Surface(
            lambda u, v: axes.c2p(*self.func(u, v)),
            u_range=[0, 1],
            v_range=[0, 1],
            resolution=10,
        )
        u1 = np.array([1, 1, 1])
        u2 = np.array([0, 1, 1])
        arrow_u1 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=u1,
            resolution=8,
            color=YELLOW
        )
        arrow_u2 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=u2,
            resolution=8,
            color=GREEN_A
        )
        poly = Polygon([0,0,0], [1,1,1], [0,1,1])
        poly.set_fill(YELLOW_C,1)

        self.add(axes, arrow_u1, plano, arrow_u2, poly)
        objects_group=VGroup(axes,arrow_u1,arrow_u2,plano, poly)
        self.add(objects_group)
        self.play(Rotating(objects_group, radians=2 * PI, axis=OUT), run_time=4)


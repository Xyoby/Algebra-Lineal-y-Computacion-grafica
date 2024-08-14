from manim import *

class GramSchmidt3D(ThreeDScene):
    def func(self, u, v, x, y):
        return u * x + v * y

    def construct(self):
        # Escena 1: Muestra los ejes coordenados X, Y y Z
        axes = ThreeDAxes(x_range=(-2, 2, 1), y_range=(-2, 2, 1), z_range=(-2, 2, 1))
        self.set_camera_orientation(theta=-30 * DEGREES, phi=75 * DEGREES)
        self.add(axes)
        self.wait(1)

        # Escena 2: Muestra el primer vector u1------------------BLUE---------------------
        u1 = np.array([1, 1, 1])
        arrow_u1 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=u1,
            resolution=8,
            color=BLUE  #set_color(BLUE_B)
        )
        label_u1 = MathTex(r"\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}", color=BLUE)
        label_u1.rotate(PI / 2, axis=RIGHT).rotate(PI / 2, axis=OUT).scale(0.2)
        label_u1.next_to(u1)
        vector_u1 = VGroup(arrow_u1, label_u1)
        self.add(vector_u1)
        self.wait(1)



        # Escena 3: Calcula y muestra el vector v1
        v1 = u1 / np.linalg.norm(u1)
        arrow_v1 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=v1,
            resolution=8,
            color=BLUE_B
        )
        label_v1 = MathTex(r"\begin{bmatrix} \frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{3}} \\ \frac{1}{\sqrt{3}} \end{bmatrix}", color=BLUE_B)
        label_v1.rotate(PI / 2, axis=RIGHT).rotate(PI / 2, axis=OUT).scale(0.5)
        label_v1.next_to(v1).shift(2 * DOWN)
        vector_v1 = VGroup(arrow_v1 )
        self.play(Transform(vector_u1[0].copy(), vector_v1))
        self.play(Create(label_v1))
        self.wait(1)
        self.play(FadeOut(label_v1))

        # Escena 4: Muestra el segundo vector u2
        u2 = np.array([0, 1, 1])
        arrow_u2 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=u2,
            resolution=8,
            color=GREEN_E
        )
        label_u2 = MathTex(r"\begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}", color=GREEN_E)
        label_u2.rotate(PI / 2, axis=RIGHT).rotate(PI / 2, axis=OUT).scale(0.5)
        label_u2.next_to(u2)
        vector_u2 = VGroup(arrow_u2, label_u2)
        self.add(vector_u2)
        self.wait(1)

        # Escena 5: Calcula y muestra el vector v2
        proj_v2_u1 = np.dot(u2, v1) * v1
        v2 = u2 - proj_v2_u1
        v2 = v2 / np.linalg.norm(v2)
        arrow_v2 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=v2,
            resolution=8,
            color=GREEN_A
        )
        label_v2 = MathTex(r"\begin{bmatrix}- \frac{2}{\sqrt{6}}\\ \frac{1}{\sqrt{6}} \\ \frac{1}{\sqrt{6}} \end{bmatrix}", color=GREEN_A)
        label_v2.rotate(PI / 2, axis=RIGHT).rotate(PI / 2, axis=OUT).scale(0.5)
        label_v2.next_to(v2).shift(2 * DOWN)
        vector_v2 = VGroup(arrow_v2)
        self.play(Transform(vector_u2[0].copy(), vector_v2))
        self.play(Create(label_v2))
        self.wait(1)
        self.play(FadeOut(label_v2))

        plano = Surface(
            lambda  u, v: axes.c2p(*self.func(u, v, u1, u2)),
            u_range=[0, 1],
            v_range=[0, 1],
            resolution=10,
            )

        self.add(plano)



        # Escena 6: Muestra el tercer vector u3
        u3 = np.array([0, 0, 1])
        arrow_u3 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=u3,
            resolution=8,
            color=YELLOW
        )
        label_u3 = MathTex(r"\begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}", color=YELLOW)
        label_u3.rotate(PI / 2, axis=RIGHT).rotate(PI / 2, axis=OUT).scale(0.5)
        label_u3.next_to(u3)
        vector_u3 = VGroup(arrow_u3, label_u3)
        self.add(vector_u3)
        self.wait(1)

        # Escena 7: Calcula y muestra el vector v3
        proj_v3_u1 = np.dot(u3, v1) * v1
        proj_v3_v2 = np.dot(u3, v2) * v2

        arrow_p = Arrow3D(
            start=np.array([0, 0, 0]),
            end=proj_v3_u1 + proj_v3_v2,
            resolution=8,
            color=YELLOW
        )
        self.add(arrow_p)
        self.wait(1)

        v3 = u3 - proj_v3_u1 - proj_v3_v2
        v3 = v3 / np.linalg.norm(v3)
        arrow_v3 = Arrow3D(
            start=np.array([0, 0, 0]),
            end=v3,
            resolution=8,
            color=YELLOW_A
        )
        label_v3 = MathTex(r"\begin{bmatrix} 0 \\ -\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{bmatrix}", color=YELLOW_A)
        label_v3.rotate(PI / 2, axis=RIGHT).rotate(PI / 2, axis=OUT).scale(0.5)
        label_v3.next_to(v3).shift(2 * DOWN)
        vector_v3 = VGroup(arrow_v3)
        self.play(Transform(vector_u3[0].copy(), vector_v3))
        self.play(Create(label_v3))
        self.wait(1)
        self.play(FadeOut(label_v3))
        self.wait(2)




        objects_group = VGroup(axes, vector_u1, vector_v1,  vector_u2 , vector_v2, plano, arrow_p,  vector_u3 ,vector_v3 )
        #objects_group.move_to(axes.c2p(0, 0, 0))

        self.add(objects_group)
        self.play(Rotating(objects_group, radians=2 * PI, axis=OUT), run_time=4)
        self.wait(1)



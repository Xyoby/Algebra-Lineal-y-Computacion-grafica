from manim import *
import numpy as np


class VectorProperties(Scene):
    def construct(self):
        # Create a 2D vector space
        vector_space = ThreeDAxes(
            x_range=[-6, 6],
            y_range=[-6, 6],
            z_range=[-6, 6]
        )

        self.play(Create(vector_space))

        # Define a line passing through the origin
        line = Line(start=-6 * RIGHT - 3 * UP, end=6 * RIGHT + 3 * UP, color=BLUE)
        line_label = MathTex("L", color=BLUE).next_to(line, 0.1 * UP)

        # Define vectors as ordered triples
        vector1 = np.array([2, 1, 0])  # (2, 1, 0)
        vector2 = np.array([4, 2, 0])  # (4, 2, 0)

        # Create vectors on the line
        vector1_arrow = Arrow3D(ORIGIN, vector1, color=RED)
        vector2_arrow = Arrow3D(ORIGIN, vector2, color=GREEN)
        vector1_label = MathTex(r"\vec{u}", color=RED).next_to(vector1_arrow, 0.5 * UP)
        vector2_label = MathTex(r"\vec{v}", color=GREEN).next_to(vector2_arrow, 0.5 * UP)
        L1 = VGroup(line, line_label)
        v1 = VGroup(vector1_arrow, vector1_label)
        v2 = VGroup(vector2_arrow, vector2_label)
        v12 = VGroup(v1, v2)

        # Add vectors to the scene
        self.play(Create(L1))
        self.play(Create(v1))
        self.play(Create(v2))
        self.wait(1)

        # Show the property of vector addition
        sum_vector = vector1 + vector2
        sum_vector_arrow = Arrow3D(ORIGIN, sum_vector, color=YELLOW)
        sum_label = MathTex(r"\vec{u}+\vec{v}", color=YELLOW).next_to(sum_vector_arrow, UP)
        sv = VGroup(sum_vector_arrow, sum_label)
        self.play(ReplacementTransform(v12.copy(), sv))
        self.wait(1)
        self.play(FadeOut(v1, v2, sv))

        # Show the property of scalar multiplication
        scalar = 1.5
        scaled_vector = scalar * vector1
        scaled_vector_arrow = Arrow3D(ORIGIN, scaled_vector, color=PURPLE)
        scalar_label = MathTex(r"1.5\vec{u}", color=PURPLE).next_to(scaled_vector_arrow, UP)
        self.play(Create(v1))
        self.play(ReplacementTransform(vector1_arrow.copy().set_color(PURPLE), scaled_vector_arrow))
        self.play(Write(scalar_label))
        self.wait(4)


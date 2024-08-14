from manim import *

class VectorTransformationRx(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-4, 4],
            axis_config={"color": WHITE},
        )
        self.add(axes)

        # Create vector x
        vector_x = Vector([2, 3], color=BLUE)
        label_x = MathTex(r"\textbf{x}", color=BLUE)
        label_x.next_to(vector_x, UP)

        # Create vector T(x)
        vector_Tx = Vector([2, -3], color=BLUE)
        label_Tx = MathTex(r"T(\textbf{x})", color=BLUE)
        label_Tx.next_to(vector_Tx, DOWN)

        # Create a dashed line
        dashed_line = DashedLine(vector_x.get_end(), vector_Tx.get_end(), color=BLUE)

        # Show vectors and dashed line
        self.play(Create(vector_x.copy()), Write(label_x))
        self.wait(1)
        self.play(Create(vector_Tx), Write(label_Tx))
        self.wait(1)
        self.play(Create(dashed_line))

        # Display coordinates and transformation matrix
        coordinates_x = MathTex(r"\begin{bmatrix} 2 \\ 3 \end{bmatrix}", color=WHITE)
        coordinates_Tx = MathTex(r"\begin{bmatrix} 2 \\ -3 \end{bmatrix}", color=WHITE)
        transformation_matrix = MathTex(r"\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} 2 \\ 3 \end{bmatrix}= \begin{bmatrix} 2 \\ -3 \end{bmatrix}", color=WHITE)
        coordinates_x.next_to(vector_x, RIGHT)
        coordinates_Tx.next_to(vector_Tx, RIGHT)
        transformation_matrix.to_corner(UL)

        # Add coordinates and transformation matrix
        self.play(Write(coordinates_x), Write(coordinates_Tx), Write(transformation_matrix))

        # Apply transformation animation
        self.play(
            Transform(vector_x, vector_Tx),
            Transform(label_x, label_Tx),
            run_time=2,
        )

        self.wait(1)




class VectorTransformationRy(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-4, 4],
            axis_config={"color": WHITE},
        )
        self.add(axes)

        # Create vector x
        vector_x = Vector([2, 3], color=BLUE)
        label_x = MathTex(r"\textbf{x}", color=BLUE)
        label_x.next_to(vector_x,RIGHT+ UP)

        # Create vector T(x)
        vector_Tx = Vector([-2, 3], color=BLUE)  # Reflection over the y-axis
        label_Tx = MathTex(r"T(\textbf{x})", color=BLUE)
        label_Tx.next_to(vector_Tx, LEFT+UP)

        # Create a dashed line
        dashed_line = DashedLine(vector_x.get_end(), vector_Tx.get_end(), color=BLUE)

        # Show vectors and dashed line
        self.play(Create(vector_x.copy()), Write(label_x))
        self.wait(1)
        self.play(Create(vector_Tx), Write(label_Tx))
        self.wait(1)
        self.play(Create(dashed_line))

        # Display coordinates and transformation matrix
        coordinates_x = MathTex(r"\begin{bmatrix} 2 \\ 3 \end{bmatrix}", color=WHITE)
        coordinates_Tx = MathTex(r"\begin{bmatrix} -2 \\ 3 \end{bmatrix}", color=WHITE)
        transformation_matrix = MathTex(r"\begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 2 \\ 3 \end{bmatrix}= \begin{bmatrix} -2 \\ 3 \end{bmatrix}", color=WHITE)
        coordinates_x.next_to(vector_x, RIGHT)
        coordinates_Tx.next_to(vector_Tx, LEFT)
        transformation_matrix.to_edge(DOWN+LEFT)

        # Add coordinates and transformation matrix
        self.play(Write(coordinates_x), Write(coordinates_Tx))
        self.wait(0.5)
        self.play(Write(transformation_matrix))

        # Apply transformation animation
        self.play(
            Transform(vector_x, vector_Tx),
            Transform(label_x, label_Tx),
            run_time=2,
        )

        self.wait(1)

class VectorTransformationDiagonal(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-4, 4],
            y_range=[-4, 4],
            x_length =8,  # Longitud del eje x
            y_length = 8,
            axis_config={"color": WHITE },
        )
        self.add(axes)

        # Create vector x
        vector_x = Vector([2, 3], color=BLUE)
        label_x = MathTex(r"\textbf{x}", color=BLUE)
        label_x.next_to(vector_x, RIGHT + UP)

        # Define the transformation matrix
        reflection_matrix = np.array([[0, 1], [1, 0]])

        # Apply the linear transformation to the vector
        vector_Tx = vector_x.copy()
        vector_Tx.apply_matrix(reflection_matrix)
        label_Tx = MathTex(r"T(\textbf{x})", color=BLUE)
        label_Tx.next_to(vector_Tx, RIGHT + DOWN)

        # Create a dashed line
        dashed_line = DashedLine(vector_x.get_end(), vector_Tx.get_end(), color=BLUE)

        # Show vectors and dashed line
        self.play(Create(vector_x), Write(label_x))
        self.wait(1)
        self.play(Create(vector_Tx), Write(label_Tx))
        self.wait(1)
        self.play(Create(dashed_line))

        # Display coordinates and transformation matrix
        coordinates_x = MathTex(r"\begin{bmatrix} 2 \\ 3 \end{bmatrix}", color=WHITE)
        coordinates_Tx = MathTex(r"\begin{bmatrix} 3 \\ 2 \end{bmatrix}", color=WHITE)
        transformation_matrix = MathTex(r"\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 2 \\ 3 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}", color=WHITE)
        coordinates_x.next_to(vector_x, RIGHT)
        coordinates_Tx.next_to(vector_Tx, LEFT)
        transformation_matrix.to_edge(DOWN + LEFT)

        # Add coordinates and transformation matrix
        self.play(Write(coordinates_x), Write(coordinates_Tx))
        self.wait(0.5)
        self.play(Write(transformation_matrix))

        # Apply transformation animation
        self.play(
            Transform(vector_x, vector_Tx),
            Transform(label_x, label_Tx),
            run_time=2,
        )

        self.wait(1)


from manim import *

class VectorTransformation3D(ThreeDScene):
    def construct(self):
        # Create axes and grid
        axes = ThreeDAxes(x_range=[-4, 4], y_range=[-4, 4], z_range=[-1, 3])
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        self.add(axes)

        # Create vector x
        vector_x = Arrow3D(start=ORIGIN, end=np.array([1, 2, 2]), color=BLUE)
        label_x = MathTex(r"\mathbf{x}", color=BLUE)
        label_x.next_to(vector_x, UR)

        # Define the transformation matrix
        reflection_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])

        # Apply the linear transformation to the vector
        vector_Tx = vector_x.copy()
        vector_Tx.apply_matrix(reflection_matrix)
        label_Tx = MathTex(r"T(\mathbf{x})", color=BLUE)
        label_Tx.next_to(vector_Tx, RIGHT + DOWN)

        # Create a dashed line
        # dashed_line = DashedLine3D(vector_x.get_end(), vector_Tx.get_end(), color=BLUE)

        # Show vectors and dashed line
        self.play(Create(vector_x), Write(label_x))
        self.wait(1)
        self.play(Create(vector_Tx), Write(label_Tx))
        self.wait(1)
        #self.play(Create(dashed_line))

        # Display coordinates and transformation matrix
        coordinates_x = MathTex(r"\begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}", color=WHITE)
        coordinates_Tx = MathTex(r"\begin{bmatrix} 1 \\ 2 \\ -2 \end{bmatrix}", color=WHITE)
        transformation_matrix = MathTex(
            r"\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ -2 \end{bmatrix}",
            color=WHITE
        )
        coordinates_x.next_to(vector_x, RIGHT)
        coordinates_Tx.next_to(vector_Tx, LEFT)
        transformation_matrix.to_corner(UL)

        # Add coordinates and transformation matrix
        self.play(Write(coordinates_x), Write(coordinates_Tx), Write(transformation_matrix))

        # Apply transformation animation
        self.play(
            Transform(vector_x, vector_Tx),
            Transform(label_x, label_Tx),
            run_time=2,
        )

        self.wait(1)

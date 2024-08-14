from manim import *
import numpy as np

class SubmatricesVisualization(Scene):
    def construct(self):
        # Define the matrix A
        matrix_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matrix = Matrix(matrix_data)
        self.play(Create(matrix))

        # Get the submatrices by removing rows and columns
        submatrices = []
        for row_idx in range(3):
            for col_idx in range(3):
                submatrix_data = np.delete(np.delete(matrix_data, row_idx, axis=0), col_idx, axis=1)
                submatrix = Matrix(submatrix_data)
                submatrix.set_color(ORANGE)
                submatrix.next_to(matrix, RIGHT)
                submatrices.append(submatrix)

        # Define the destination position for submatrices
        destination_position = DOWN * 2

        # Animate the visualization of submatrices
        for submatrix in submatrices:
            self.play(Transform(submatrix, submatrix.copy().next_to(destination_position)))
            self.wait(1)

        self.wait(2)

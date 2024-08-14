from manim import *
import numpy as np

class RecursiveCofactorExpansion(Scene):
    def construct(self):
        # Crear la matriz original
        matrix_data = np.array([
            [1, 2, 3, 4],
            [8, 5, 1, 1],
            [2, 0, 8, 6],
            [0, 1, 4, 7]
        ])

        # Extraer la matriz triangular superior
        upper_triangular = matrix_data #np.triu(matrix_data)
        matrix = Matrix(upper_triangular)
        matrix.scale(0.6).to_edge(0.5*UP+LEFT)
        self.play(Write(matrix))
        self.wait(1)

        # Iniciar el proceso de expansión por cofactores recursiva
        det_value = self.calculate_determinant(upper_triangular, matrix, depth=0)

        # Mostrar el resultado final del determinante
        det_label = MathTex("\\text{det}(A) = ", str(det_value)).scale(0.4).to_edge(2*DOWN)
        self.play(Write(det_label))
        self.wait(2)

    def calculate_determinant(self, matrix_data, parent_matrix, depth):
        # Caso base: si la matriz es de 1x1, devuelve su único elemento
        if matrix_data.size == 1:
            return matrix_data[0][0]

        det_value = 0
        for i in range(matrix_data.shape[0]):
            element = parent_matrix.get_entries()[i * matrix_data.shape[1]]  # Elemento de la primera columna
            highlight_box = SurroundingRectangle(element, color=YELLOW)
            self.play(Create(highlight_box))
            self.wait(0.5)

            # Calcular el menor y su determinante
            sign = (-1) ** (i + 1)
            minor_data = np.delete(np.delete(matrix_data, i, axis=0), 0, axis=1)
            minor_matrix = Matrix(minor_data).scale(0.3).next_to(parent_matrix, RIGHT, buff=1 + depth)
            self.play(Write(minor_matrix))

            # Recursión para calcular el determinante del menor
            minor_det = self.calculate_determinant(minor_data, minor_matrix, depth + 1)
            cofactor = sign * matrix_data[i][0] * minor_det
            det_value += cofactor

            self.play(FadeOut(highlight_box), FadeOut(minor_matrix))
            self.wait(0.5)

        return det_value

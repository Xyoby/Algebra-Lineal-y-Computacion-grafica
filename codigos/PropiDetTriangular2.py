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

        # Crear la matriz en Manim usando los datos originales
        matrix = Matrix(matrix_data)
        matrix.scale(0.6).to_edge(UP+2*LEFT)
        self.play(Create(matrix))
        self.wait(1)

        # Iniciar el proceso de expansión por cofactores recursiva
        det_value = self.calculate_determinant(matrix_data, matrix, depth=0)

        # Mostrar el resultado final del determinante
        det_label = MathTex(r"\text{det}(A) = ", f"{det_value:.2f}").scale(0.7).to_edge(DOWN)
        self.play(Write(det_label))
        self.wait(2)

    def calculate_determinant(self, matrix_data, parent_matrix, depth):
        if matrix_data.size == 1:
            return matrix_data[0][0]  # Caso base, devuelve el único elemento en una matriz 1x1

        det_value = 0
        sign = 1  # Alternar signos para cada elemento de la primera columna
        for i in range(matrix_data.shape[0]):
            # Elemento actual y resaltado
            element = parent_matrix.get_entries()[i * matrix_data.shape[1]]
            highlight_box = SurroundingRectangle(element, color=YELLOW)
            self.play(Create(highlight_box))
            self.wait(0.5)

            # Calcular el menor y su determinante
            sign = (-1) ** (i + 1)
            minor_data = np.delete(np.delete(matrix_data, i, axis=0), 0, axis=1)

            minor_matrix = Matrix(minor_data).scale(0.3).next_to(parent_matrix, RIGHT, buff=1 + depth)
            self.play(TransformFromCopy(element, minor_matrix))

            # Recursión para calcular el determinante del menor
            minor_det = self.calculate_determinant(minor_data, minor_matrix, depth + 1)
            cofactor = sign * matrix_data[i][0] * minor_det
            det_value += cofactor

            self.play(FadeOut(highlight_box), FadeOut(minor_matrix))
            self.wait(0.5)

        return det_value

from manim import *
import numpy as np
from fractions import Fraction

def rationalize(number):
    """ Helper function to convert a float to a rational number, returns a LaTeX string. """
    frac = Fraction(number).limit_denominator()
    if frac.denominator == 1:
        return f"{frac.numerator}"
    else:
        return f"\\frac{{{frac.numerator}}}{{{frac.denominator}}}"

class MatrixWithRationals(Matrix):
    """ Custom Matrix class to handle rational numbers. """
    def __init__(self, matrix_data, **kwargs):
        rationalized_data = [[rationalize(number) for number in row] for row in matrix_data]
        super().__init__(rationalized_data, **kwargs)

class RecursiveCofactorExpansion(Scene):
    def construct(self):
        # Crear la matriz original
        matrix_data = np.array([
            [1, 2, 3, 4],
            [8, 5, 1, 1],
            [2, 0, 8, 6],
            [0, 1, 4, 7]
        ])

        matrix = MatrixWithRationals(matrix_data)
        matrix.scale(0.6).to_edge(UP)
        self.play(Write(matrix))
        self.wait(1)

        # Iniciar el proceso de expansión por cofactores recursiva
        det_value = self.calculate_determinant(matrix_data, matrix, depth=0)

        # Mostrar el resultado final del determinante
        det_value_rational = rationalize(det_value)
        det_label = MathTex("\\text{det}(A) = ", det_value_rational).scale(0.7).to_edge(DOWN)
        self.play(Write(det_label))
        self.wait(2)

    def calculate_determinant(self, matrix_data, parent_matrix, depth):
        if matrix_data.size == 1:
            return matrix_data[0][0]  # Caso base, devuelve el único elemento en una matriz 1x1

        det_value = 0
        sign = 1  # Alternar signos para cada elemento de la columna
        for i in range(matrix_data.shape[0]):
            element = parent_matrix.get_entries()[i * matrix_data.shape[1]]
            highlight_box = SurroundingRectangle(element, color=YELLOW)
            self.play(Create(highlight_box))
            self.wait(0.5)

            minor_data = np.delete(np.delete(matrix_data, i, axis=0), 0, axis=1)
            minor_matrix = MatrixWithRationals(minor_data).scale(0.3)
            minor_matrix.move_to(3*RIGHT + 3*DOWN)

            minor_det = self.calculate_determinant(minor_data, minor_matrix, depth + 1)

            cofactor = sign * matrix_data[i][0] * minor_det
            det_value += cofactor

            self.play(FadeOut(highlight_box), FadeOut(minor_matrix))
            self.wait(0.5)

            sign *= -1  # Cambiar el signo para el siguiente cofactor

        return det_value

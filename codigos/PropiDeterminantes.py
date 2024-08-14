from manim import *
import numpy as np

class DeterminantProperties(Scene):
    def construct(self):
        # Crear una matriz
        matrix_data = [[1, 2, 3, 4],
                       [8, 5, 1, 1],
                       [2, 0, 8, 6],
                       [0, 1, 4, 7]]
        matrix = Matrix(matrix_data)
        matrix.to_edge(UP)

        # Propiedad 1: det(A) para una matriz triangular A
        # Supongamos que A ya es triangular en este caso
        self.play(Write(matrix))
        det_A = round(np.linalg.det(matrix_data), 2)
        det_A_text = MathTex("\\text{det}(A) = ", str(det_A)).next_to(matrix, DOWN)
        self.play(Write(det_A_text))
        self.wait(2)

        # Propiedad 2: det(cA) = c^n det(A) para cualquier constante c y matriz A
        # Ilustrar la propiedad con una constante c
        c = 2
        c_matrix_data = np.multiply(c, matrix_data)
        c_matrix = Matrix(c_matrix_data)
        self.play(Transform(matrix, c_matrix))
        det_cA = round(np.linalg.det(c_matrix_data), 2)
        det_cA_text = MathTex("\\text{det}(cA) = ", str(c), "^n \\cdot \\text{det}(A) = ", str(det_cA))
        det_cA_text.next_to(c_matrix, DOWN)
        self.play(Transform(det_A_text, det_cA_text))
        self.wait(2)

        # Propiedad 3: det(A) = -det(B) si B se obtiene al intercambiar dos filas de A
        # Ilustrar la propiedad intercambiando dos filas
        matrix_data_swapped = matrix_data.copy()
        matrix_data_swapped[1], matrix_data_swapped[2] = matrix_data_swapped[2], matrix_data_swapped[1]
        matrix_swapped = Matrix(matrix_data_swapped)
        self.play(Transform(matrix, matrix_swapped))
        det_B = round(np.linalg.det(matrix_data_swapped), 2)
        det_B_text = MathTex("\\text{det}(A) = -\\text{det}(B) = ", str(-det_B))
        det_B_text.next_to(matrix_swapped, DOWN)
        self.play(Transform(det_A_text, det_B_text))
        self.wait(2)

        # ... Continúa con el resto de las propiedades ...

        # Finaliza la escena
        self.wait(2)

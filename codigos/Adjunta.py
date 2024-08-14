from manim import *
import numpy as np

class AdjuntaMatrix(Scene):
    def construct(self):
        # Agregar título
        title = Text("Determinante y Matriz Adjunta", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Crear matriz original
        matrix_data = np.array([[4, -1, 1], [4, 5, 3], [2, 0, 0]])
        matrix = Matrix(matrix_data, include_background_rectangle=True)
        matrix.to_edge(LEFT-RIGHT).shift(LEFT)
        self.play(Write(matrix))
        self.wait(1)

        # Calcular la adjunta
        det = np.linalg.det(matrix_data)
        adjoint_data = np.linalg.inv(matrix_data) * det
        adjoint_matrix = Matrix(adjoint_data.round().astype(int), include_background_rectangle=True)
        adjoint_matrix.next_to(matrix, RIGHT, buff=0.5)

        # Mostrar la adjunta
        self.play(TransformFromCopy(matrix, adjoint_matrix))
        self.wait(1)

        # Multiplicación para verificar A * Adj(A) = det(A) I
        product_data = np.dot(matrix_data, adjoint_data)
        identity_matrix = Matrix(product_data.round().astype(int), include_background_rectangle=True)
        identity_matrix.next_to(adjoint_matrix, RIGHT, buff=1)

        # Animación de multiplicación
        self.play(Write(identity_matrix))
        self.wait(2)

        # Eliminar todas las matrices y mostrar la inversa
        inverse_data = adjoint_data / det
        inverse_matrix = Matrix(inverse_data.round(2), include_background_rectangle=True)
        inverse_matrix.move_to(ORIGIN)

        self.play(
            FadeOut(matrix), FadeOut(adjoint_matrix), FadeOut(identity_matrix),
            TransformFromCopy(adjoint_matrix, inverse_matrix)
        )
        self.wait(2)

        # Mostrar etiqueta de la inversa
        inverse_label = MathTex(r"A^{-1} = \frac{1}{\text{det}(A)} \text{Adj}(A)")
        inverse_label.next_to(inverse_matrix, DOWN)
        self.play(Write(inverse_label))
        self.wait(2)

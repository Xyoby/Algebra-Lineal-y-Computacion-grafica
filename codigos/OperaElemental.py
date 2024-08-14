from manim import *


class MatrixOperations(Scene):
    def construct(self):
        # Datos iniciales de la matriz A.
        data_a = [[1, 2, 3], [2, -4, 6], [3, -9, -3]]

        # Crear la matriz original A y escalarla.
        matrix_a = Matrix(data_a).scale(0.7)
        matrix_a.to_edge(UP, buff=1)  # Mover a la parte superior de la escena

        # Crear la matriz resultante del intercambio de filas 2 y 3 y escalarla.
        data_swapped = [data_a[0], data_a[2], data_a[1]]  # Cambia los datos primero.
        matrix_swapped = Matrix(data_swapped).scale(0.7)

        # Crear la matriz resultante de multiplicar la fila 1 por -2 y sumarla a la fila 2, luego escalar.
        data_modified = [data_swapped[0],
                         [data_swapped[1][i] - 2 * data_swapped[0][i] for i in range(len(data_swapped[0]))],
                         data_swapped[2]]
        matrix_modified = Matrix(data_modified).scale(0.7)

        # Crear la matriz resultante de multiplicar la fila 3 por 1/2 y escalar.
        data_final = [data_modified[0], data_modified[1],
                      [int(1 / 2 * data_modified[2][i]) for i in range(len(data_modified[2]))]]
        matrix_final = Matrix(data_final).scale(0.7)

        # Organizar las matrices modificadas en la parte inferior de la escena.
        matrices_group = VGroup(matrix_swapped, matrix_modified, matrix_final).arrange(RIGHT, buff=1).next_to(matrix_a,
                                                                                                              DOWN,
                                                                                                              buff=1)

        # Animar la creación de la matriz original.
        self.play(Create(matrix_a))
        self.wait(1)

        # Animar secuencialmente las transformaciones y colocaciones de las otras matrices.
        self.play(ReplacementTransform(matrix_a.copy(), matrix_swapped))
        self.wait(1)
        self.play(ReplacementTransform(matrix_swapped.copy(), matrix_modified))
        self.wait(1)
        self.play(ReplacementTransform(matrix_modified.copy(), matrix_final))
        self.wait(1)

        # Ajustar la posición de la agrupación de matrices si es necesario.
        self.play(matrices_group.animate.scale(0.7))
        self.wait()

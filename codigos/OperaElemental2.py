from manim import *

class MatrixOperations(Scene):
    def construct(self):
        # Datos iniciales de la matriz A.
        data_a = [[1, 2, 3], [2, -4, 6], [3, -9, -3]]

        # Crear la matriz original A y escalarla.
        matrix_a = Matrix(data_a).scale(0.7)
        matrix_a.to_edge(UP, buff=1)  # Mover a la parte superior de la escena

        # Matriz identidad para las operaciones elementales
        identity_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

        # 1. Intercambio de filas 2 y 3 en la matriz identidad
        identity_swapped = identity_matrix.copy()
        identity_swapped[1], identity_swapped[2] = identity_swapped[2], identity_swapped[1]
        matrix_elemental_swap = Matrix(identity_swapped).scale(0.7)

        # 2. Multiplicar la fila 1 por -2 (y sumarla a la fila 2) en la matriz identidad
        identity_modified = identity_matrix.copy()
        identity_modified[1] = [-2 if i == 0 else (1 if i == 1 else 0) for i in range(3)]
        matrix_elemental_modify = Matrix(identity_modified).scale(0.7)

        # 3. Multiplicar la fila 3 por 1/2 en la matriz identidad
        identity_final = identity_matrix.copy()
        identity_final[2] = [0.5 if i == 2 else (1 if i == i else 0) for i in range(3)]
        matrix_elemental_final = Matrix(identity_final).scale(0.7)

        # Crear las matrices resultantes de las operaciones
        data_swapped = [data_a[0], data_a[2], data_a[1]]
        matrix_swapped = Matrix(data_swapped).scale(0.7)

        data_modified = [data_swapped[0],
                         [data_swapped[1][i] - 2 * data_swapped[0][i] for i in range(len(data_swapped[0]))],
                         data_swapped[2]]
        matrix_modified = Matrix(data_modified).scale(0.7)

        data_final = [data_modified[0], data_modified[1],
                      [int(1 / 2 * data_modified[2][i]) for i in range(len(data_modified[2]))]]
        matrix_final = Matrix(data_final).scale(0.7)

        # Organizar y mostrar las matrices modificadas y sus matrices elementales asociadas
        matrices_group = VGroup(matrix_swapped, matrix_modified, matrix_final).arrange(RIGHT, buff=1).next_to(matrix_a, DOWN, buff=1)
        matrices_elemental_group = VGroup(matrix_elemental_swap, matrix_elemental_modify, matrix_elemental_final).arrange(RIGHT, buff=1).next_to(matrices_group, DOWN, buff=0.5)

        self.play(Create(matrix_a))
        self.wait(1)

        self.play(ReplacementTransform(matrix_a.copy(), matrix_swapped))
        self.wait(1)
        self.play(Write(matrix_elemental_swap.next_to(matrix_swapped, DOWN, buff=0.5)))
        self.wait(1)

        self.play(ReplacementTransform(matrix_swapped.copy(), matrix_modified))
        self.wait(1)
        self.play(Write(matrix_elemental_modify.next_to(matrix_modified, DOWN, buff=0.5)))
        self.wait(1)

        self.play(ReplacementTransform(matrix_modified.copy(), matrix_final))
        self.wait(1)
        self.play(Write(matrix_elemental_final.next_to(matrix_final, DOWN, buff=0.5)))
        self.wait(1)

from manim import *

class MatrixTransformation(Scene):
    def construct(self):
        # Crear una matriz original
        matrix_original = Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])

        self.play(Create(matrix_original.move_to(UP)))

        # Extraer una submatriz de 2x2
        submatrix = Matrix([
            [5, 6],
            [8, 9]
        ]).move_to(2*DOWN)

    #    elements = [matrix_original.get_entries()[i][j] for i in range(1, 3) for j in range(1, 3)]
    #    self.play(TransformFromCopy(VGroup(*elements), submatrix))

        m = self.get_submatrix(matrix_original, 1, 1)
        minor = m[0].copy().move_to(2*DOWN)
        self.play(TransformFromCopy(m, minor))


        self.wait(1)

    def get_submatrix(self, matrix, rows, cols):
        submatrix_elements = []
        for i in range(3):
            for j in range(3):
                if i !=rows and j != cols:
                    submatrix_elements.append(matrix.get_entries()[i + 3 * j])
        return VGroup(*submatrix_elements)
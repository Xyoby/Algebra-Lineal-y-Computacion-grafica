from manim import *

class ReducedRowEchelonForm(Scene):
    def construct(self):
        # Define la matriz inicial A.
        A = [[1, 3, -2, 0, 2, 0],
             [2, 6, -5, -2, 4, -3],
             [0, 0, 5, 10, 0, 15],
             [2, 6, 0, 8, 4, 8]]

        # Crea la matriz de Manim y la muestra.
        matrix_mob = Matrix(A).scale(0.5)
        self.add(matrix_mob)
        self.wait(1)

        m, n = len(A), len(A[0])

        for pivot_row in range(m):
            # Encuentra la columna pivote.
            pivot_col = next((i for i, x in enumerate(A[pivot_row]) if x != 0), None)

            # Verifica si existe una columna pivote y no es cero.
            if pivot_col is not None and A[pivot_row][pivot_col] != 0:
                # Escala la fila para hacer el pivote 1.
                pivot = A[pivot_row][pivot_col]
                A[pivot_row] = [x / pivot for x in A[pivot_row]]
                new_matrix_mob = Matrix(A).scale(0.5)
                self.play(Transform(matrix_mob, new_matrix_mob))
                self.wait(1)

                # Realiza la eliminación de filas para hacer ceros por encima y por debajo del pivote.
                for target_row in range(m):
                    if target_row != pivot_row and A[target_row][pivot_col] != 0:
                        factor = A[target_row][pivot_col]
                        A[target_row] = [x - factor * y for x, y in zip(A[target_row], A[pivot_row])]
                        new_matrix_mob = Matrix(A).scale(0.5)
                        self.play(Transform(matrix_mob, new_matrix_mob))
                        self.wait(1)

        # Mueve las filas cero al final.
        zero_rows = [row for row in A if all(x == 0 for x in row)]
        non_zero_rows = [row for row in A if any(x != 0 for x in row)]
        A = non_zero_rows + zero_rows
        new_matrix_mob = Matrix(A).scale(0.5)
        self.play(Transform(matrix_mob, new_matrix_mob))
        self.wait(2)

        # Finalmente, mostrar la matriz en su forma escalonada reducida.
        reduced_row_echelon_label = Text("Reduced Row Echelon Form of A:").to_edge(UP)
        self.play(Write(reduced_row_echelon_label), Transform(matrix_mob, new_matrix_mob))
        self.wait(2)

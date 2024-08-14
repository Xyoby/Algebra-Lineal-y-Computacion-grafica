from manim import *

class RowEchelonForm(Scene):
    def construct(self):
        # Given matrix A
        A = [[1, 3, -2, 0, 2, 0],
             [2, 6, -5, -2, 4, -3],
             [0, 0, 5, 10, 0, 15],
             [2, 6, 0, 8, 4, 8]]

        # Display original matrix A
        original_matrix = Matrix(A, element_alignment_corner=ORIGIN)
        original_matrix.scale(0.8)
        self.play(Create(original_matrix))
        self.wait()

        # Perform row operations for REF
        m, n = len(A), len(A[0])
        for i in range(m - 1):
            if A[i][i] == 0:
                _, max_row = max((abs(A[j][i]), j) for j in range(i + 1, m))
                A[i], A[max_row] = A[max_row], A[i]
                self.play(Transform(original_matrix, Matrix(A, element_alignment_corner=ORIGIN).scale(0.8)))
                self.wait()

            if A[i][i] != 0:
                A[i] = [int(x / A[i][i]) for x in A[i]]
                self.play(Transform(original_matrix, Matrix(A, element_alignment_corner=ORIGIN).scale(0.8)))
                self.wait()

            for j in range(i + 1, m):
                if A[j][i] != 0:
                    factor = A[j][i]
                    A[j] = [x - factor * y for x, y in zip(A[j], A[i])]
                    self.play(Transform(original_matrix, Matrix(A, element_alignment_corner=ORIGIN).scale(0.8)))
                    self.wait()

        # Display row echelon form of A
        self.play(Transform(original_matrix, Matrix(A, element_alignment_corner=ORIGIN).scale(0.8, about_edge=UL)))
        self.wait()

        # Perform additional row operations for RREF
        for i in range(m - 1, 0, -1):
            for j in range(i - 1, -1, -1):
                if A[j][i] != 0:
                    factor = A[j][i]
                    A[j] = [x - factor * y for x, y in zip(A[j], A[i])]
                    self.play(Transform(original_matrix, Matrix(A, element_alignment_corner=ORIGIN).scale(0.8)))
                    self.wait()

        # Display reduced row echelon form of A
        self.play(Transform(original_matrix, Matrix(A, element_alignment_corner=ORIGIN).scale(0.8, about_edge=DL)))
        self.wait()

        # Add labels
        labels = VGroup(
            Text("Row interchange", color=WHITE),
            Text("Row scaling", color=WHITE),
            Text("Row replacement", color=WHITE),
        )
        labels.arrange(DOWN, buff=0.5)
        labels.next_to(original_matrix, DOWN, buff=0.5)
        self.play(Create(labels))
        self.wait()

        # Final message
        final_message = Text("Reduced Row Echelon Form (RREF)", color=WHITE)
        final_message.next_to(original_matrix, DOWN, buff=0.5)
        self.play(Transform(labels, final_message))
        self.wait()

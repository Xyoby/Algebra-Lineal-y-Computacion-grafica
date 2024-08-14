from manim import *

class DeterminantByCofactors(Scene):
    def construct(self):
        matrix = Matrix([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
        self.play(Create(matrix))
        self.wait()

        # Choose a random row to visualize cofactors
        row_index = 0
        row = matrix.get_mob_matrix()[row_index]
        cofactors = [self.calculate_cofactor(matrix.get_mob_matrix, row_index, col) for col in range(3)]

        # Display the cofactors step by step
        for col, cofactor in enumerate(cofactors):
            cofactor_text = f"Cofactor of ({row_index+1}, {col+1})"
            cofactor_value = Integer(cofactor).scale(0.8)
            text_group = VGroup(Text(cofactor_text).scale(0.8), cofactor_value)
            text_group.arrange(DOWN, buff=0.3).next_to(matrix, RIGHT)
            self.play(Write(text_group))
            self.wait()

    def calculate_cofactor(self, matrix, row, col):
        minor_matrix = np.delete(np.delete(matrix, row, axis=0), col, axis=1)
        minor_determinant = np.linalg.det(minor_matrix)
        cofactor = (-1) ** (row + col) * minor_determinant
        return cofactor

# Run the animation
if __name__ == "__main__":
    scene = DeterminantByCofactors()
    scene.render()

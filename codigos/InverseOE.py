from manim import *

class GaussJordanInversionAdjusted(Scene):
    def construct(self):
        # Matriz A original
        A = [[1, -1, 3], [0, 2, 4], [0, 0, -5]]
        # Matriz identidad I
        I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

        matrix_A = Matrix(A).scale(0.5)
        matrix_A.to_edge(UP)

        matrix_A = Matrix(A).scale(0.5)
        matrix_A.to_edge(UP)
        steps_titles = [
            "Matriz A Original",
            "Matriz Aumentada Inicial [A|I]"
        ]

        title_A = Text(steps_titles[0], font_size=20).scale(0.5).next_to(matrix_A, UP)
        self.play(Write(title_A), Write(matrix_A))
        self.wait(1)

        # Define los datos de las matrices para cada paso del proceso.
        matrices_data = [
            [[1, -1, 3, 1, 0, 0], [0, 2, 4, 0, 1, 0], [0, 0, -5, 0, 0, 1]],  # Matriz aumentada inicial [A|I]
            [[1, -1, 3, 1, 0, 0], [0, 2, 4, 0, 1, 0], [0, 0, 1, 0, 0, -1/5]],  # R3 = R3 / -5
            [[1, -1, 0, 1, 0, 3/5], [0, 2, 0, 0, 1, 4/5], [0, 0, 1, 0, 0, -1/5]],  # R1 = R1 - 3R3, R2 = R2 - 4R3
            [[1, -1, 0, 1, 0, 3/5], [0, 1, 0, 0, 1/2, 2/5], [0, 0, 1, 0, 0, -1/5]],  # R2 = R2 / 2
            [[1, 0, 0, 1, 1/2, 1], [0, 1, 0, 0, 1/2, 2/5], [0, 0, 1, 0, 0, -1/5]]  # R1 = R1 + R2
        ]

        # Títulos para cada paso.
        titles = [
            "Matriz aumentada inicial [A|I]",
            "R3 = R3 / -5",
            "R1 = R1 - 3R3, R2 = R2 - 4R3",
            "R2 = R2 / 2",
            "R1 = R1 + R2, Inversa de A obtenida"
        ]

        # Crear y posicionar las matrices.
        matrices = []  # Almacena los objetos Matrix para animarlos más tarde.
        for i, data in enumerate(matrices_data):
            # Crear matriz para el paso actual.
            matrix = Matrix(data).scale(0.5)
            # Ajustar el tamaño del texto de las etiquetas.
            title = Text(titles[i], font_size=20).scale(0.5)

            if i < 3:  # Posicionar las primeras tres matrices a la izquierda.
                if i == 0:
                    matrix.to_edge(LEFT).to_edge(UP)
                else:
                    matrix.next_to(matrices[-1], DOWN, buff=0.5)
            else:  # Posicionar las restantes matrices a la derecha.
                if i == 3:
                    matrix.to_edge(RIGHT).to_edge(UP)
                else:
                    matrix.next_to(matrices[-1], DOWN, buff=0.5)

            title.next_to(matrix, UP)
            matrices.append(matrix)

            # Animar la creación de la matriz y su título.
            self.play(Write(title), Write(matrix))
            self.wait(1)

        # Ajuste final para mostrar la inversa en la parte inferior derecha.
        inverse_matrix = matrices[-1]
        inverse_title = Text("Inversa de A", font_size=20).scale(0.5).next_to(inverse_matrix,16* DOWN)
        self.play(inverse_matrix.animate.move_to(DOWN * 3), Write(inverse_title))
        self.wait(4)

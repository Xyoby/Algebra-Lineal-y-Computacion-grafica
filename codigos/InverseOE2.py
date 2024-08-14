from manim import *
from fractions import Fraction

class ExtendedGaussJordanInversion(Scene):
    def construct(self):
        # Define las operaciones elementales en una lista.
        operations = [
            "Matriz Aumentada Inicial",
            "R3 = R3 / (-5)",
            "R1 = R1 - 3R3",
            "R2 = R2 - 4R3",
            "R2 = R2 / 2",
            "R1 = R1 + R2",
            "R1 = R1 + R3",
            "R2 = R2 - 2R3"
        ]

        # Crea la matriz aumentada inicial [A|I].
        initial_data = [
            [1, -1, 3, 1, 0, 0],
            [0, 2, 4, 0, 1, 0],
            [0, 0, -5, 0, 0, 1]
        ]

        # Aplica cada operación elemental y actualiza la matriz.
        current_data = [[float_to_fraction(val) for val in row] for row in initial_data]

        matrices = [Matrix(current_data).scale(0.5)]
        labels = [Text(operations[0], font_size=20).scale(0.5).next_to(matrices[0], UP)]

        self.play(FadeIn(labels[0]), FadeIn(matrices[0]))
        self.wait(1)

        # Función para aplicar operaciones elementales y actualizar la matriz.
        def apply_operation(operation_index):
            nonlocal current_data
            # Aplica las operaciones elementales basadas en el índice.
            if operation_index == 1:  # R3 = R3 / (-5)
                current_data[2] = [val / -5 if i < 3 else val for i, val in enumerate(current_data[2])]
            elif operation_index == 2:  # R1 = R1 - 3R3
                current_data[0] = [current_data[0][i] - 3 * current_data[2][i] for i in range(6)]
            elif operation_index == 3:  # R2 = R2 - 4R3
                current_data[1] = [current_data[1][i] - 4 * current_data[2][i] for i in range(6)]
            elif operation_index == 4:  # R2 = R2 / 2
                current_data[1] = [val / 2 if i < 3 else val for i, val in enumerate(current_data[1])]
            elif operation_index == 5:  # R1 = R1 + R2
                current_data[0] = [current_data[0][i] + current_data[1][i] for i in range(6)]
            elif operation_index == 6:  # R1 = R1 + R3
                current_data[0] = [current_data[0][i] + current_data[2][i] for i in range(6)]
            elif operation_index == 7:  # R2 = R2 - 2R3
                current_data[1] = [current_data[1][i] - 2 * current_data[2][i] for i in range(6)]
            # Crea la nueva matriz y etiqueta.
            new_matrix = Matrix([[float_to_fraction(val) for val in row] for row in current_data]).scale(0.5)
            new_label = Text(operations[operation_index], font_size=20).scale(0.5).next_to(new_matrix, UP)
            matrices.append(new_matrix)
            labels.append(new_label)

        # Ejecuta cada operación elemental y muestra la matriz resultante.
        for i in range(1, len(operations)):
            apply_operation(i)
            if i < 4:
                matrices[i].next_to(matrices[i - 1], DOWN, buff=0.5)  # Las primeras 4 matrices a la izquierda
            else:
                if i == 4:
                    matrices[i].to_edge(RIGHT).to_edge(UP)
                else:
                    matrices[i].next_to(matrices[i - 1], DOWN, buff=0.5)  # Resto de matrices a la derecha

            self.play(FadeIn(labels[i]), FadeIn(matrices[i]))
            self.wait(1)

def float_to_fraction(value):
    """Convierte un valor flotante a una representación de fracción como cadena."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    fraction = Fraction(value).limit_denominator()
    return f"{fraction.numerator}/{fraction.denominator}" if fraction.denominator != 1 else str(fraction.numerator)

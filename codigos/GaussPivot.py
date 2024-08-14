from manim import *
import numpy as np

class SolucionSistema(Scene):
    def construct(self):

        # Agregar título y autor
        title = Text("Solución de un SEL", font_size=20).to_edge(LEFT+UP, buff=1)
        author = Text("X Chávez", font_size=10).next_to(title, DOWN)

        # Cargar imagen
        image = ImageMobject("logo.png")
        image.scale(0.05).next_to(author, DOWN)
        self.add(title, author, image)
        self.play(FadeIn(image))

        # Matriz de coeficientes y términos independientes
        matrix_data = np.array([[2, 1, -1, 8], [-3, -1, 2, -11], [-2, 1, 2, -3]])
        matrix = Matrix(matrix_data)
        matrixA = matrix.get_entries()[:9]
        matrixB = matrix.get_entries()[9:]

        # Crear matrices
        self.play(Write(matrixA))
        self.wait(1)
        self.play(matrixA.animate.scale(0.8).move_to(2*UP))
        self.wait(1)

        # Escoger pivote y eliminar en columnas
        pivote = 0
        eliminaciones = VGroup()
        for i in range(3):
            coef_pivote = matrixA[pivote*3 + i]
            if coef_pivote != 0:
                eliminaciones.add(coef_pivote)
                coef_pivote.set_color(GREEN)
                self.play(coef_pivote.animate.scale(1.2))
                self.wait(1)
                for j in range(i+1, 3):
                    coef_a_eliminar = matrixA[(pivote+j)*3 + i]
                    eliminaciones.add(coef_a_eliminar)
                    coef_a_eliminar.set_color(RED)
                    self.play(Transform(coef_a_eliminar, coef_a_eliminar.copy().scale(1.2)))
                    self.wait(1)
                    coef_nuevo = MathTex("{-", str(coef_a_eliminar), "\over", str(coef_pivote), "}").set_color(YELLOW)
                    coef_nuevo.scale(1.2)
                    coef_nuevo.move_to(coef_a_eliminar)
                    self.play(Transform(coef_a_eliminar, coef_nuevo))
                    self.wait(1)
                self.wait(1)
                pivote += 1

        # Mostrar matriz escalonada
        matrix_escalonada = np.array([[1, 0, -3, 2], [0, 1, -2, 3], [0, 0, 0, 0]])
        matrix_esc = Matrix(matrix_escalonada)
        matrixB_esc = matrixB[:2]
        matrixA_esc = matrixA[:6]
        self.play(Transform(matrixA, matrixA_esc), Transform(matrixB, matrixB_esc))
        self.play(matrixA.animate.move_to(2*UP).scale(0.8))
        self.wait(1)
        self.play(Transform(matrixA, matrix_esc), matrixB.animate.move_to(2*UP).scale(0.8))
        self.wait(1)

        # Solución
        solucion = np.array([[2], [3], [0]])
        sol_matrix = Matrix(solucion)
        self.play(matrixB.animate.move_to(2*DOWN))
        self.wait(1)
        self.play(Write(sol_matrix))
        self.wait(1)

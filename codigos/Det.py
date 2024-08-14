from manim import *
import numpy as np

class DeterminantOfAMatrix(Scene):
    def construct(self):
        # Agregar título y logro
        title = Text("ALGEBRA LINEAL 2023 2", font_size=30).move_to(ORIGIN)
        title.set_color(GREEN)  # Cambiar el color del texto si lo deseas

        # Mostrar el título en la pantalla
        self.play(Write(title))

        # Esperar un tiempo
        self.wait(2)

        # Desaparecer el título
        self.play(FadeOut(title))

        # Agregar título y logro
        title = Text(" Determinante", font_size=20).to_edge(LEFT+UP, buff=1)
        author = Text(" X Chávez", font_size=10).next_to(title, DOWN)

        # Cargar imagen
        image = ImageMobject("logo.png")
        image.scale(0.05).next_to(author, DOWN)
        self.add(title, author, image)
        self.play(FadeIn(image))


        matrix_data = np.array([[4, -1, 1], [4, 5, 3], [2, 0, 0]])
        matrix = Matrix(matrix_data)
        stuff = VGroup(matrix)
        matrixA = stuff[0]

        self.play(Write(matrixA))
        self.play(matrixA.animate.scale(1).move_to(2*UP ))

        # Calculate the determinant of A
        det  = round(np.linalg.det(matrix_data),2)

        # scaling down the `det` string
        det = get_det_text(matrix,
                    determinant=None,
                    initial_scale_factor=1)

        # must add the matrix
        self.add(det)


        row_to_del = 1
        Col_colors = [RED, BLUE, YELLOW]
#        Col_colors = [RED ]

        expression = MathTex("=")
        expression.move_to(6*LEFT+DOWN)
        sumandos = VGroup(expression)
        self.play(expression.animate.scale(1), runtime=1)

        A_rows1 = matrixA.get_entries()[1:3]
        A_rows2 = matrixA.get_entries()[7:9]

        M1 = VGroup(A_rows1, A_rows2)

        A_rows1 = matrixA.get_entries()[0]
        A_rows2 = matrixA.get_entries()[2]
        A_rows3 = matrixA.get_entries()[6]
        A_rows4 = matrixA.get_entries()[8]
        M2 = VGroup(A_rows1, A_rows2,A_rows3,A_rows4)

        A_rows1 = matrixA.get_entries()[0:2]
        A_rows2 = matrixA.get_entries()[6:8]
        M3 = VGroup(A_rows1, A_rows2)

        gr= VGroup(*M1[0],*M2[0],*M3[0])
        elAm = matrixA.get_entries()[3:6]
        elAm1 = VGroup(*elAm)
        elemAmin = elAm.copy()

        bOpen1 = Tex(r"\big|", color=WHITE, font_size=100)
        punt = MathTex(".")
        bOpen2 = Tex(r"\big|", color=WHITE, font_size=100)
        rscal = 0.6
        for  col_to_del, color in enumerate(Col_colors):
            bOpen1 = Tex(r"\big|", color=WHITE, font_size=100)
            punt = Tex(".")
            bOpen2 = Tex(r"\big|", color=WHITE, font_size=100)

            matrixA.set_color(WHITE)

            fb2 = SurroundingRectangle(matrixA.get_rows()[row_to_del], buff=.1, color=color)
            self.play(Create(fb2))
            self.wait(1)

            row = matrixA.get_mob_matrix()[row_to_del]
            # Animar cada elemento de la fila individualmente
            for element in row.copy():
                self.play(element.animate.set_color(color), run_time=0.01)

            fb1 = SurroundingRectangle(matrixA.get_columns()[col_to_del], buff=.1, color=color)
            self.play(Create(fb1))
            self.wait(1)

            # Animar la columna a eliminar en amarillo
            column = [matrix.get_mob_matrix()[row][col_to_del] for row in range(len(matrix.get_mob_matrix()))]
            for element in column.copy():
                self.play(element.animate.set_color(color), run_time=0.01)

            # Creación de la submatriz y calculo del  cofactor
            minor_data = np.delete(np.delete(matrix_data, row_to_del, axis=0), col_to_del, axis=1)
            minor=Matrix(minor_data)
            minor_det = np.linalg.det(minor_data)
            cofactor = (-1) ** (row_to_del + col_to_del) * minor_det
            cof = get_det_text(minor,
                               determinant=cofactor,
                               initial_scale_factor=1)
            
            # Mostrar la matriz resultante
            elemAmin[col_to_del].scale(rscal).next_to(sumandos, RIGHT)
            expression = MathTex( ".","(-1)^{", str(row_to_del+1), "+", str(col_to_del+1), "}")
            expression.scale(rscal).next_to(elemAmin[col_to_del], RIGHT)
            punt.scale(rscal).next_to(expression,RIGHT)
            bOpen1.scale(rscal).next_to(punt,RIGHT)
            minor.scale(rscal).next_to(bOpen1,RIGHT, buff=-0.1)
            bOpen2.scale(rscal).next_to(minor, RIGHT, buff=-0.1)
            sumandos.add(elemAmin[col_to_del])
            sumandos.add(expression)
            sumandos.add(bOpen1)
            sumandos.add(punt)
            sumandos.add(minor)
            sumandos.add(bOpen2)
            # self.play(Create(expression))
            self.play(elAm1[col_to_del].set_color(WHITE).animate, runtime=0.1)
            self.play(elemAmin[col_to_del].animate, runtime=0.1)
            self.play(expression.animate,runtime=1)
            self.play(punt.animate, runtime=0.1)
            self.play(bOpen1.animate, runtime=0.01)
            self.play(Transform(gr[col_to_del].copy(),minor.get_entries()),runtime=0.1)
            self.play(bOpen2.animate, runtime=0.01)
            self.play(FadeOut(fb1), FadeOut(fb2))

            if col_to_del != 2:
                expression = MathTex(" + ")
                expression.scale(rscal).next_to(bOpen2, RIGHT)
                self.play(expression.animate, runtime=1)
                sumandos.add(expression)

            self.wait(1)

        expresion = [MathTex("= \, 4 "+"\\cdot"+"0 +"), MathTex("5 "+"\\cdot"+"(-2) +"),MathTex("3 "+"\\cdot"+"-2\,\,=- 16")]
        expresion[0].to_edge(DOWN)
        for i in range(1, len(expresion)):
            expresion[i].next_to(expresion[i - 1], RIGHT)

        for i in range(3):
            result =  sumandos[(1+ i*7)*1:(1+ i*7)*7].copy()
            self.play(Transform(result,expresion[i]))
            self.wait(1)

        self.wait(2)
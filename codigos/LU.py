from manim import *

class LUFactorization(Scene):
    def construct(self):
        # Agregar título y logro
        title = Text("ALGEBRA LINEAL ", font_size=30).move_to(ORIGIN)
        title.set_color(GREEN)  # Cambiar el color del texto si lo deseas

        # Mostrar el título en la pantalla
        self.play(Write(title))

        # Esperar un tiempo
        self.wait(2)

        # Desaparecer el título
        self.play(FadeOut(title))

        # Agregar título y logro
        title = Text(" Factorización LU", font_size=20).to_edge(LEFT + UP, buff=1)
        author = Text(" X Chávez", font_size=10).next_to(title, DOWN)

        # Cargar imagen
        image = ImageMobject("logo.png")
        image.scale(0.05).next_to(author, DOWN)
        self.add(title, author, image)
        self.play(FadeIn(image))

        self.wait(2)
        self.play(FadeOut(image, title, author))



        nomA= MathTex("A=").scale(0.4)
        nomA.move_to(UP*2.5 + LEFT*6.5)
        self.play(Create(nomA))
        # Matriz original 1
        matrix = Matrix([
            [1, 2, 3],
            [2, -4, 6],
            [3, -9, -3]
        ])

#         Matriz 2
#        matrix = Matrix([
#            [2, 6, 2],
#            [-3, -8, 0],
#            [4, 9, 2]
#        ])
        matrix.scale(0.6)
        matrix.next_to(nomA,RIGHT)

        self.play(Create(matrix))
        self.play(Create(matrix.copy()))
        self.wait(6)

        # Matrices semenjantes  elementales y sus inversas

        matrices = [
            (Matrix([
                [1, 2, 3],
                [0,-8, 0],
                [3, -9, -3]
            ]), Matrix([
                [1 , 0, 0],
                [-2, 1, 0],
                [0, 0, 1]
            ]), Matrix([
                [1, 0, 0],
                [2, 1, 0],
                [0, 0, 1]
            ])),
            (Matrix([
                [1, 2, 3],
                [0, -8, 0],
                [0, -15, -12]
            ]), Matrix([
                [1, 0, 0],
                [0, 1, 0],
                [-3, 0, 1]
            ]), Matrix([
                [1, 0, 0],
                [0, 1, 0],
                [3, 0, 1]
            ])),
            (Matrix([
                [1, 2, 3],
                [0, -8, 0],
                [0, 0 , -12]
            ]), Matrix([
                [1, 0, 0],
                [0, 1, 0],
                [0, "{-15 \over 8} ", 1]
            ]), Matrix([
                [1, 0, 0],
                [0, 1, 0],
                [0,"{ 15\over 8}", 1]
            ] ))
        ]

#        matrices = [
#            (Matrix([
#                [1, 3, 1],
#                [-3, -8, 0],
#                [4, 9, 2]
#            ]), Matrix([
#                [1 / 2, 0, 0],
#                [0, 1, 0],
#                [0, 0, 1]
#            ]), Matrix([
#                [2, 0, 0],
#                [0, 1, 0],
#                [0, 0, 1]
#            ])),
#            (Matrix([
#                [1, 3, 1],
#                [0, 1, 3],
#                [4, 9, 2]
#            ]), Matrix([
#                [1, 0, 0],
#               [3, 1, 0],
#                [0, 0, 1]
#            ]), Matrix([
#                [1, 0, 0],
#                [-3, 1, 0],
#                [0, 0, 1]
#            ])),
#            (Matrix([
#                [1, 3, 1],
#                [0, 1, 3],
#                [0, -3, -2]
#            ]), Matrix([
#                [1, 0, 0],
#                [0, 1, 0],
#                [-4, 0, 1]
#            ]), Matrix([
#                [1, 0, 0],
#                [0, 1, 0],
#                [4, 0, 1]
#            ])),
#            (Matrix([
#                [1, 3, 1],
#                [0, 1, 3],
#                [0, 0, 7]
#            ]), Matrix([
#                [1, 0, 0],
#                [0, 1, 0],
#                [0, 3, 1]
#            ]), Matrix([
#                [1, 0, 0],
#                [0, 1, 0],
#                [0, -3, 1]
#            ])),
#            (Matrix([
#                [1, 3, 1],
#                [0, 1, 3],
#                [0, 0, 1]
#            ]), Matrix([
#                [1, 0, 0],
#                [0, 1, 0],
#                [0, 0, "1 \over 7"]
#            ]), Matrix([
#                [1, 0, 0],
#                [0, 1, 0],
#                [0, 0, 7]
#            ]))
#        ]

#        Para reducir el tamaño de las fracciones
        ent = matrices[2][1].get_entries()
        ent[7].next_to(ent[4], 0.1 * DOWN).scale(0.7)

        ent = matrices[2][2].get_entries()
        ent[7].next_to(ent[4], 0.1 * DOWN).scale(0.7)


        TextIgual = MathTex("\sim").scale(0.6)
        TextIgual.next_to(matrix, RIGHT)
        self.play(Create(TextIgual))


        L = VGroup()

        # Reducción de la matriz a su forma escalonada
        for i, (semejante_matrix, elementary_matrix, inverse_matrix) in enumerate(matrices):
            object = VGroup(TextIgual.copy(), matrix.copy())
            self.play(Create(object))

            semejante_matrix.scale(0.6)
            semejante_matrix.next_to(TextIgual, RIGHT)
            TextIgual.next_to(semejante_matrix, RIGHT)

            self.play(Transform(matrix, semejante_matrix))

            self.wait()

            elementary_matrix.scale(0.5)
            elementary_matrix.next_to(matrix, DOWN, buff=0.4)
            arrow = Arrow(matrix.get_bottom(), elementary_matrix.get_top(), buff=0.1)
            # Agregar texto "E_i"
            texto_ei = MathTex("E_{" + str(i + 1)+"}=").scale(0.4)
            texto_ei.next_to(elementary_matrix, 0.8*LEFT)
            elmObj=VGroup(texto_ei,arrow,elementary_matrix)
            self.play(Create(elmObj))



            inverse_matrix.scale(0.5)
            inverse_matrix.next_to(elementary_matrix, DOWN, buff=0.4)
            # Agregar texto "E_i"
            texto_in = MathTex("E_{" + str(i + 1) + "}^{-1}=").scale(0.4)
            texto_in.next_to(inverse_matrix, LEFT)
            invmObj = VGroup(texto_in, inverse_matrix)
            self.play(Create(invmObj))

            L.add(inverse_matrix.copy())
            self.wait()


        # Agregar texto "L"
        LText = MathTex("L=E_1^{-1}\cdot E_2^{-1}\cdot E_3^{-1}=").scale(.6)
        LText.to_corner(DOWN + LEFT  - 1.5 * UP)
        L.next_to(LText,RIGHT)
        IText = MathTex("=").scale(1)
        IText.next_to(L,RIGHT)
        ResultObject= VGroup(LText, L, IText)
        self.play(Create(ResultObject))
        self.wait(4)

        IText = MathTex("L=E_1^{-1}\cdot E_2^{-1}\cdot E_3^{-1}=").scale(.6)
        IText.to_corner(DOWN + LEFT - 1.5*UP)
        Lmatrix = Matrix([[1, 0, 0], [2, 1, 0], [3, "15 \over 8", 1]]).scale(.6)
        Lmatrix.next_to(IText, RIGHT)

        ent = Lmatrix.get_entries()
        ent[7].next_to(ent[4], 0.1 * DOWN).scale(0.7)


        Lobject=VGroup(IText , Lmatrix)
        self.play(Transform(ResultObject,Lobject))

        self.wait(10)




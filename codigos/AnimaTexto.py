from manim import *
import random

class AlphabetCircle(Scene):
    def construct(self):
        # Crear círculo
        circle = Circle(radius=3, color=BLACK)

        # Lista de letras del abecedario
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        colors = color_gradient([BLUE, GREEN, YELLOW, RED], len(alphabet))
        letter_mobjects = [Text(letter, color=colors[i]) for i, letter in enumerate(alphabet)]

        # Posicionar las letras en el círculo
        for i, letter in enumerate(letter_mobjects):
            angle = i * TAU / 26  # Dividir el círculo en 26 partes
            letter.move_to(circle.point_at_angle(angle))

        # Animación de rotación
        self.play(Create(circle))
        for letter in letter_mobjects:
            self.play(Create(letter))
        self.wait(1)

        # Rotar las letras en un círculo
        rotating_group = VGroup(*letter_mobjects)
        self.play(Rotate(rotating_group, angle=TAU, about_point=ORIGIN, run_time=5))

        # Desvanecer círculo y letras
        self.play(FadeOut(circle), FadeOut(rotating_group))
        self.wait(1)


        # Intercambiar aleatoriamente el orden de las posiciones
        random.shuffle(letter_mobjects)

        # Posicionar las letras en el círculo
        for i, letter in enumerate(letter_mobjects):
            angle = i * TAU / 26  # Dividir el círculo en 26 partes
            letter.move_to(circle.point_at_angle(angle))


        self.play(*[TransformFromCopy( letter, rotating_group[i]) for i, letter in enumerate(letter_mobjects)])
        self.wait(10)


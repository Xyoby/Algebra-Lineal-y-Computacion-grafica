from manim import *
import random

class SyllableCircles(Scene):
    def construct(self):
        circles = VGroup()

        # Listas de consonantes y vocales
        consonants = "BCDFGHJKLMNPQRSTVWXYZ"
        vowels = "AEIOU"

        # Generar monosílabos de consonante + vocal
        syllables = [c + v for c in consonants for v in vowels]

        # Mezclar las sílabas de forma aleatoria
        random.shuffle(syllables)

        # Crear círculos y posicionar sílabas
        for i in range(5):
            circle = Circle(radius=1.5, color=BLACK)
            circles.add(circle)

            syllable_subset = syllables[i * len(syllables) // 5 : (i + 1) * len(syllables) // 5]

            syllable_mobjects = [Text(syllable, color=WHITE) for syllable in syllable_subset]
            for j, syllable in enumerate(syllable_mobjects):
                angle = j * TAU / len(syllable_subset)
                syllable.move_to(circle.point_at_angle(angle))

            self.play(Create(circle))
            for syllable in syllable_mobjects:
                self.play(Create(syllable))

        self.wait(1)

        # Rotar los círculos y sílabas
        for circle in circles:
            self.play(Rotate(circle, angle=TAU, about_point=ORIGIN, run_time=3))

        self.wait(1)

        # Desvanecer círculos y sílabas
        self.play(*[FadeOut(circle) for circle in circles])
        self.wait(1)

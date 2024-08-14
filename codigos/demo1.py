
from manim import *

class Determinante3(Scene):

    def construct(self):
        # Agregar título y logro
        title = Text(" Determinante", font_size=20).to_edge(LEFT, buff=1)
        author = Text(" X Chávez", font_size=10).next_to(title, DOWN)

        # Cargar imagen
        image = ImageMobject("logo.png")
        image.scale(0.05).next_to(author, DOWN)
        self.add(title, author, image)


        det = Tex(r'$\det \, $')
        m0 = Matrix([[1, 1, 0], [0, 1, 1], [1, 0, 2]])
        m0.scale(1.0)
        self.wait(1)
        det.next_to(m0, LEFT)
        self.play(Write(det))
        self.play(Write(m0, run_time=3))

        grupo = Group(det, m0)
        self.play(ApplyMethod(grupo.shift, 2.5 * UP))
        self.play(ApplyMethod(grupo.shift, 4.0 * LEFT))
        self.wait(1)

        fb1 = SurroundingRectangle(m0.get_columns()[0], buff=.1, color=RED)
        fb2 = SurroundingRectangle(m0.get_rows()[0], buff=.1, color=RED)
        self.wait(1)
        self.play(Create(fb1))
        self.wait(1)
        self.play(Create(fb2))
        self.wait(1)

        m0.get_entries()[0].set_color(RED)
        m0.get_entries()[4:6].set_color(RED)
        m0.get_entries()[7:9].set_color(RED)
        self.wait(1)

        ###################################################################################################################

        d11 = Tex(r'$\Delta_{11} = {\left( { - 1} \right)^{i + j}} \left( 1 \right)\left| {\begin{array}{*{20}{c}}1&1\\0&2\end{array}} \right|=2$', color=RED)
        # d11.next_to(m0, DOWN)
        d11.scale(1)
        self.play(Write(d11, run_time=5))
        self.wait(2)

        self.play(ApplyMethod(d11.shift, 2 * RIGHT))
        self.play(ApplyMethod(d11.shift, 3 * UP))
        self.wait(1)
        self.play(FadeOut(fb1), FadeOut(fb2))
        m0.get_entries()[:].set_color(WHITE)
        self.wait(1)

        ###################################################################
        fb1 = SurroundingRectangle(m0.get_columns()[0], buff=.1, color=GREEN)
        self.play(Create(fb1))
        self.wait(1)
        fb2 = SurroundingRectangle(m0.get_rows()[1], buff=.1, color=GREEN)
        self.play(Create(fb2))
        self.wait(1)

        m0.get_entries()[3].set_color(GREEN)
        m0.get_entries()[1:3].set_color(GREEN)
        m0.get_entries()[7:9].set_color(GREEN)
        self.wait(1)
        d21 = Tex(r'$\Delta_{21}={\left( { - 1} \right)^{i + j}} \left( 0 \right)\left| {\begin{array}{*{20}{c}}1&0\\0&2\end{array}} \right|=0$', color=GREEN)
        d21.scale(1)
        self.play(Write(d21, run_time=5))
        self.wait(2)
        self.play(ApplyMethod(d21.shift, 2 * RIGHT))
        self.play(ApplyMethod(d21.shift, 1 * UP))
        self.play(FadeOut(fb1), FadeOut(fb2))
        m0.get_entries()[:].set_color(WHITE)
        self.wait(1)

        ###################################################################

        ###################################################################
        fb1 = SurroundingRectangle(m0.get_columns()[0], buff=.1, color=BLUE)
        self.play(Create(fb1))
        self.wait(1)
        fb2 = SurroundingRectangle(m0.get_rows()[2], buff=.1, color=BLUE)
        self.play(Create(fb2))
        self.wait(2)

        m0.get_entries()[6].set_color(BLUE)
        #m0.get_entries()[6].set_weight(BOLD)
        m0.get_entries()[1:3].set_color(BLUE)
        #m0.get_entries()[1:3].set_weight(BOLD)
        m0.get_entries()[4:6].set_color(BLUE)
        #m0.get_entries()[4:6].set_weight(BOLD)
        self.wait(1)
        d31 = Tex(
            r'$\Delta_{31}={\left( { - 1} \right)^{i + j}} \left( 1 \right)\left| {\begin{array}{*{20}{c}}1&0\\1&1\end{array}} \right|=1$',
            color=BLUE)
        d31.scale(1)
        d31.shift(DOWN)
        self.play(Write(d31, run_time=5))
        self.wait(1)
        self.play(ApplyMethod(d31.shift, 2 * RIGHT))
        self.play(ApplyMethod(d31.shift, 0 * UP))
        self.play(FadeOut(fb1), FadeOut(fb2))
        m0.get_entries()[:].set_color(WHITE)
        self.wait(1)

        ###################################################################

        r1 = Tex(r'$\Delta  \,=\, $', r'$\,2\,+\,$', r'$\,0\,+\,$', r'$\,1\,=\,$', r'$\,3$')
        r1[1].color = RED
        r1[2].color = GREEN
        r1[3].color = BLUE

        r1.scale(1.5)
        r1.shift(3 * DOWN)
        r1.shift(2 * RIGHT)
        self.play(Write(r1), run_time=3)

        self.wait(1)
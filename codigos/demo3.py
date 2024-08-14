
from manim import *

class Test(Scene):
    def construct(self):
        m = Matrix(
            [["A", "B", "C"],
             ["A", "B", "D"],
             ["A", "B", "F"],
             ["A", "h", "F"]],
        )
        self.add(m.get_brackets())
        rows = m.get_cols()
        self.play(Write(rows[3]))
        prev_row = rows[0]
        for row in rows[1:]:
            self.wait()
            self.play(
                ReplacementTransform(prev_row.copy(), row),
            )
            prev_row = row

        self.wait()
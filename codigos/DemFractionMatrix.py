from manim import *

class GetEntriesExample(Scene):
    def construct(self):

        matrices = [
            (Matrix([
                [1, 2, 3],
                [0, -8, 0],
                [3, -9, -3]
            ]), Matrix([
                [1, 0, 0],
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
                [0, 0, -12]
            ]), Matrix([
                [1, 0, 0],
                [0, 1, 0],
                [0, "{-15 \over 8} ", 1]
            ]), Matrix([
                [1, 0, 0],
                [0, 1, 0],
                [0, "{ 15\over 8}", 1]
            ]))
        ]

        ent = matrices[2][1].get_entries()
        ent[7].next_to(ent[4], 0.1 * DOWN).scale(0.7)
        self.play(Create(matrices[2][1]))


        ent =  matrices[2][2].get_entries()
        ent[7].next_to(ent[4], 0.1 * DOWN).scale(0.7)
        self.play(Create(matrices[2][2]))

from manim import *
import numpy as np

class MatOpe(Scene):
   def construct(self):
      n = 3
      matrix = Matrix([[2, 1, 1], [1, 2, 1], [3, 2, 3]])
      matrixx = [[2, 1, 1], [1, 2, 1], [3, 2, 3]]

      identity = Matrix(np.identity(n))
      identity.next_to(matrix, RIGHT)
      MAu = np.hstack((matrixx, np.identity(3)))
      self.add( Matrix(MAu))
      self.wait()

      for col in range(n):
        pivot_row = None
        for row in range(col, n):
           if MAu[row, col] != 0:
             pivot_row = row
             break

           if pivot_row is None:
              continue
           MAu[[col, pivot_row]] = MAu[[pivot_row, col]]
           pivot_element = MAu[col, col]
           self.play(matrix.animate.set(np.array(MAu[:, :n])), run_time=0.5)
           self.play(identity.animate.set(np.array(MAu[:, n:])), run_time=0.5)

           MAu[col] /= pivot_element
           self.play(Create(MAu))
           self.wait()

           for row in range(n):
               if row == col:
                   continue
               multiplier = MAu[row, col]
               MAu[row] -= multiplier * MAu[col]
               self.play(matrix.animate.set(np.array(MAu[:, :n])), run_time=0.5)
               self.play(identity.animate.set(np.array(MAu[:, n:])), run_time=0.5)

           self.wait()
from manim import *

class DeleteRowExample(Scene):
    def construct(self):
        matrix_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matrix = Matrix(matrix_data)
        matrix.to_edge(UP)  # Mover la matriz a la parte superior de la pantalla
        self.play(Create(matrix))
        #self.add(matrix)

        row_to_delete = 1
        column_to_delete = 0
        row = matrix.get_mob_matrix()[row_to_delete]
        # Animar cada elemento de la fila individualmente
        for element in row:
            self.play(element.animate.set_color(YELLOW), run_time=0.1)
        self.wait(1)



        # Animar la columna a eliminar en amarillo
        column = [matrix.get_mob_matrix()[row][column_to_delete] for row in range(len(matrix.get_mob_matrix()))]
        for element in column:
            self.play(element.animate.set_color(YELLOW),run_time=0.1 )
        self.wait(1)

        # Crear la matriz resultante después de eliminar fila y columna
        minor_data = np.delete(np.delete(matrix_data, row_to_delete, axis=0), column_to_delete, axis=1)
        minor_det =  np.linalg.det(minor_data)
        minor = Matrix(minor_data)
        cofactor = (-1) ** (row_to_delete + column_to_delete) * minor_det

        matrices_group = VGroup(matrix, minor)
        matrices_group.arrange(DOWN, buff=0.5)  # Alinea las matrices verticalmente
        matrices_group.to_edge(UP)  # Mueve el grupo de matrices a la parte superior de la pantalla

        cof = get_det_text(minor,
                           determinant=cofactor,
                           initial_scale_factor=1)
        # Mostrar la matriz resultante
        self.play(Create(matrix))
        self.play(Transform(matrix, matrices_group))
        self.wait(1)
        self.play(Transform(minor, cof))
        self.wait(1)



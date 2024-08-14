from manim import *

class SVDAnimation(Scene):
    def construct(self):
        # Generamos una matriz de puntos aleatorios en el espacio tridimensional
        point_cloud_matrix = np.random.rand(10, 3) * 2 - 1  # 10 puntos en 3D

        # Mostramos la nube de puntos original
        original_points = VGroup(*[Dot(point) for point in point_cloud_matrix])
        self.play(Create(original_points))
        self.wait()

        # Calculamos la SVD
        U, sigma, VT = np.linalg.svd(point_cloud_matrix, full_matrices=False)

        # Creamos matrices para U, sigma y VT
        U_matrix = Matrix(U, v_buff=0.5)
        sigma_matrix = Matrix(np.diag(sigma), v_buff=0.5)
        VT_matrix = Matrix(VT, v_buff=0.5)

        # Posicionamos las matrices
        U_matrix.next_to(original_points, DOWN)
        sigma_matrix.next_to(U_matrix, DOWN)
        VT_matrix.next_to(sigma_matrix, DOWN)

        # Mostramos las matrices
        self.play(Create(U_matrix))
        self.wait()
        self.play(Create(sigma_matrix))
        self.wait()
        self.play(Create(VT_matrix))
        self.wait()

        # Transformamos la nube de puntos usando U, sigma y VT
        transformed_points = VGroup(*[Dot(point) for point in U @ np.diag(sigma) @ VT])
        transformed_points.next_to(VT_matrix, DOWN)

        # Mostramos la nube de puntos transformada
        self.play(Transform(original_points, transformed_points))
        self.wait()

        # Agregamos etiquetas
        labels = VGroup(
            Text("Nube de Puntos Original").next_to(original_points, UP),
            Text("U").next_to(U_matrix, UP),
            Text("Σ").next_to(sigma_matrix, UP),
            Text("V^T").next_to(VT_matrix, UP),
            Text("Nube de Puntos Transformada").next_to(transformed_points, UP),
        )

        self.play(Create(labels))
        self.wait()

        # Resaltamos el mayor valor singular
        largest_singular_value = Text("Mayor Valor Singular", color=RED).next_to(sigma_matrix, RIGHT)
        self.play(Create(largest_singular_value))
        self.wait()

        # Desvanecemos todo
        self.play(FadeOut(original_points), FadeOut(labels), FadeOut(largest_singular_value))
        self.wait()

if __name__ == "__main__":
    config.pixel_height = 800
    config.pixel_width = 1200
    config.frame_height = 7.0
    config.frame_width = 10.0
    config.frame_y_radius = config.frame_height / 2
    config.frame_x_radius = config.frame_width / 2
    config.frame_center = np.array([0, 0, 0])
    config.background_color = "#FFFFFF"
    config.renderer = "cairo"
    config.quality = "high"
    config.skip_animations = False
    config.disable_caching = True
    config.write_to_movie = True
    config.save_last_frame = True
    config.output_file = "svd_animation"
    config.output_format = ".mp4"
    config.ffmpeg_loglevel = "error"
    config.verbosity = "ERROR"
    config.disable_caching = True
    config.disable_caching_animation = True
    config.disable_caching_notification = True
    config.disable_caching_output = True
    config.disable_caching_tex = True
    config.tex_template = TexTemplateLibrary.simple
    config.tex_compiler = "pdflatex"

    # Ejecutamos la animación
    SVDAnimation().render()

from manim import *

class ProductoEscalarScene(ThreeDScene):
    def construct(self):
        # Vectores en 2D
        u_2d = Vector([3, 2], color=BLUE)
        v_2d = Vector([1, 4], color=GREEN)

        # Suma de productos de componentes
        suma_productos = u_2d.copy().shift(v_2d.get_end())
        suma_productos.set_color(ORANGE)

        # Propiedad del producto escalar
        producto_escalar = u_2d.get_scalar_projection(v_2d)
        angulo = u_2d.get_angle(v_2d)
        propiedad_text = MathTex(
            "\\mathbf{u} \\cdot \\mathbf{v} =",
            "\\|\\mathbf{u}\\| \\|\\mathbf{v}\\| \\cos(\\theta)"
        ).scale(0.8).next_to(suma_productos, DOWN)

        # Muestra los vectores y la propiedad
        self.play(Create(u_2d), Create(v_2d))
        self.wait()
        self.play(Transform(u_2d, suma_productos))
        self.wait()
        self.play(Write(propiedad_text))
        self.wait()

        # Transición a 3D
        self.play(FadeOut(propiedad_text))
        self.play(Transform(u_2d, Vector([3, 2, 0], color=BLUE)))
        self.play(Transform(v_2d, Vector([1, 4, 2], color=GREEN)))
        self.wait()

        # Producto escalar en 3D
        producto_escalar_3d = u_2d.get_scalar_projection(v_2d)
        self.play(Transform(u_2d, producto_escalar_3d))
        self.wait()

        # Mostrar ángulo
        angulo_text = MathTex("\\theta").next_to(angulo, RIGHT)
        self.play(Create(angulo), Write(angulo_text))
        self.wait()

        # Finalización
        self.play(FadeOut(u_2d), FadeOut(v_2d), FadeOut(angulo), FadeOut(angulo_text))
        self.wait()

# Crear la escena
scene = ProductoEscalarScene()
scene.render()

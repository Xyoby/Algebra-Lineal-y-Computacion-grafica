from manim import *
import numpy as np

class SurfaceRotation(ThreeDScene):
    def construct(self):
        # Define la función
        def func(x, y):
            return 4*x*y - x**2 - y**2 - 14*x + 4*y + 10

        # Crea la superficie
        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                func(u, v)  # Aplica la función a las coordenadas u, v
            ]),
            u_range=[-10, 10],
            v_range=[-10, 10],
            resolution=(50, 50)
        ).set_style(fill_opacity=0.75, stroke_color=BLUE)

        # Ajusta la cámara y la iluminación
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)  # Inicia la rotación de la cámara

        # Añade la superficie a la escena
        self.add(surface)

        # Rota la superficie
        self.play(Rotate(surface, angle=260 * DEGREES, axis=UP), run_time=5)

        # Detiene la rotación de la cámara
        self.stop_ambient_camera_rotation()

        # Muestra la animación
        self.wait()

# Configura la calidad de la renderización
config.pixel_height = 720
config.pixel_width = 1280
config.frame_rate = 30

# Guarda la animación como un archivo de video
scene = SurfaceRotation()
scene.render()

Polígono(
    (
        ( r_1(a1 + (a2 - a1) / 2) +  (Nr/2)*( r_2(a1 + (a2 - a1) / 2) -r_1(a1 + (a2 - a1) / 2))/Nr) *
        cos(a1 + (a2 - a1) / 2),
        ( r_1(a1 + (a2 - a1) / 2) +  (Nr/2)*( r_2(a1 + (a2 - a1) / 2) -r_1(a1 + (a2 - a1) / 2))/Nr) *
        sen(a1 + (a2 - a1) / 2)
    ),
    (
        (r_1(a1 + (a2 - a1) / 2) + (Nr / 2 + 3) *
         (r_2(a1 + (a2 - a1) / 2)) - r_1(a1 + (a2 - a1) / 2)) / Nr *
        cos(a1 + (a2 - a1) / 2),
        (r_1(a1 + (a2 - a1) / 2) + (Nr / 2 + 3) *
         (r_2(a1 + (a2 - a1) / 2)) - r_1(a1 + (a2 - a1) / 2)) / Nr *
        sen(a1 + (a2 - a1) / 2)
    ),


    (
        (r_1(a1 + (Na/2+1)(a2 - a1) / Na) + (Nr / 2 + 1) *
         (r_2(a1 + (Na/2+1)(a2 - a1) / Na)
        - r_1(a1 + (Na/2+1)(a2 - a1) / Na)) / Nr) *
        cos(a1 + (Na/2+1)(a2 - a1) / Na),
        (r_1(a1 + (Na/2+1)(a2 - a1) / Na) + (Nr / 2 + 1) *
         (r_2(a1 + (Na/2+1)(a2 - a1) / Na)
        - r_1(a1 + (Na/2+1)(a2 - a1) / Na) )/ Nr) *
        sen(a1 + (Na/2+1)(a2 - a1) / Na)
    ),
    (
        (r_1(a1 + (Na/2+1)(a2 - a1) / Na) + (Nr / 2 ) *
         (r_2(a1 + (Na/2+1)(a2 - a1) / Na)
        - r_1(a1 + (Na/2+1)(a2 - a1) / Na)) / Nr )*
        cos(a1 + (Na/2+1)(a2 - a1) / Na),
        (r_1(a1 + (Na/2+1)(a2 - a1) / Na) + (Nr / 2 ) *
         (r_2(a1 + (Na/2+1)(a2 - a1) / Na)
        - r_1(a1 + (Na/2+1)(a2 - a1) / Na)) / Nr) *
        sen(a1 + (Na/2+1)(a2 - a1) / Na)
    )
         )
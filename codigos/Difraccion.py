from manim import *
import numpy as np


class LightDiffraction(ThreeDScene):
    def construct(self):
        # Configurar el entorno 3D
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Crear la fuente de luz
        light_source = np.array([-3, -3, 3])  # Posición de la fuente de luz
        light_end = np.array([0, 0, 1])  # Punto central de impacto en la esfera

        # Definir los colores para la difracción
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

        # Crear la esfera de cristal
        sphere = Sphere(radius=1, color=BLUE, fill_opacity=0.2)
        sphere.shift(light_end)
        self.add(sphere)

        # Generar rayos de luz desde la fuente hacia la esfera
        rays = VGroup()
        for color in colors:
            ray = Line(start=light_source, end=light_end, color=WHITE, stroke_width=2)
            rays.add(ray)
        self.play(Create(rays))  # Animación de la creación de rayos

        # Implementar la difracción de los rayos en la esfera
        refracted_rays = VGroup()
        angles = np.linspace(-PI / 4, PI / 4, num=len(colors))
        for ray, angle, color in zip(rays, angles, colors):
            refracted_ray = Line(
                start=light_end,
                end=light_end + rotate_vector(light_end - light_source, angle, axis=[1, 0, 0]),
                color=color,
                stroke_width=2,
            )
            refracted_rays.add(refracted_ray)

        self.play(Transform(rays, refracted_rays))  # Animación de la difracción
        self.begin_ambient_camera_rotation(rate=0.1)  # Rotación lenta de la cámara
        self.wait(5)

        # Animar la salida de la luz difractada
        for ray in refracted_rays:
            self.play(ray.animate.shift(ray.get_vector() * 2))

        self.wait(2)
        self.stop_ambient_camera_rotation()


def rotate_vector(vec, angle, axis):
    """Rotar un vector alrededor de un eje dado por un ángulo específico."""
    rotation_matrix = rotation_matrix_transpose(angle, axis)
    return np.dot(rotation_matrix, vec)


def rotation_matrix_transpose(angle, axis):
    """Crear una matriz de rotación para girar vectores en 3D."""
    return np.array(
        [
            [
                np.cos(angle) + axis[0] ** 2 * (1 - np.cos(angle)),
                axis[0] * axis[1] * (1 - np.cos(angle)) - axis[2] * np.sin(angle),
                axis[0] * axis[2] * (1 - np.cos(angle)) + axis[1] * np.sin(angle),
            ],
            [
                axis[1] * axis[0] * (1 - np.cos(angle)) + axis[2] * np.sin(angle),
                np.cos(angle) + axis[1] ** 2 * (1 - np.cos(angle)),
                axis[1] * axis[2] * (1 - np.cos(angle)) - axis[0] * np.sin(angle),
            ],
            [
                axis[2] * axis[0] * (1 - np.cos(angle)) - axis[1] * np.sin(angle),
                axis[2] * axis[1] * (1 - np.cos(angle)) + axis[0] * np.sin(angle),
                np.cos(angle) + axis[2] ** 2 * (1 - np.cos(angle)),
            ],
        ]
    )


if __name__ == "__main__":
    scene = LightDiffraction()
    scene.render()


## Pasos para instalar Manim usando PyCharm y MiKTeX:

### 1. Instalación de Python y PyCharm:

- **Instalar Python:** Descarga e instala la última versión de Python desde https://www.python.org/downloads/. Asegúrate de seleccionar la opción "Add Python to PATH" durante la instalación.
- **Instalar PyCharm:** Descarga e instala la versión gratuita de PyCharm Community Edition desde https://www.jetbrains.com/pycharm/download/. 

### 2. Instalación de MiKTeX:

- **Instalar MiKTeX:** Descarga e instala MiKTeX desde https://miktex.org/download. Sigue las instrucciones de instalación, que suelen ser sencillas.
- **Actualizar el paquete de instalación:** MiKTeX necesita actualizaciones periódicas. Después de la instalación, ejecútalo para actualizar los paquetes necesarios.

### 3. Instalación de Manim:

- **Instalar Manim en PyCharm:**
  - Abre PyCharm.
  - Crea un nuevo proyecto o abre uno existente.
  - Ve a **File > Settings > Project: [nombre del proyecto] > Python Interpreter**.
  - Haz clic en el botón "+" para agregar un nuevo paquete.
  - Busca "manim" en la barra de búsqueda.
  - Selecciona "manim" y haz clic en "Install Package".
  - Espera a que se complete la instalación.
 
  - Puedes ver este video de referencia: 

### 4. Configurar MiKTeX en Manim:

- **Configura la ruta de MiKTeX:**
  - Abre el archivo **config.py** dentro del directorio del proyecto en Pycharm.
  - Busca la línea `TEX_DIRECTORY = ''` y reemplaza el valor vacío con la ruta de instalación de MiKTeX. Por ejemplo, si lo instalaste en la carpeta "C:/Program Files/MiKTeX 2.9", la ruta sería: `TEX_DIRECTORY = 'C:/Program Files/MiKTeX 2.9/miktex/bin/x64'`.
- **Instala paquetes adicionales de LaTeX (opcional):**
  - Si necesitas usar paquetes de LaTeX específicos en tus animaciones, puedes instalarlos utilizando el administrador de paquetes de MiKTeX.
  - Busca en la terminal de tu sistema o en el menú de inicio de Windows por "MiKTeX Package Manager". 
  - Busca y selecciona los paquetes necesarios.
  - Sigue las instrucciones para instalarlos.

### 5. Probar Manim:

- **Crear un nuevo archivo Python:**
  - Crea un nuevo archivo Python en tu proyecto.
  - Copia el siguiente código en el archivo:

    ```python
    from manim import *

    class Intro(Scene):
        def construct(self):
            text = Text("¡Hola, Manim!")
            self.play(Write(text))
            self.wait(2)

    if __name__ == "__main__":
        render(Intro, preview=True)
    ```

- **Ejecutar el código:**
  - Haz clic derecho en el archivo Python y selecciona "Run 'nombre del archivo'".
  - Espera a que se complete la compilación.
  - Se abrirá una ventana con la animación.

### Consejos adicionales:

- **Comprueba la ruta de MiKTeX en la configuración:** Si la animación no funciona, asegúrate de que la ruta de MiKTeX en el archivo **config.py** sea correcta.
- **Instala paquetes de LaTeX adicionales:** Si necesitas usar paquetes de LaTeX específicos, instálalos utilizando el administrador de paquetes de MiKTeX.
-  **Instala FFMPEG:** Algunas veces puede que este programa no se instale correctamente. Te sufgiero que lo instales manualmente   https://www.youtube.com/watch?v=0zN9oZ98ZgE .
- **Busca ayuda:** Si tienes problemas al instalar MiKTeX o Manim, puedes buscar ayuda en la documentación de Manim https://docs.manim.community/en/stable/ o en foros y grupos de ayuda de Manim.

¡Espero que esta guía te ayude a instalar Manim en PyCharm y empezar a crear tus propias animaciones matemáticas!

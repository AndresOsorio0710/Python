# SortFiles
Este es un _scrypt_ hecho en _Python_ que nos permite organizar los archivos en nuestros directorios.

## ¿Pero qué hace?

Recorre todos los directorios del directorio don se está ejecutando y toma cada archivo en estos directorios reubicándolos en un nuevo directorio llamado _Organized_, este contiene otros directorios que corresponde al tipo de archivo encontrado.



_Organized_ tiene la siguiente estructura:

~~~

Organiszed:

    |_ AUDIO

        |_['.WAV', '.AIFF', '.AU', '.FLAC', '.MPEG-4', '.TTA', '.ATRAC','.MP3', '.VORBIS', '.AAC', '.WMA', '.OGG', '.DSD', '.MQA']

    |_ DOCUMENTS

        |_['.DOC', '.DOCX', '.DOT', '.XLS', '.XLSX', '.XLSM', '.XLT', '.PPT', '.PPTX', '.PPS', '.POT']

    |_ IMG

        |_['.BMP', '.RAW', '.RAW', '.TIF', '.PNG', '.JPG', '.JPEG', '.GIF','.TIFF', '.PSD', '.EPS', '.PIC', '.SVG', '.AI', '.DWG', ]

    |_ OTHES

        |_ "Extensiones diferentes"

    |_ TXT

        |_ .TXT

    |_ VIDEO

        |_['.MP4', '.AVI', '.MKV', '.FLV', '.MOV', '.WMV', '.DIVX', '.H.264', '.XVID', '.RM']

~~~



## ¿Como usarlo?

- ### Requerimientos:

    1. Tener Python 3.x instalado

- ### Pasos

    1. Copiamos el proyecto en el directorio que deseamos organizar, si en este directorio solo hay archivos, copiamos el proyecto en el directorio exterior a este

    2. Ejecutamos el archivo _sort_files.py_



        ### ¡¿Pero cómo?!



        Abrimos una terminar en el directorio donde se encuentra este archivo y copiamos la siguiente línea, presionamos _Enter_.



        ~~~
        python sort_files.py
        ~~~ 

    3. Esperamos que el programa haga lo suyo y revisamos el nuevo directorio resultante _Organized_

## ¿Cómo se me ocurrió esto?
Hace mucho tiempo venía usando una unidad de estado sólido para guardar ahí información como documentos de mis estudios, imágenes, proyectos de programación, etc. muchos de estos documentos no estaban cargados en la nube, y desafortunadamente conecte esta unidad a un _Mac_, el resultado de esto, una unidad ilegible, trate de repararla, pero me fue imposible.



Buscando en internet encontré algunas soluciones gratuitas que me permitían recuperar los archivos de esta unidad, no solo lo que estaban antes de dañarse sino archivos eliminados antes del daño, pero esta herramientas no recuperan los archivos de forma ordenada.



Afortunadamente los proyectos de programación más importante y que uso muy seguido se encuentran respaldados aquí en _GitHub_, pero mucha información como fotos familiares, y documentos muy importantes se encontraban por ahí en alguna de las carpetas que me recupero la herramienta.



Después de recorrer al rededor de 100 directorios en los que la mayoría de los archivos eran archivos de programas o sistemas operativos instalados anteriormente en esa unidad, preferí hacer un programa que me organizara los archivos en una carpeta común, _IMG_ es un directorio de solo archivos de imágenes, _VIDEO_ es un directorio de solo archivos de video y así con los demás directorios.



Esto soluciono mi problema, espero te sirva a ti también.



[Herramienta con la que recupere la información de mi unidad de estado sólido ](https://www.youtube.com/watch?v=Ie1qOMLkkwg)
# Iterative Assessed Activity XBlock

![coverage](coverage-badge.svg)

## Presentación

Este XBlock de desarrollo iterativo asesorado (IAA por sus siglas en inglés), permite construir actividades en que se pueda responder varias veces la misma pregunta a lo largo de un curso, recibiendo feedback personalizado para cada respuesta. Se podrán construir documentos de manera incremental, permitiendo al usuario revisar sus respuestas anteriores.

## Instalación

Para instalar en Devstack (o cualquier instancia de edX):

1. Instalar tanto en el LMS como en Studio:

```bash
$ pip install -e /path/to/iaaxblock
```

2. Aplicar las migraciones (desde el LMS):

```bash
$ python manage.py lms migrate iaaxblock
```

3. Agregar a los cursos mediante el nombre 'iaaxblock'.

4. Incorporar el edx-platform personalizado a la instancia de Open edX, para permitir el borrado y duplicación de bloques.


## Documentación

Este XBlock cuenta con 3 formatos: Completo (_full_), Sólo respuesta anterior (_display_), y Resumen (_summary_).

Haciendo uso del formato Completo, se permite al estudiante responder una pregunta abierta. La respuesta queda guardada para ser referenciada posteriormente. También, es posible mostrar alguna respuesta anterior del estudiante. El formato de Sólo respuesta anterior, como su nombre lo indica, únicamente muestra una respuesta anterior. Por último, el formato Resumen muestra las respuestas que se seleccionen para dicho fin, permitiendo al estudiante observar su avance a lo largo del curso, o la construcción de documentos incrementales, que pueden descargarse en formato Word.

Se cuenta con las siguientes entradas en Studio, las cuales se despliegan dinámicamente según corresponda:

- **Título del bloque**: Texto mostrado como título del contenedor.
- **Tipo de bloque**: "Completo", "Sólo respuesta anterior", "Resumen".
- **Nombre de actividad**: Identificador que asocia las respuestas entre sí, para ser accedidas desde los bloques de Resumen. (_full_)
- **ID**: Identificador numérico único (de hasta 2 decimales) de esta instancia de la actividad. (_full_)
- **Sección**: Identificador que permite asociar varios IDs bajo un subtítulo en los bloques de Resumen. (_full_)
- **Enunciado**: Pregunta que el estudiante debe responder. (_full_)
- **Largo mínimo**: Largo mínimo en caracteres que debe tener la respuesta del estudiante. (_full_)
- **¿Mostrar una respuesta anterior?**: "Sí" o "No", si mostrar una respuesta anterior o no. (_full_)
- **Actividad de respuesta anterior**: Nombre de la actividad cuya respuesta anterior desea verse. (_full, display_)
- **ID de respuesta anterior**: ID de la instancia de la actividad cuya respuesta anterior desea verse. (_full, display_)
- **Título de respuesta anterior**: Texto introductorio que se muestra previo a la respuesta anterior. (_full, display_)
- **Tipo de resumen**: "Completo" o "Sección", ayuda para el llenado automático de 'IDs de resumen'. (_summary_)
- **Sección de resumen**: Sección cuyos IDs se desean ver en el resumen. (_summary_)
- **Visibilidad de resumen**: "Instructores" o "Instructores y alumnos", quienes podrán ver el bloque. (_summary_)
- **Texto de resumen**: Texto introductorio que se muestra previo al resumen. (_summary_)
- **IDs de resumen**: IDs de respuestas que se mostrarán en el resumen. (_summary_)


## TODO

- Repaso general y mejora de estilos de la funcionalidad de feedback.
- Posibilidad de mostrar múltiples respuestas anteriores dentro de un mismo contenedor.

## Licencia

Desarrollado para REDFID.
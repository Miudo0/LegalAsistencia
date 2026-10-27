# LegalAsistencia

Páginas legales y soporte de **Asistencia AMPA/ANPA**, preparadas para GitHub Pages
siguiendo la estructura de LegalMigalla. Contacto: <miudo09dev@gmail.com>.

## Páginas

| Documento | Ruta prevista |
| --- | --- |
| Portada | `/LegalAsistencia/` |
| Política de privacidad | `/LegalAsistencia/privacy-policy/` |
| Condiciones de uso | `/LegalAsistencia/terms-of-use/` |
| Soporte | `/LegalAsistencia/support/` |
| Servicios y licencias | `/LegalAsistencia/third-party-licenses/` |

El repositorio es `Miudo0/LegalAsistencia`. Si cambia, actualizar
`baseurl` en `_config.yml`. Los enlaces usan `relative_url` para respetar esa base.

## Estado

Textos preparados el 2026-10-27 a partir de la implementación de LectorAsistencia,
no de las funciones del generador macOS. Repositorio creado por el usuario:
https://github.com/Miudo0/LegalAsistencia. Primer commit `ecdb8dd` subido a `main`.
Sitio publicado: https://miudo0.github.io/LegalAsistencia/. Las cinco páginas
responden HTTP 200 por HTTPS, comprobadas con cURL el 2026-10-27.
La integración en Ajustes está a cargo de otra IA; App Store Connect sigue pendiente.

Se utiliza el mismo criterio de contacto que LegalMigalla, confirmado por el usuario.
La política de la herramienta no sustituye la información de privacidad de cada ANPA.

## Publicación e integración

1. Revisar los textos y las tareas de `TODO.md`.
2. Subir los archivos al repositorio creado; autorización recibida el 2026-10-27.
3. En GitHub, configurar Settings → Pages → Deploy from a branch y seleccionar
   la rama publicada y la carpeta raíz.
4. Comprobar la compilación Jekyll, HTTPS y las cinco páginas en la URL asignada.
5. Incorporar las URLs definitivas de privacidad y soporte a App Store Connect.
6. Añadir el acceso a privacidad dentro de Ajustes de Asistencia.

La publicación está completada. Pendientes: revisión móvil, App Store Connect
y confirmar la integración en Ajustes realizada por la otra IA.

## Autotest

Desde esta carpeta:

```sh
python3 scripts/validar.py
```

Comprueba front matter, rutas, enlaces internos, configuración y límite de líneas.
No compila Jekyll ni valida jurídicamente los textos. Tras publicar, comprobar con
`curl --fail --location` cada URL de la tabla usando el dominio real asignado por GitHub.

## Mantenimiento

Actualizar fecha de los documentos afectados y `CHANGELOG.md` al cambiar el
tratamiento de datos. Las tareas viven en `TODO.md` y la estructura se documenta
en `ARQUITECTURE.md`.

# Arquitectura de LegalAsistencia

## Alcance

Sitio estático de documentación pública para Asistencia AMPA/ANPA. Sigue la
estructura de LegalMigalla; el contenido describe la lectora iOS/iPadOS.

## Módulos

- `index.md`: entrada y navegación a todos los documentos.
- `privacy-policy.md`: datos, destinatarios, conservación, derechos y contacto.
- `terms-of-use.md`: condiciones de la herramienta y uso por asociaciones.
- `support.md`: contacto, diagnóstico y protección de datos al pedir ayuda.
- `third-party-licenses.md`: servicios, dependencias y recursos externos.
- `_config.yml`: tema, idioma, rutas base y exclusión de documentación interna.
- `scripts/validar.py`: autotest local de documentos, rutas y configuración.

Cada página declara título y permalink. Los enlaces internos usan el filtro
`relative_url` de Jekyll. El tema es `jekyll-theme-minimal`, soportado por GitHub Pages.
No se incluyen JavaScript propio, formularios ni herramientas de analítica.

## Publicación

Repositorio: `Miudo0/LegalAsistencia`, remoto SSH
`git@github.com:Miudo0/LegalAsistencia.git`. GitHub Pages activo desde `main`,
carpeta raíz: https://miudo0.github.io/LegalAsistencia/. Los archivos de
mantenimiento y scripts se excluyen del sitio.

## Validación

`python3 scripts/validar.py` verifica los módulos públicos y configuración.
El 2026-10-27 se comprobaron las cinco rutas públicas mediante cURL: HTTP 200
por HTTPS. La revisión visual en móvil sigue pendiente.

## Referencias utilizadas

- [Normas Apple: privacidad y betas](https://developer.apple.com/app-store/review/guidelines/).
- [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679/oj).
- [WeatherKit](https://developer.apple.com/weatherkit/).
- [Mapas y privacidad](https://www.apple.com/legal/privacy/data/es/apple-maps/).
- [GitHub Pages y datos de visitantes](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection).

Contraste local: entidades Socio, CensoANPA, RegistroAsistencia y CobroEntrada;
exportadores CSV/PDF, escáner VisionKit, repositorios MapKit/WeatherKit,
RedactorResumenFoundationModels y composición SwiftData de LectorAsistencia.

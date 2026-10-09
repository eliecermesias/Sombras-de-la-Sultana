# Documentacion del proyecto: Sombras de la Sultana

Este directorio conserva el historico de trabajo, decisiones, cambios estructurales y acuerdos de produccion del proyecto.

La documentacion no reemplaza los archivos operativos de `Context`, `Skills` o `Episodes`; funciona como memoria del proceso: que se hizo, por que se hizo y donde quedo guardado.

## Estructura

- `History/`: registro cronologico de trabajo realizado.
- `Decisions/`: decisiones de organizacion, direccion y produccion.

## Documentos iniciales

- [History/2026-10-08-worklog.md](History/2026-10-08-worklog.md): historico inicial del trabajo realizado hasta ahora.
- [Decisions/project-structure.md](Decisions/project-structure.md): decisiones sobre estructura de carpetas y responsabilidades de cada directorio.

## Regla de mantenimiento

Cada vez que se haga una intervencion relevante en el proyecto, agregar una entrada en `History` con:

- Fecha.
- Area trabajada.
- Archivos o carpetas modificadas.
- Resumen de cambios.
- Pendientes o siguiente paso.

Cuando se tome una decision que afecte la organizacion del proyecto, registrar el motivo en `Decisions`.

## Regla obligatoria de trazabilidad

Cada vez que se genere o modifique un cuento, imagen, prompt, storyboard, pieza de audio, video, publicacion o edicion del proyecto, debe quedar registrado en `Documentation`.

La entrada debe indicar:

- Que se genero o modifico.
- Para que episodio o area aplica.
- Donde quedo guardado.
- Que habilidad de `Skills` se uso o se actualizo.
- Que queda pendiente, si aplica.

Si durante el trabajo aparece un procedimiento reutilizable, una regla nueva, una estructura de prompt o un criterio de calidad que pueda servir en futuros episodios, debe crearse o actualizarse una habilidad dentro de `Skills`.


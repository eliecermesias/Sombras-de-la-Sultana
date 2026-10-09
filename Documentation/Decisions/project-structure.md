# Decision de estructura del proyecto

## Fecha

2026-10-08

## Decision

El proyecto se organiza con carpetas separadas para produccion, contexto, habilidades y documentacion.

## Directorio oficial

Todo el trabajo debe realizarse dentro de:

`D:\Users\eliec\Documents\Sombras de la Sultana`

No se debe usar como fuente de verdad ningun espejo temporal, carpeta interna de Codex o directorio fuera del workspace oficial.

## Responsabilidad de carpetas

### `Episodes`

Contiene los entregables operativos de cada episodio:

- Historia.
- Storyboard.
- Arte.
- Prompts.
- Audio.
- Video.
- Publicacion.
- Registro.

### `Context`

Contiene la vision general del proyecto y roles de produccion:

- Productor.
- Director.
- Animador.
- Ilustrador.
- Contexto condensado.
- Habilidades generales condensadas.

### `Skills`

Contiene la biblioteca operativa de habilidades:

- Habilidades base del pipeline.
- Sistema de prompts.
- Fichas por episodio.
- Reglas especificas para nutrir cada historia y prompt.

### `Documentation`

Contiene memoria del proceso:

- Historico cronologico.
- Decisiones de estructura.
- Cambios importantes.
- Pendientes y siguientes pasos.

## Motivo

La separacion evita mezclar vision, produccion y trazabilidad. Tambien permite que cada episodio crezca con sus propios prompts e instrucciones sin perder coherencia con la identidad general de *Sombras de la Sultana*.

## Regla

Cuando se cree o modifique una pieza importante del proyecto, registrar el cambio en `Documentation/History`.

## Decision adicional: registro permanente de produccion

Cada cuento, imagen, prompt, storyboard, audio, video, publicacion o edicion debe dejar registro documental. La documentacion es parte del entregable, no una tarea opcional posterior.

Ademas, cada vez que el proyecto genere una practica repetible, se debe crear o actualizar una habilidad en `Skills`. Esto permite que el proyecto aprenda de cada episodio y que los siguientes trabajos no empiecen desde cero.


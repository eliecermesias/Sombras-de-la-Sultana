# Skills - Sombras de la Sultana

Este directorio centraliza las habilidades, historias y prompts reutilizables del proyecto.

La idea es que `Context` conserve la vision general del proyecto y que `Skills` funcione como biblioteca operativa: aqui se documenta como trabajar cada tipo de entrega y como se alimenta cada episodio con sus historias, storyboards y prompts.

## Estructura

- `_base/`: habilidades generales aplicables a todos los episodios.
- `Episodes/`: habilidades, historia, prompts y criterios particulares de cada episodio.

## Habilidades base

- [_base/production-pipeline.md](_base/production-pipeline.md): flujo completo de historia a publicacion.
- [_base/prompt-system.md](_base/prompt-system.md): reglas para construir prompts visuales consistentes.

## Episodios

- [01 - El caminante del cementerio Central](Episodes/01%20-%20El%20caminante%20del%20cementerio%20Central/Skill.md)
- [02 - Tragedia del 7 de agosto](Episodes/02%20-%20Tragedia%20del%207%20de%20agosto/Skill.md)
- [03 - La monja de San Francisco](Episodes/03%20-%20%20La%20monja%20de%20San%20Francisco/Skill.md)
- [04 - El perro de Joaquin de Caicedo y Cuero](Episodes/04%20-%20El%20perro%20de%20Joaquin%20de%20Caicedo%20y%20Cuero/Skill.md)
- [05 - El cura de San Bosco](Episodes/05%20-%20El%20cura%20de%20San%20Bosco/Skill.md)
- [06 - El acomodador del Aristi](Episodes/06%20-%20El%20acomodador%20del%20Aristi/Skill.md)
- [07 - El espejo de Pance](Episodes/07%20-%20El%20espejo%20de%20Pance/Skill.md)

## Regla de uso

Cuando se trabaje un episodio, leer primero su `Skill.md`, luego sus fuentes de historia, storyboard y prompts. Los prompts refinados o nuevos deben guardarse dentro de la carpeta del episodio correspondiente en `Skills/Episodes`.

## Regla de crecimiento

Cada vez que se genere un cuento, imagen, prompt o edicion, revisar si dejo una regla reutilizable. Si la dejo, crear o actualizar una habilidad en este directorio.

Ejemplos de habilidades que deben nacer del trabajo:

- Una plantilla nueva para prompts de imagen.
- Un criterio de direccion para escenas de aparicion.
- Un flujo de edicion de audio o video.
- Una forma de documentar versiones.
- Una regla de continuidad visual para un personaje o lugar.

Todo cambio relevante en `Skills` debe registrarse tambien en `Documentation/History`.


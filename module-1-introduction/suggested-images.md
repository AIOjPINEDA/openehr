# Imágenes Sugeridas para Mejorar la Documentación de openEHR

## 1. Diagrama del Modelo de Dos Niveles de openEHR

Este diagrama ilustra el concepto fundamental del modelado de dos niveles en openEHR, mostrando la separación entre el Modelo de Referencia (estable) y los Arquetipos/Plantillas (conocimiento clínico).

**Fuente recomendada**: https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html#_multi_level_modelling_and_archetypes

**Descripción**: Un diagrama que muestre:
- El nivel inferior (Modelo de Referencia) con sus componentes técnicos estables
- El nivel superior (Arquetipos y Plantillas) con el conocimiento clínico variable
- Las flechas que indican cómo los arquetipos restringen el Modelo de Referencia
- Las plantillas que seleccionan y restringen arquetipos para casos de uso específicos

## 2. Relación entre Arquetipos y Plantillas

Este diagrama muestra cómo las plantillas seleccionan y combinan arquetipos para crear modelos específicos para casos de uso clínicos.

**Fuente recomendada**: Crear un diagrama personalizado basado en la información de la sección 2.3 del documento

**Descripción**: Un diagrama que muestre:
- Varios arquetipos (Blood Pressure, Heart Rate, Weight, etc.)
- Una plantilla seleccionando y combinando estos arquetipos
- Restricciones aplicadas por la plantilla (como hacer opcionales ciertos elementos)
- El resultado final como un modelo específico para un caso de uso

## 3. Ejemplo Visual de Reutilización e Interoperabilidad

Este diagrama ilustra el ejemplo mencionado en la sección 4 sobre cómo dos aplicaciones diferentes pueden usar el mismo arquetipo pero configurarlo de manera diferente.

**Fuente recomendada**: Crear un diagrama personalizado basado en la información de la sección 4 del documento

**Descripción**: Un diagrama que muestre:
- Un arquetipo central de Blood Pressure
- Dos plantillas diferentes (sistema ambulatorio y hospitalario) que usan este arquetipo
- Diferentes configuraciones en cada plantilla (elementos opcionales vs. obligatorios)
- Flujo de datos entre sistemas mostrando la interoperabilidad

## 4. Estructura del Modelo de Referencia

Este diagrama muestra los componentes principales del Modelo de Referencia de openEHR.

**Fuente recomendada**: https://specifications.openehr.org/releases/RM/latest/ehr.html

**Descripción**: Un diagrama que muestre:
- Los principales paquetes del Modelo de Referencia
- Tipos de datos y estructuras de datos
- Tipos de entrada (OBSERVATION, EVALUATION, INSTRUCTION, ACTION)
- Relaciones entre estos componentes

## 5. Diagrama de Flujo de Implementación

Este diagrama muestra el flujo de trabajo para implementar un sistema basado en openEHR.

**Descripción**: Un diagrama que muestre:
1. Selección/creación de arquetipos
2. Desarrollo de plantillas para casos de uso específicos
3. Implementación en sistemas clínicos
4. Intercambio de datos entre sistemas

## Notas para la Implementación

- Todas las imágenes deben incluir leyendas claras y explicativas
- Se recomienda usar colores consistentes para representar los diferentes componentes (RM, arquetipos, plantillas)
- Incluir versiones simplificadas para conceptos introductorios y versiones más detalladas para referencia
- Considerar la creación de versiones animadas o interactivas para presentaciones o formación

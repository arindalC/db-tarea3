# ITAM Primavera 2025 - Tarea de Normalización
Integrantes del equipo: 
- Arindal Contreras Arrellano — 208529
- Lourdes Angélica Gutiérrez Landa — 207706
- Arturo Rodríguez Vázquez 
- Bernardo González Moreno 
---

## Configuración:

Este proyecto no tiene dependencias adicionales de Python, por lo que no es 
necesario crear un ambiente virtual. Está desarollado y probado con Python 3.13,
pero debe funcionar con 3.8 o superior.

## Descripción: 
Esta tarea implementa funciones para analizar dependencias funcionales y multivaluadas dentro de una relación y verificar si cumple con la forma normal de Boyce-Codd (BCNF) y la cuarta forma normal (4NF). Incluye funciones para evaluar la trivialidad de dependencias, calcular cierres, y verificar llaves.

## Estructura:
[1. components.py](https://github.com/arindalC/db-tarea3/blob/main/normalization/components.py): Implementación de `is_trivial` para dependencias funcionales y multivaluadas.

[2. algorithms.py](https://github.com/arindalC/db-tarea3/blob/main/normalization/algorithms.py): Implementación de las funciones de normalización (`closure`, `is_key`, `is_relvar_in_bcnf`,`is_relvar_in_4nf`).

## Funcionalidades

- **`FunctionalDependency.is_trivial()`**:
  - Una dependencia funcional es trivial si los atributos dependientes ya están contenidos en el conjunto del determinante.
  - Regresa `True` si es trivial, `False` si no lo es.
  
- **`MultivaluedDependency.is_trivial(heading)`**:
  - Regresa `True` si es trivial respecto al encabezado, `False` si no.

- **`closure(attributes, functional_dependencies)`**
  - Calcula el cierre de un conjunto de atributos, i.e. conjunto de todos los atributos que pueden ser determinados funcionalmente
 
- **`is_superkey(attributes, heading, functional_dependencies)`**
  - Verifica si `attributes` es una superllave, i.e. si puede determinar todos los atributos del encabezado.
 
- **`is_key(attributes, heading, functional_dependencies)`**
  - Verifica si `attributes` es una llave , i.e. no existe un subconjunto propio que también sea superllave.
 
- **`is_relvar_in_bcnf(relvar)`**
  - Verifica si para cada dependencia funcional no trivial, el determinante es una superllave.
  - Regresa `True` si la relvar está en BCNF, `False` si no.
 
- **`is_relvar_in_4nf(relvar)`**
  - Verifica si una relvar está en 4NF si está en BCNF y además, para cada dependencia multivaluada no trivial, el determinante es una superllave.
  - Regresa `True` si la relvar está en 4NF, `False` si no.

## Suposiciones Realizadas
1. Las dependencias funcionales y multivaluadas están definidas correctamente. 
2. Las clases `FunctionalDependency`, `MultivaluedDependency` y `Relvar` proporcionan métodos y propiedades como `determinant`, `dependant`, `functional_dependencies`, `multivalued_dependencies` y `heading`.









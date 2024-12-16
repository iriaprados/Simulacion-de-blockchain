# Simulación de Blockchain con Proof of Stake

Este proyecto es una simulación de un sistema de blockchain implementado en Python. El objetivo principal es demostrar cómo funciona un mecanismo de consenso **Proof of Stake (PoS)** utilizando múltiples nodos que compiten por la oportunidad de crear bloques en la cadena.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Estructura del Código](#estructura-del-código)
- [Requisitos](#requisitos)
- [Ejecución](#ejecución)
- [Ejemplo de Salida](#ejemplo-de-salida)
- [Notas](#notas)
- [Contribuciones](#contribuciones)

---

## Descripción

Este proyecto simula la creación de una blockchain con un número configurable de bloques y nodos. Cada nodo tiene una probabilidad asociada para ser seleccionado como el productor del siguiente bloque, basada en el mecanismo de **Proof of Stake**.

El proceso incluye:
1. **Selección del productor del bloque**: Según probabilidades predefinidas.
2. **Sección crítica protegida por un mutex**: Solo un nodo puede crear un bloque a la vez.
3. **Producción de bloques**: Cada bloque incluye información como un índice, marca de tiempo, hash y referencia al bloque anterior.

---

## Características

- Simulación de nodos con probabilidades diferentes para ser seleccionados.
- Uso de un **mutex** para proteger la sección crítica y evitar condiciones de carrera.
- Generación de bloques con hash único basado en datos específicos.
- Almacenamiento de la blockchain como una lista de bloques.

---

## Estructura del Código

1. **Clase `block`**:
   Representa un bloque en la blockchain, con atributos como índice, marca de tiempo, hash y nodo productor.

2. **Funciones principales**:
   - `proof_of_stake()`: Selecciona un nodo productor basado en probabilidades.
   - `critical_section()`: Simula la producción de un bloque y lo añade a la blockchain.
   - `run_node()`: Define el comportamiento de cada nodo en la simulación.

3. **Función principal `main()`**:
   Inicia múltiples hilos, cada uno representando un nodo, y gestiona la producción de bloques.

---

## Requisitos

Para ejecutar este proyecto, necesitas:
- Python 3.x
- Librerías estándar (`threading`, `time`, `random`, `hashlib`)

---

## Ejecución

Sigue estos pasos para ejecutar la simulación:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/blockchain-simulation.git
   cd blockchain-simulation

## Ejemplo de salida 
Nodo 1 iniciado

Nodo 2 iniciado

Nodo 3 iniciado

Nodo 4 iniciado

Nodo 3 ha sido seleccionado para producir el bloque 0
Nodo 3 accedió a la sección crítica...
Nodo 3 adquirió el lock en tiempo 1733775156
Nodo 3 ha creado el bloque 0
Nodo 3 ha liberado la sección crítica

...
Índice: 0
Timestamp: 1733775156
Hash del bloque: e3b0c44298...
Productor del bloque: Nodo 3
Hash del bloque anterior: 0
...

> [!NOTE]
> Los pesos de selección para los nodos pueden ajustarse modificando el diccionario probabilidades:
> **probabilidades = {"Nodo 1": 50, "Nodo 2": 30, "Nodo 3": 20}**

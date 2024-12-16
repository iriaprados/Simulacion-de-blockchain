from hashlib import sha256
import threading
import time
import random

# Definir variables globales 
num = 4  # Número de nodos
blocks = 12  # Número de bloques
mutex = threading.Lock()  # Crear mutex
blockchain = []  # Lista que simula el blockchain, para el almacenamiento de los bloques
probabilidades = {"Nodo 1": 50, "Nodo 2": 30, "Nodo 3": 20}  # Probabilidad de cada nodo

# Creación de la clase block
class block:
    def __init__(self, index, timestamp, block_hash, previous_hash, validator):
        self.index = index  # Posición del bloque en la cadena
        self.timestamp = timestamp  # Marca de tiempo de generación del bloque
        self.block_hash = block_hash  # Hash del bloque
        self.previous_hash = previous_hash  # Hash del bloqueo anterior
        self.validator = validator  # Nodo productor del bloque

    def __str__(self):
        return (f'Bloque (Indice: {self.index}, Marca de tiempo: {self.timestamp}, Hash: {self.block_hash}, Hash previo: {self.previous_hash}, Nodo creador: {self.validator})\n')


# Función proof_of_stake()
def proof_of_stake():
    # Convertir los valores del diccionario probabilidades en listas
    nodos = list(probabilidades.keys())  # Nombre de los nodos
    pesos = list(probabilidades.values())  # Participaciones (70,10,20)

    seleccion = random.choices(nodos, weights=pesos, k=1)[0]  # Selección del nodo basado en los pesos definidos en el diccionario

    print(f'\nProbabilidades de selección de los nodos: {probabilidades}')
    print(f'El nodo seleccionado para la producción del bloque es el {seleccion}\n')

    return seleccion


# Función para la sección crítica
def critical_section(productor, particiones, mutex):
    print(f'\nEl nodo {productor} intenta acceder a la sección crítica del bloque')

    mutex.acquire()  # Abrir mutex

    print(f'El nodo productor {productor} tiene el mutex')

    if blockchain:
        bloque_anterior = blockchain[-1]  # Si en la blockchain hay un bloque anterior se captura
    else:
        bloque_anterior = None  # En la blockchain no hay un bloque anterior

    timestamp = int(time.time())  # Tiempo actual (segundos)

    if bloque_anterior:
        hash_anterior = bloque_anterior.block_hash  # Si hay un bloque previo en el blockchain, se obtiene su hash
    else:
        hash_anterior = '0'  # Si no hay bloque anterior, se indica con cero

   
    datos = str(len(blockchain)) + str(particiones) + str(timestamp) + hash_anterior  # Datos para generar el hash

    block_hash = sha256(datos.encode()).hexdigest() # Hash para los datos 

    nuevo_bloque = block(len(blockchain), timestamp, block_hash, hash_anterior, productor) # Creación del bloque 

    blockchain.append(nuevo_bloque)

    time.sleep(2)

    mutex.release() # Liberar el mutex

    print(f'Bloque {nuevo_bloque.index} producido, el nodo {productor} liberado el mutex\n')


# Función principal que simula el proceso de producción de bloques
def main():
    for i in range(5):
        print(f'Selección {i + 1}:')
        productor = proof_of_stake()

        # Generar hilos 
        thread = threading.Thread(target=critical_section, args=(productor, i, mutex)) # Hilos con target la sección crítica 
        thread.start()
        thread.join() 


if __name__ == "__main__":
    # Crear el bloque génesis
    genesis_block = block(0, time.time(), "hash_inicial", None, "Node-1")
    blockchain.append(genesis_block)  # Añadir el bloque génesis

    print(genesis_block)  # Muestra los datos del bloque génesis

    # Llamar a la función principal
    main()

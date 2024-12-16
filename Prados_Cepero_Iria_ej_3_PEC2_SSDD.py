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

# Creación de la clase block, crea un bloque
class block:
    def __init__(self, index, timestamp, block_hash, previous_hash, validator):
        self.index = index  # Posición del bloque en la cadena
        self.timestamp = timestamp  # Marca de tiempo de generación del bloque
        self.block_hash = block_hash  # Hash del bloque
        self.previous_hash = previous_hash  # Hash del bloqueo anterior
        self.validator = validator  # Nodo productor del bloque

    def __str__(self):
        return (f'Bloque (Indice: {self.index}, Marca de tiempo: {self.timestamp}, Hash: {self.block_hash}, Hash previo: {self.previous_hash}, Nodo creador: {self.validator})\n')


# Función proof_of_stake(), selecciona el nodo que puede participar 
def proof_of_stake():
    # Convertir los valores del diccionario probabilidades en listas
    nodos = list(probabilidades.keys())  # Nombre de los nodos
    pesos = list(probabilidades.values())  # Participaciones (70,10,20)

    seleccion = random.choices(nodos, weights=pesos, k=1)[0]  # Selección del nodo basado en los pesos definidos en el diccionario

    # print(f'\nProbabilidades de selección de los nodos: {probabilidades}')
    # print(f'El nodo seleccionado para la producción del bloque es el {seleccion}\n')

    return seleccion


# Función para la sección crítica, simula creación del bloque 
def critical_section(productor, particiones, mutex):
    print(f'{productor} accedió a la sección crítica ...')

    mutex.acquire()  # Abrir mutex

    print(f'{productor} adquirió el lock en tiempo {int(time.time())}')

    if blockchain:
        bloque_anterior = blockchain[-1]  # Si en la blockchain hay un bloque anterior se captura
    else:
        bloque_anterior = None  # En la blockchain no hay un bloque anterior

    timestamp = int(time.time())  # Generar el tiempo actual (segundos)

    if bloque_anterior:
        hash_anterior = bloque_anterior.block_hash  # Si hay un bloque previo en el blockchain, se obtiene su hash
    else:
        hash_anterior = '0'  # Si no hay bloque anterior, se indica con cero

   # Generación del hash 
   # Datos: ID del nodo, particiones del nodo, timestamp en segundos, hash del bloque anterior
    datos = str(len(blockchain)) + str(particiones) + str(timestamp) + hash_anterior 

    hash = sha256(datos.encode()).hexdigest() # Hash generado apartir de los datos  

    nuevo_bloque = block(len(blockchain), timestamp, hash, hash_anterior, productor) # Creación del bloque. 

    blockchain.append(nuevo_bloque)

    time.sleep(2) # Simulación del trabajo 

    print(f'{productor} ha creado el bloque {nuevo_bloque.index}')
    mutex.release() # Liberar el mutex
    print(f'{productor} ha liberado la sección crítica')

# Función para definir el compartamiento de lso nodos 
def run_node(productor, mutex): 
    print(f'{productor} iniciado\n')

    time.sleep(0.5) # Retraso entre la impresión y el comienzo del ciclo 

    while len(blockchain) < blocks: # Mientras la blockchain contenga menos bloques que el objetivo (12) 
        print(f'{productor} está esperando para producir un bloque')

        nodo_productor = proof_of_stake()

        if nodo_productor == productor: 
            print(f'{productor} ha sido seleccionado para producir el bloque {len(blockchain)}') 
            critical_section(productor, len(blockchain), mutex)
        time.sleep(1)

# Función principal que simula el proceso de producción de bloques
def main():
    hilos= [] # Inciar todos los hilos 
    for i in range(1, num+1): # Para cada uno de los nodos genrados, se crea un hilo
        hilo= threading.Thread(target=run_node, args=(f'Nodo {i}', mutex)) # Los hilos con target la función run_node
        hilos.append(hilo)
        hilo.start()
    
    for hilo in hilos: # Esperar que todos los hilos terminen 
        hilo.join()
    
     # Imprimir la cadena de bloques una vez todos los bloques hayan sido producidos
    print("\nCADENA DE BLOQUES FINAL:")
    for block in blockchain:
        print(f"\nÍndice: {block.index} \nTimestamp: {block.timestamp} \nHash del bloque: {block.block_hash} \nProductor del bloque: {block.validator} \nHash del bloque anterior: {block.previous_hash}")
 
if __name__ == "__main__":
    # Llamar a la función principal
    main()

# EJERCICIO 3 

# Importar librerías 
import hashlib
import threading
import time
import random

# Definir variables globales 
num= 4 # Número de nodos
blocks= 12 # Número de bloques 
mutex= threading.Lock() # Creae mutex 
blockchain = [] # Lista que simula el blockchain, para el almacenamiento de los bloques 
probabilidades = {"Nodo 1": 50, "Nodo 2": 30, "Nodo 3": 20} # Probabilidad de cada nodo 

# Creación de la clase block 
class block: 
    def __init__(self, index, timestamp, block_hash, previous_hash, validator):

        self.index= index # Posición del bloque en la cadena 
        self.timestamp= timestamp # Marca de tiempo de generación del bloque
        self.block_hash= block_hash # Hash del bloque 
        self.previous_hash= previous_hash # Hash del bloqueo anterior 
        self.validator= validator # Nodo productor del bloque 
    
    def __str__(self):
        return(f'Bloque (Indice: {self.index}, Marca de tiempo: {self.timestamp}, Hash: {self.block_hash}, Hash previo: {self.previous_hash}, Nodo creador: {self.validator})\n')

# Prueba para clase block, borrar 
if __name__ == "__main__":
    # Ejemplo de un bloque
    genesis_block = block(0, time.time(), "hash_inicial", None, "Node-1")
    print(genesis_block)  # Muestra los datos del bloque

# Función proof_of_stake()
def proof_of_stake(): 
    # Convertir los valores del diccionario probabilidades en listas 
    nodos = list(probabilidades.keys()) # Nombre de los nodos 
    pesos = list(probabilidades.values()) # Participaciones (70,10,20)

    seleccion= random.choices(nodos, weights= pesos, k= 1) [0] # Selección del nodo basado en los pesos definidos en el diccionario 

    print(f'\nProbabilidades de selección de los nodos: {probabilidades}')
    print(f'El nodo seleccionado para la producción del bloque es el {seleccion}\n')

    return seleccion

# Prueba para la función proof_of_stake(), borrar 

if __name__ == "__main__": 
    for i in range (5): 
        print(f'Selección {i+1}: ')
        proof_of_stake()
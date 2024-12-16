# EJERCICIO 3 

# Importar librerías 
import hashlib
import threading
import time

# Definir variables globales 
num= 4 # Número de nodos
blocks= 12 # Número de bloques 
mutex= threading.Lock() # Creae mutex 
blockchain = [] # Lista que simula el blockchain, para el almacenamiento de los bloques 

# Creación de la clase block 
class block: 
    def __init__(self, index, timestamp, block_hash, previous_hash, validator):

        self.index= index # Posición del bloque en la cadena 
        self.timestamp= timestamp # Marca de tiempo de generación del bloque
        self.block_hash= block_hash # Hash del bloque 
        self.previous_hash= previous_hash # Hash del bloqueo anterior 
        self.validator= validator # Nodo productor del bloque 
    
    def __str__(self):
        return(f"Bloque (Indice: {self.index}, Marca de tiempo: {self.timestamp}, Hash: {self.block_hash}, Hash previo: {self.previous_hash}, Nodo creador: {self.validator})\n")

# Prueba para clase block, borrar 
# if __name__ == "__main__":
#     # Ejemplo de un bloque
#     genesis_block = block(0, time.time(), "hash_inicial", None, "Node-1")
#     print(genesis_block)  # Muestra los datos del bloque

# Función proof_of_stake()
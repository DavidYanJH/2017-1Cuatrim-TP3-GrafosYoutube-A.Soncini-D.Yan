from pruebas import *
from grafo import Grafo
from auxiliares import *

def main():
	pruebas()
	grafo = Grafo()
	cargar_grafo(grafo)
	lista_walks = random_walks(grafo, 1, 20, 10)
	print(type(lista_walks))
	similares(grafo, 1, 5, lista_walks)

main()
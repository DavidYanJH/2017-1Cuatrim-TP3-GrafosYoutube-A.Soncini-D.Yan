from grafo import Grafo
from auxiliares import *
from time import time

def pruebas():
	"""********************************Simple Test*****************************"""
	"""print("Simple Test de las diferentes funciones del Grafo")
	grafo = Grafo()
	print("")
	print("Un grafo vacio ha sido creado exitosamente")
	print("El grafo vacio tiene {} vertices".format(grafo.vertices))
	print("El grafo vacio tiene {} aristas".format(grafo.aristas))
	print("")

	print("Insercion de los vertices 0, 1, 2, 3, 4, 5, 6, 7, 8, 9")
	grafo.add_vertice(0)
	grafo.add_vertice(1)
	grafo.add_vertice(2)
	grafo.add_vertice(3)
	grafo.add_vertice(4)
	grafo.add_vertice(5)
	grafo.add_vertice(6)
	grafo.add_vertice(7)
	grafo.add_vertice(8)
	grafo.add_vertice(9)
	print("El grafo tiene {} vertices despues de la insercion".format(grafo.vertices))
	print("El grafo tiene {} aristas despues de la insercion".format(grafo.aristas))
	print("Los vertices existentes en el grafo son:")
	lista = grafo.get_vertices() 
	for vertice in lista:
		print("Vertice {}".format(vertice))
	print("")

	print("Agrego aristas de 0 a 1, 2, 3, 8")
	grafo.add_arista(0, 1)
	grafo.add_arista(0, 2)
	grafo.add_arista(0, 3)
	grafo.add_arista(0, 8)
	print("El grafo tiene {} aristas actualmente".format(grafo.aristas))
	print("Agrego aristas de 1 a 2, 3")
	grafo.add_arista(1, 2)
	grafo.add_arista(1, 3)
	print("El grafo tiene {} aristas actualmente".format(grafo.aristas))
	print("v1 y v0 son adyacentes entre si {}".format(grafo.son_adyacentes(1, 0)))
	print("v0 y v8 son adyacentes entre si {}".format(grafo.son_adyacentes(0, 8)))
	print("v2 y v3 no son adyacentes entre si {}".format(not grafo.son_adyacentes(2, 3)))
	print("")
	
	adyacentes = grafo.get_adyacentes(0)
	for vertice in adyacentes:
		print("Vertice 0 tiene como adyacentes a {}".format(vertice))
	print("")
	
	adyacentes = grafo.get_adyacentes(1)
	for vertice in adyacentes:
		print("Vertice 1 tiene como adyacentes a {}".format(vertice))
	print("")
		
	adyacentes = grafo.get_adyacentes(9)
	if len(adyacentes) == 0 : 
		print("El vertice 9 no tiene ningun adyacente actualmente")	
		print("")

	print("Elimino el arista entre 1 y 0")
	grafo.remove_arista(1, 0)
	print("v1 y v0 ya no son adyacentes entre si {}".format(not grafo.son_adyacentes(0, 1)))
	print("Ahora el grafo aun tiene {} aristas".format(grafo.aristas))
	print("Elimino el arista entre 0 y 8")
	grafo.remove_arista(0, 8)
	print("v0 y v8 ya no son adyacentes entre si {}".format(not grafo.son_adyacentes(0, 8)))
	print("Ahora el grafo aun tiene {} aristas".format(grafo.aristas))		
	print("")

	print("Elimino el vertice 0 del grafo")
	grafo.remove_vertice(0)
	print("El vertice 0 ya no existe en el grafo {}".format(not grafo.vertice_exist(0)))
	print("El grafo tiene {} aristas despues de eliminar el vertice 0".format(grafo.aristas))
	print("Elimino el vertice 1 del grafo")
	grafo.remove_vertice(1)
	print("El vertice 1 ya no existe en el grafo {}".format(not grafo.vertice_exist(1)))
	print("El grafo tiene {} aristas despues de eliminar el vertice 1".format(grafo.aristas))
	print("")

	print("Agrego al grafo el vertice 1 nuevamente")
	grafo.add_vertice(1)
	print("Agrego al grafo el vertice 0 nuevamente")
	grafo.add_vertice(0)
	print("Nuevamente el grafo tiene los {} vertices orginales".format(grafo.vertices))
	print("El grafo tiene ahora {} aristas".format(grafo.aristas))
	print("")

	print("Agrego aristas al grafo con 10 vertices")
	print("Agrego 4 aristas de 0 a 1, 2, 3, 8")
	grafo.add_arista(0, 1)
	grafo.add_arista(0, 2)
	grafo.add_arista(0, 3)
	grafo.add_arista(0, 8)
	print("El grafo ahora tiene {} aristas".format(grafo.aristas))
	print("Agrego 2 aristas de 1 a 2, 3")
	grafo.add_arista(1, 2)
	grafo.add_arista(1, 3)
	print("El grafo ahora tiene {} aristas".format(grafo.aristas))
	print("Agrego 1 arista entre 2 y 3")
	grafo.add_arista(2, 3)
	print("El grafo ahora tiene {} aristas".format(grafo.aristas))
	print("Agrego 3 aristas de 3 a 4, 6, 8")
	grafo.add_arista(3, 4)
	grafo.add_arista(3, 6)
	grafo.add_arista(3, 8)
	print("Agrego 1 arista entre 4 y 5")
	grafo.add_arista(4, 5)
	print("El grafo ahora tiene {} aristas".format(grafo.aristas))
	print("Agrego 1 arista entre 5 y 6")
	grafo.add_arista(5, 6)
	print("El grafo ahora tiene {} aristas".format(grafo.aristas))
	print("Agrego 3 aristas de 6 a 7, 8, 9")
	grafo.add_arista(6, 7)
	grafo.add_arista(6, 8)
	grafo.add_arista(6, 9)
	print("El grafo ahora tiene {} aristas".format(grafo.aristas))
	print("Agrego 1 arista entre 7 y 8")
	grafo.add_arista(7, 8)
	print("El grafo ahora tiene {} aristas".format(grafo.aristas))
	print("Agrego 1 arista entre 8 y 9")
	grafo.add_arista(8, 9)
	print("El grafo finalmente tiene {} aristas".format(grafo.aristas))
	print("")"""

	"""********************************Random Walks Test*****************************"""
	"""print("Test Simple de Random_Walks\n")
	print("3 random walks de longitud 6 desde el vertice 0")
	lista_walks = random_walks(grafo, 0, 9, 3)
	for i in range(3):
		print(lista_walks[i])
	print("")	
	print("8 random walks de longitud 6 desde un vertice aleatorio")
	lista_walks = random_walks(grafo, None, 6, 8)
	for i in range(8):
		print(lista_walks[i])
	print("")

	print("Test de Casos Bordes de Random Walks\n")
	print("3 random walks de longitud 9 desde el vertice 11")
	lista_walks = random_walks(grafo, 11, 9, 3)
	if lista_walks is None:
		print("None ya que el vertice 11 no existe en el grafo\n")
	print("3 random walks de longitud 1 desde un vertice aleatorio")	
	lista_walks = random_walks(grafo, None, 1, 3)
	if lista_walks is None:
		print("None ya que la longtitud de cada camino es menor igual a 1\n")
	print("0 random walks de longitud 3 desde un vertice aleatorio")	
	lista_walks = random_walks(grafo, None, 3, 0)
	if lista_walks is None:	
		print("None ya que la cantidad de random walks a realizar es 0\n")"""
		
	"""******************************Test: Iteracion del Grafo**************************"""
	"""print("Listado de todos los Vertices existentes en el Grafo:")
	for i in grafo:
		print("Vertice {}".format(i))	
	print("")"""
	
	"""********************************Grafo Stats Test******************************"""
	"""grafo_stats(grafo)
	print("")"""

	"""**************************Grafo Carga & Similares Test************************"""
	print("*********************Comienzo de los Test*********************")
	print(".....................Carga del Grafo.....................")
	time_inicial = time()
	grafo = Grafo()
	cargar_grafo(grafo)
	time_final = time()
	time_execution = time_final - time_inicial
	print("Tiempo de Ejecucion de la Carga del Grafo: {}\n".format(time_execution))
	"""*********************************Fin de Carga Test****************************"""

	"""print("*********************************Similares a 1********************************")
	similares(grafo, "1", 5)
	print("*********************************Similares a 4********************************")
	similares(grafo, "4", 10)
	print("*********************************Similares a 10420****************************")
	similares(grafo, "10420", 8)
	print("")

	print("*********************************Recomendar a 1********************************")
	recomendar(grafo, "1", 5)
	print("*********************************Recomendar a 4********************************")
	recomendar(grafo, "4", 10)
	print("*********************************Recomendar a 10420****************************")
	recomendar(grafo, "10420", 8)"""

	"""********************************Grafo Stats Test******************************"""
	grafo_stats(grafo)
	print("")

	"""*******************************Distancia Stats Test***************************"""
	print("Prueba de Distancia con Usuario 9")
	time_inicial = time()
	distancia_stats(grafo, "9")
	time_final = time()
	time_execution = time_final - time_inicial
	print("Tiempo de Ejecucion de Distancia de un Vertice: {}\n".format(time_execution))

	print("*********************Fin de los Test*********************")
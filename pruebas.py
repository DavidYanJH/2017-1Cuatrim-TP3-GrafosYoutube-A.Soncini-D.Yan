from grafo import Grafo
from auxiliares import *
from time import time

def pruebas():
	
	"""**************************Grafo Carga Test************************"""
	print("*********************Comienzo de los Test*********************")
	print(".....................Carga del Grafo.....................")
	time_inicial = time()
	grafo = Grafo()
	cargar_grafo(grafo)
	time_final = time()
	time_execution = time_final - time_inicial
	print("Tiempo de Ejecucion de la Carga del Grafo: {}\n".format(time_execution))

	"""*****************************Similares & Recomendar Test************************"""
	print("*********************************Similares a 1********************************")
	similares(grafo, "1", 6)
	print("*********************************Similares a 9********************************")
	similares(grafo, "9", 10)
	print("*********************************Similares a 10238****************************")
	similares(grafo, "10238", 8)
	print("")

	print("*********************************Recomendar a 1********************************")
	recomendar(grafo, "1", 8)
	print("*********************************Recomendar a 4********************************")
	recomendar(grafo, "9", 10)
	print("*********************************Recomendar a 10238****************************")
	recomendar(grafo, "10238", 20)

	"""********************************Grafo Stats Test******************************"""
	time_inicial = time()
	grafo_stats(grafo)
	time_final = time()
	time_execution = time_final - time_inicial
	print("Tiempo de Ejecucion de Stats del Grafo: {}\n".format(time_execution))
	

	"""******************************Camino Minimo BFS Test****************************"""
	time_inicial = time()
	print("camino 11 1991")
	contactos_conexion(grafo, "11", "1991")
	print("camino 1 7")
	contactos_conexion(grafo, "1", "7")
	print("camino 9 1")
	contactos_conexion(grafo, "9", "1")
	time_final = time()
	time_execution = time_final - time_inicial
	print("Tiempo de Ejecucion de Camino Minimo: {}\n".format(time_execution))

	"""*******************************Distancia Stats Test***************************"""
	print("Prueba de Distancia con Usuario 9")
	time_inicial = time()
	distancia_stats(grafo, "9")
	time_final = time()
	time_execution = time_final - time_inicial
	print("Tiempo de Ejecucion de Distancia de un Vertice: {}\n".format(time_execution))

	print("*********************Fin de los Test*********************")
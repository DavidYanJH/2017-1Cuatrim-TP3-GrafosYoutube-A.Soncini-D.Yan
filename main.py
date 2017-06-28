import sys
from grafo import Grafo
from auxiliares import *

def display_menu(grafo):
	menu = {'similares': similares, 'recomendar': recomendar, 'camino': contactos_conexion, 'centralidad': centralidad, 'distancias': distancia_stats, 'estadisticas': grafo_stats, 'comunidades': comunidades, '?': ayuda}

	print("A continuacion, escriba un comando (? para ayuda):")
	print("> ", end='')
	command = input()
	while (command != "exit"):
		args = command.split()
		try:
			menu[args[0]](grafo, args)
		except:
			print("Error. El comando es inexistente.")
		print("A continuacion, escriba un comando (? para ayuda):")
		print("> ", end='')
		command = input()

def main():
	if (len(sys.argv) != 2):
		print("Error. Debe ejecutar el programa con solo un argumento.")
		return

	grafo = Grafo()
	try:
		cargar_grafo(grafo, sys.argv[1])
	except IOError:
		return
	display_menu(grafo)

main()
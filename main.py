import sys
from grafo import Grafo
from auxiliares import *

def display_menu(grafo):
	menu = {'similares': similares, 'recomendar': recomendar, 'camino': contactos_conexion, 'centralidad': centralidad, 'distancias': distancia_stats, 'estadisticas': grafo_stats, 'comunidades': comunidades, 'ayuda': ayuda_specific, '?': ayuda_general, 'exit': exit}

	print("A continuacion, introduzca un comando ('?' si desea acceder al manual con los comandos disponibles)")
	print("> ", end='')
	command = input()
	while (command != "exit"):
		args = command.split()
		try:
			if (args[0] == "ayuda" or args[0] == "?"):
				menu[args[0]](menu, args)	
			else: 
				menu[args[0]](grafo, args)
		except Exception:
			print("Error en el Comando Introducido.")
		print("A continuacion, introduzca un comando ('?' si desea acceder al manual con los comandos disponibles)")
		print("> ", end='')
		command = input()


def main():
	NUM_ARGUM = 2
	if (len(sys.argv) != NUM_ARGUM):
		print("El Usuario debe indicar la Ruta y el Nombre del Archivo con los datos de la Red Social al ejecutar el Programa.")
		print("Error en la Cantidad de Argumentos al invocar el Programa.")
		return 0		
	grafo = Grafo()
	try:
		cargar_grafo(grafo, sys.argv[1])
	except IOError:
		print("Error al Abrir el Archivo < {} > con los Datos de la Red Social.\n".format(sys.argv[1]))
		return 0
	display_menu(grafo)

main()
import random
from heapq import *

def cargar_grafo(grafo):
	file = open('com-youtube.ungraph.txt', 'r')
	linea = file.readline()
	linea = linea.rstrip("\n")

	while (linea != ''):
		if not (linea[0] == '#'):
			lista = linea.split("\t")
			verticeant = lista[0]
			grafo.add_vertice(verticeant)
			while (linea != '') and (verticeant == lista[0]):
				grafo.add_vertice(lista[1])
				grafo.add_arista(verticeant, lista[1])
				linea = file.readline()
				linea = linea.rstrip("\n")
				lista = linea.split("\t")
		else:
			linea = file.readline()
			linea = linea.rstrip("\n")

	file.close()
	#print("El grafo quedo con {} Vertices y {} Aristas".format(grafo.vertices, grafo.aristas))

def random_walks(grafo, v_inicial, lenght_walk, total_walk):
	"""Realiza una serie de random walks o recorridos aleatorios en el grafo dado.
	   la variable total_walk determina la cantidad de recorridos a realizar;
	   la variable lenght_walk determina la longitud de cada recorrido aleatorio;
	   la variable v_inicial determina el vertice de partida de cada recorrido:
	   si v_inicial is None entonces los recorridos partiran desde cualquier
	   vertice aleatorio del grafo dado, en cambio si v_inicial is not None y existe
	   en el grafo dado entonces sera el vertice de partida.
	   La funcion random_walks retorna una lista con los recorridos aleatorios realizados
	   en forma de listas de vertices, en caso de error retorna un None."""
	if v_inicial is not None and not grafo.vertice_exist(v_inicial): return None
	if lenght_walk <= 1 or total_walk <= 0: return None    
	   
	lista_walks = []
	
	if v_inicial is None:
		vertices = grafo.get_vertices()
		v_inicial = random.choice(vertices)

	for i in range(total_walk):
		walk = []
		walk.append(v_inicial)
		v_actual = v_inicial
		for j in range(1, lenght_walk):
			ady_actual = grafo.get_adyacentes(v_actual)
			v_actual = random.choice(ady_actual)
			walk.append(v_actual)
		lista_walks.append(walk)
	return lista_walks

def grafo_stats(grafo):
	print("-----------Datos Estadisticos del Grafo------------")
	print("Cantidad de Vertices del Grafo: {}".format(grafo.vertices))
	print("Cantidad de Aristas del Grafo: {}".format(grafo.aristas))
	vertices = float(grafo.vertices)
	aristas = float(grafo.aristas)
	grado_promedio = aristas / vertices
	print("Promedio de Grado de Entrada de cada Vertice: {:.2f}".format(grado_promedio))
	print("Promedio de Grado de Salida de cada Vertice: {:.2f}".format(grado_promedio))
	max_arista = vertices * (vertices - 1) / 2
	densidad_relat = aristas / max_arista
	print("Densidad Relativa del Grafo: {:.2f}".format(densidad_relat))

def obtener_lista_semejantes(grafo, userid):
	lista_walks = random_walks(grafo, userid, 20000, 100)
	diccionario = {}
	total = 0
	#Realizo el conteo de apariciones totales por usuario (utilizo diccionario)
	for caminos in lista_walks:
		for vertice in caminos:
			if vertice in diccionario:
				diccionario[vertice] +=1
			else:
				diccionario[vertice] = 1
				total +=1
	heap = []
	#Ingreso todos los valores en Heap
	for user in diccionario:
		tupla = (diccionario[user], user)
		heappush(heap, tupla)

	listaord = []
	#Heapsort
	for i in range(total):
		listaord.append(heappop(heap))

	#Quito al mismo usuario del resultado
	listaord.pop()
	return listaord

def similares(grafo, userid, cantsimil):
	"""Calcula la cantidad 'cantsimil' de usuarios semejantes a 'userid', 
	   Siendo los usuarios similares aquellos que aparecen mas veces en
	   los sucesivos caminos aleatorios."""
	listaord = obtener_lista_semejantes(grafo, userid)
	listafin = []
	for i in range(cantsimil):
		tupla = (listaord.pop())
		listafin.append(tupla[1])
	charf = ", ".join(listafin)
	print(charf)

def recomendar(grafo, userid, cantrecom):
	listaord = obtener_lista_semejantes(grafo, userid)
	total = len(listaord)
	listafin = []
	for i in range(total):
		tupla = listaord.pop()
		if not grafo.son_adyacentes(userid, tupla[1]):
			listafin.append(tupla[1])
			if len(listafin) == cantrecom:
				break
	charf = ", ".join(listafin)
	print(charf)

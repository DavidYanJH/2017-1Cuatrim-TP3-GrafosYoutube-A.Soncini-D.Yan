
import random
from heapq import heappush, heappop
import queue


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
	vertices = grafo.total_vertices()
	aristas = grafo.total_aristas()
	print("Cantidad de Vertices del Grafo: {}".format(vertices))
	print("Cantidad de Aristas del Grafo: {}".format(aristas))
	grado_promedio = aristas / vertices
	print("Promedio de Grado de Entrada de cada Vertice: {:.2f}".format(grado_promedio))
	print("Promedio de Grado de Salida de cada Vertice: {:.2f}".format(grado_promedio))
	max_arista = vertices * (vertices - 1) / 2
	densidad_relat = aristas / max_arista
	print("Densidad Relativa del Grafo: {:.2f}".format(densidad_relat))



def bfs_conexion(grafo, origen, visitados, antecesores, orden, destino):
	q = queue.Queue()
	q.put(origen)
	visitados[origen] = True
	while not q.empty():
		v = q.get()
		for w in grafo.get_adyacentes(v):
			if w not in visitados:
				q.put(w) 
				visitados[w] = True
				orden[w] = orden[v] + 1
				antecesores[w] = v
				if destino in visitados: return #Condicion de Corte en Caso Necesario


def distancia_stats(grafo, userid):
	#Inicializacion de las Variables Fundamentales a Utilizar en BFS
	visitados = {}
	antecesores = {}
	orden = {}
	antecesores[userid] = None
	orden[userid] = 0
	#BFS con un determinado Vertice/Usuario del Grafo
	bfs_conexion(grafo, userid, visitados, antecesores, orden, None)
	#Consigo la Maxima Distancia al Vertice/Usuario Origen
	max_distance = max(orden.values())
	#Inicializacion de una Lista Auxiliar, cuya funcion consiste en contabilizar
	#las cantidades de usuarios segun la distancia al Vertice/Usuario Origen 
	distance = [] 
	for i in range(max_distance + 1):
		distance.append(0)
	#Proceso de Contabilizar las cantidades de usuarios segun distancia al Origen
	for v in visitados:
		distance[orden[v]] += 1
	#Mensajes de Salida Estandar
	for i in range(1, max_distance + 1):
		print("Distancia {}: {} usuarios".format(i, distance[i]))	


def contactos_conexion(grafo, id_origen, id_destino):
	#Inicializacion de las Variables Fundamentales a Utilizar en BFS
	visitados = {}
	antecesores = {}
	orden = {}
	antecesores[id_origen] = None
	orden[id_origen] = 0
	#BFS de Camino Minimo desde usuario id_origen hacia usuario id_destino
	bfs_conexion(grafo, id_origen, visitados, antecesores, orden, id_destino)
	#Verifico la Existencia de Camino o Conexion entre Ambos Usuarios
	if id_destino in visitados:
		#Reconstruyo el Camino Minimo Hallado usando una LIFO.Queue/Pila
		p = queue.LifoQueue()
		actual = id_destino
		p.put(actual)
		for i in range(orden[actual]):
			actual = antecesores[actual]
			p.put(actual)
		#Doy Formato Necesario a la Salida	
		while not p.empty():
			actual = p.get()
			if not p.empty(): print("{}".format(actual), end = " --> ")
			else: print("{}\n".format(actual))
	else: print("Imposible Conectar Ambos Usuarios") #Caso sin Conexion		


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

def max_freq(grafo, comunidades, vertice):
	adyacentes = grafo.get_adyacentes(vertice)				# Obtengo lista de adyacentes de vertice actual
	aux = {}												# Diccionario temporal para almacenar contadores segun label
	aux_max = 0												# Contador de apariciones del label mas frecuente
	comunidad_max = ""										# Variable de retorno de label mas frecuente

	for adyacente in adyacentes:							# Por cada vertice adyacente al vertice actual...
		if comunidades[adyacente] not in aux:				# Si su label no esta en diccionario temporal...
			aux[comunidades[adyacente]] = 1					# Guardo label, con contador en 1 aparicion...
		else:
			aux[comunidades[adyacente]] += 1				# Si el label ya esta en diccionario temporal, incremento su contador de apariciones...
		if aux[comunidades[adyacente]] > aux_max:			# Si este label es mas frecuente que el maximo hasta ahora...
			aux_max = aux[comunidades[adyacente]]			# Guardo nuevo maximo...
			comunidad_max = comunidades[adyacente]			# Guardo nombre de comunidad con maxima frecuencia...
	return comunidad_max									# Retorno comunidad de maxima frecuencia...


def comunidades(grafo):
	comunidades = {}
	vertices = grafo.get_vertices()			# Obtengo todos los vertices del grafo en una lista
	random.shuffle(vertices)				# Rerodeno aleatoriamente
	
	for vertice in vertices:				# Por cada vertice del grafo...
		comunidades[vertice] = vertice 		# Cada vertice lleva inicialmente su propia label de comunidad.

	for i in range(20):						# Ciclos de iteracion, que dan la condicion de corte
		for vertice in vertices:				# Por cada vertice del grafo...
			comunidades[vertice] = max_freq(grafo, comunidades, vertice)			# Cambio label segun maxima frecuencia de labels en adyacentes
	
	aux = {}													# Creo diccionario de comunidades y miembros
	cant_comunidades = 0										# Contador de cantidad de comunidades
	for vertice in vertices:									# Por cada vertice del grafo original...
		if comunidades[vertice] not in aux:						# Si la comunidad del vertice actual no existe en el diccionario final...
			aux[comunidades[vertice]] = []						# Agrego nueva cmomunidad, con lista de miembros vacia
			aux[comunidades[vertice]].append(vertice)			# Agrego primer miembro de la comunidad
			cant_comunidades += 1								# Incremento contador de cantidad de comunidades
		else:
			aux[comunidades[vertice]].append(vertice)			# Si la cmunidad ya existe en diccionario final, agrego miembro
	
	print("Existen {} comunidades".format(cant_comunidades))	# Se imprime el total de comunidades
	
	for comunidad in aux:										# Se imprimen las comunidades y sus miembros, filtrando segun criterios de consigna
		cantidad_comunidad = len(aux[comunidad])
		if ((cantidad_comunidad > 5) and (cantidad_comunidad < 2000)):
			print("Comunidad {} tiene {} integrantes".format(comunidad, cantidad_comunidad))
			print("Integrantes: {}".format(aux[comunidad]))

			
def centralidad(grafo, n):
	vertices = grafo.get_vertices()			# Obtengo todos los vertices del grafo en una lista
	print("tengo vertices del grafo")
	centrales = {}
	total = 0
	for i in range(100):
		print("Ejecucion {}".format(i))
		v_inicial = random.choice(vertices)
		similares = obtener_lista_semejantes(grafo, v_inicial)
		
		for similar in similares:
			#print(similar[1])
			if similar[1] not in centrales:
				centrales[similar[1]] = 1
			else:
				centrales[similar[1]] += 1
	heap = []
	#Ingreso todos los valores en Heap
	for vertice in centrales:
		tupla = (centrales[vertice], vertice)
		heappush(heap, tupla)
		total += 1

	listaord = []
	#Heapsort
	for i in range(total):
		listaord.append(heappop(heap))
	listafin = []
	print("Usuarios centrales: ", end='')
	for usuario in range(n):
		tupla = listaord.pop()
		listafin.append(tupla[1])
	charf = ", ".join(listafin)
	print(charf)
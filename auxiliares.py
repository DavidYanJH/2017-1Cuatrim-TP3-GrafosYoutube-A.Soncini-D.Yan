
import random
from heapq import heappush, heappop
import queue


def cargar_grafo(grafo, archivo):
	print("Cargando archivo {}...".format(archivo))
	print("Aguarde unos instantes...")
	try:
		file = open(archivo, 'r')
	except IOError:
		print("Oops! Parece que {} no es un archivo existente. Abortando...".format(archivo))
		raise IOError

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
	print("\nArchivo cargado con exito!")


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


def grafo_stats(grafo, args):


	if len(args) != 1:
		print("Error. El comando no admite argumentos")
		return

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


def distancia_stats(grafo, args):

	if len(args) != 2:
		print("Error. El comando admite solo 1 argumento")
		return

	if not grafo.vertice_exist(args[1]):
		print("Error. El usuario {} es inexistente en la red.".format(args[1]))
		return
	userid = args[1]

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


def contactos_conexion(grafo, args):
	#Inicializacion de las Variables Fundamentales a Utilizar en BFS

	if len(args) != 3:
		print("Error. El comando admite solo 2 argumentos")
		return

	if not grafo.vertice_exist(args[1]):
		print("Error. El usuario {} es inexistente en la red.".format(args[1]))
		return
	id_origen = args[1]

	if not grafo.vertice_exist(args[2]):
		print("Error. El usuario {} es inexistente en la red.".format(args[2]))
		return
	id_destino = args[2]

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


def similares(grafo, args):
	"""Calcula la cantidad 'cantsimil' de usuarios semejantes a 'userid', 
	   Siendo los usuarios similares aquellos que aparecen mas veces en
	   los sucesivos caminos aleatorios."""	
	if len(args) != 3:
		print("Error. El comando admite solo 2 argumentos")
		return

	if not grafo.vertice_exist(args[1]):
		print("Error. El usuario {} es inexistente en la red.".format(args[1]))
		return
	userid = args[1]

	try:
		cantsimil = int(args[2])
	except ValueError:
		print("Error. '{}' no es un número entero".format(args[2]))
		return

	listaord = obtener_lista_semejantes(grafo, userid)
	listafin = []
	for i in range(cantsimil):
		tupla = (listaord.pop())
		listafin.append(tupla[1])
	charf = ", ".join(listafin)
	print(charf)


def recomendar(grafo, args):

	if len(args) != 3:
		print("Error. El comando admite solo 2 argumentos")
		return

	if not grafo.vertice_exist(args[1]):
		print("Error. El usuario {} es inexistente en la red.".format(args[1]))
		return
	userid = args[1]

	try:
		cantrecom = int(args[2])
	except ValueError:
		print("Error. '{}' no es un número entero".format(args[2]))
		return

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


def comunidades(grafo, args):

	if len(args) != 1:
		print("Error. El comando no admite argumentos")
		return

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

			
def centralidad(grafo, args):

	if len(args) != 2:
		print("Error. El comando admite solo 1 argumento")
		return

	try:
		n = int(args[1])
	except ValueError:
		print("Error. '{}' no es un número entero".format(args[1]))
		return

	vertices = grafo.get_vertices()								# Obtengo todos los vertices del grafo en una lista
	centrales = {}												# Creo diccionario de conteo de apariciones
	total = 0

	for i in range(100):										# Iteraciones suficientes para determinar centralidad. 
		v_inicial = random.choice(vertices)						# Elijo un vertice aleatorio
		temp = random_walks(grafo, v_inicial, 200000, 1)		# Hago caminata random de una porcion significativa del grafo
		caminata = temp[0]										# Guardo lista de vertices obtenida

		
		for paso in caminata:
			if paso not in centrales:
				centrales[paso] = 1
			else:
				centrales[paso] += 1
	heap = []
	for vertice in centrales:									# Ingreso todos los valores en Heap
		tupla = (centrales[vertice], vertice)					# Armo tupla con cantidad de ocurrencias de vertice y vertice
		heappush(heap, tupla)									# Guardo en heap
		total += 1												# Cuento total de operaciones

	listaord = []												# Heapsort
	for i in range(total):
		listaord.append(heappop(heap))							# Genero lista de tuplas ordenadas segun ocurrencias de vertices
	
	listafin = []												# Lista para guardar solo los n usuarios centrales solicitados
	print("Usuarios centrales: ", end='')
	
	for usuario in range(n):									# Armado de la lista con n usuarios centrales
		tupla = listaord.pop()
		listafin.append(tupla[1])

	listafin.sort()												# Sorts de acuerdo a la consiga
	listafin.sort(key=len)
	charf = ", ".join(listafin)									# Print final
	print(charf)

def ayuda(grafo, args):
	print("Ayuda de programa TP3 - Grafos en YouTube")
	print("")
	print("Comandos disponibles:")

	print("Similares: dado un usuario, encontrar los personajes más similares a este.")
	print("\tParámetros:")
	print("\t\tid: el id del usuario.")
	print("\t\tn: la cantidad de usuarios semejantes que se desea buscar.")
	print("\tSalida: los n usuarios más similares al indicado, ordenados de mayor a menor similaridad.")
	print("\tEjemplo:")
	print("\t\t> similares 1 5")
	print("\t\t> 20 22 21583 1219 3")
	print("")

	print("Recomendar: dado un usuario, recomendar otro (u otros) usuario con el cual aún no tenga relación, y sea lo más similar a él posible.")
	print("\tParámetros:")
	print("\t\tid: el id del usuario en cuestión.")
	print("\t\tn: la cantidad de usuarios a recomendar.")
	print("\tSalida: los n usuarios más similares al indicado, ordenados de mayor a menor similaridad.")
	print("\tEjemplo:")
	print("\t\t> recomendar 5 4")
	print("\t\t> 1072, 884, 29664, 29686")
	print("")

	print("Camino: queremos que un comunicado llegue lo más rápido posible de un usuario A a un usuario B. Sabemos que un usuario puede comunicar su mensaje solo a sus contactos directos, por lo que la mejor estrategia será pasar por la menor cantidad de usuarios posibles. Tener presente que es posible que el grafo tenga más de una componente conexa, por lo que pueden haber vértices entre los cuales no exista camino posible.")
	print("\tParámetros:")
	print("\t\tid1: el id del usuario de partida.")
	print("\t\tid2: el id del usuario de llegada.")
	print("\tSalida: camino más corto para llegar desde el usuario con id1 al usuario con id2.")
	print("\tEjemplo:")
	print("\t\t> camino 11 1991")
	print("\t\t> 11 -> 663545 -> 106 -> 1991")
	print("")

	print("Centralidad (o Betweeness): permite obtener los usuarios más centrales de la red. Los usuarios más centrales suelen ser a su vez los más importantes (o como se denomina en redes sociales, influyente).")
	print("\tParámetros:")
	print("\t\tn: la cantidad de usuarios que se desean mostrar.")
	print("\tSalida: los n usuarios más centrales de la red, ordenados de mayor a menor.")
	print("\tEjemplo:")
	print("\t\t> centralidad 3")
	print("\t\t> 83 663545 832")
	print("")

	print("Distancias: dado un usuario, obtener la cantidad de personajes que se encuentran a cada una de las distancias posibles, considerando las distancias como la cantidad de saltos.")
	print("\tParámetro:")
	print("\t\tid: el id del usuario al cuál se le desean obtener las distancias.")
	print("\tSalida:")
	print("\t\tDistancia 1: cantidad de usuarios adyacentes al usuario en cuestión.")
	print("\t\tDistancia 2: cantidad de usuarios a distancia 2 del usuario en cuestión.")
	print("\t\tetc.")
	print("\tEjemplo:")
	print("\t\t> distancias 9")
	print("\t\t> Distancia 1: 1")
	print("\t\t> Distancia 2: 28")
	print("\t\t> Distancia 3: 7147")
	print("\t\tetc.")
	print("")

	print("Estadísticas: muchas veces es de interés obtener ciertas estadísticas sobre las uniones del grafo. Nos interesa que nos muestre el total de vértices, el total de aristas, el promedio del grado de cada vértice y la densidad del grafo (la proporción entre la cantidad de aristas, y la cantidad de aristas máximas que puede llegar tener el grafo, con esa cantidad de vértices).")
	print("\tParámetros: (ninguno)")
	print("\tSalida:")
	print("\t\tCantidad de vértices.")
	print("\t\tCantidad de aristas.")
	print("\t\tPromedio del grado de entrada cada vértice.")
	print("\t\tPromedio del grado de salida cada vértice.")
	print("\t\tDensidad del grafo.")
	print("")
	print("Comunidades: nos permite mostrar las comunidades que se encuentren en la red. Recomendamos utilizar el algoritmo de Label Propagation descrito en la introducción de este trabajo práctico.")
	print("\tParámetros: (ninguno)")
	print("\tSalida: Por cada comunidad, la cantidad de integrantes, y un listado con los integrantes.")
	print("\tEjemplo:")
	print("\t\t> estadisticas")
	print("\t\t> Cantidad de vértices: 12")
	print("\t\t> Cantidad de aristas: 144")
	print("\t\t> Promedio de grado de entrada de cada vértice: 11")
	print("\t\t> Promedio de grado de salida de cada vértice: 11")
	print("\t\t> Densidad del grafo: 1")
	print("")

	print("Exit (salir del programa): Sale del programa")
	print("\tParámetros: (ninguno)")
	print("\tEjemplo:")
	print("\t\t> exit")






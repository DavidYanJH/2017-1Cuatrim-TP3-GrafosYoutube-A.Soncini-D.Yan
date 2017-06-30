from auxiliares import *

def similares(grafo, args):
	NUM_ARGUM = 3   
	if (len(args) != NUM_ARGUM):
		print("Error. El comando 'similares' admite solamente 2 argumentos")
		print("Mas informacion sobre el comando 'similares' utilice el comando 'ayuda'")
		return

	if not grafo.vertice_exist(args[1]):
		print("Error. El usuario {} es inexistente en la red.".format(args[1]))
		print("Mas informacion sobre el comando 'similares' utilice el comando 'ayuda'")
		return

	try:
		cantsimil = int(args[2])
	except ValueError:
		print("Error. La cantidad de usuarios similares a informar debe ser un numero entero mayor a 0")
		print("Mas informacion sobre el comando 'similares' utilice el comando 'ayuda'")
		return

	if (cantsimil <= 0):
		print("Error. La cantidad de usuarios similares a informar debe ser un numero entero mayor a 0")
		print("Mas informacion sobre el comando 'similares' utilice el comando 'ayuda'")
		return

	userid = args[1]
	listafin = get_lista_similares(grafo, userid, cantsimil)
	charf = ", ".join(listafin)
	print(charf)


def recomendar(grafo, args):
	NUM_ARGUM = 3
	if (len(args) != NUM_ARGUM):
		print("Error. El comando 'recomendar' admite solamente 2 argumentos")
		print("Mas informacion sobre el comando 'recomendar' utilice el comando 'ayuda'")
		return

	if not grafo.vertice_exist(args[1]):
		print("Error. El usuario {} es inexistente en la red.".format(args[1]))
		print("Mas informacion sobre el comando 'recomendar' utilice el comando 'ayuda'")
		return

	try:
		cantrecom = int(args[2])
	except ValueError:
		print("Error. La cantidad de usuarios a recomendar debe ser un numero entero mayor a 0")
		print("Mas informacion sobre el comando 'recomendar' utilice el comando 'ayuda'")
		return

	if (cantrecom <= 0):
		print("Error. La cantidad de usuarios a recomendar debe ser un numero entero mayor a 0")
		print("Mas informacion sobre el comando 'recomendar' utilice el comando 'ayuda'")
		return
	
	userid = args[1]	
	listaord = get_lista_similares(grafo, userid, 0)
	listafin = []
	for i in range(len(listaord)):
		if not grafo.son_adyacentes(userid, listaord[i]):
			listafin.append(listaord[i])
			if len(listafin) == cantrecom: break
	charf = ", ".join(listafin)
	print(charf)


def contactos_conexion(grafo, args): #Camino Minimo
	NUM_ARGUM = 3
	if (len(args) != NUM_ARGUM):
		print("Error. El comando 'camino' admite solamente 2 argumentos")
		print("Mas informacion sobre el comando 'camino' utilice el comando 'ayuda'")
		return

	if not grafo.vertice_exist(args[1]) or not grafo.vertice_exist(args[2]):
		if not grafo.vertice_exist(args[1]):
			print("Error. El usuario {} es inexistente en la red.".format(args[1]))
		if not grafo.vertice_exist(args[2]):
			print("Error. El usuario {} es inexistente en la red.".format(args[2]))
		print("Mas informacion sobre el comando 'camino' utilice el comando 'ayuda'")	
		return

	#Inicializacion de las Variables Fundamentales a Utilizar en BFS
	id_origen = args[1]
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



def centralidad(grafo, args):
	NUM_ARGUM = 2
	if (len(args) != NUM_ARGUM):
		print("Error. El comando 'centralidad' admite solamente 1 argumento")
		print("Mas informacion sobre el comando 'centralidad' utilice el comando 'ayuda'")
		return

	try:
		cantctral = int(args[1])
	except ValueError:
		print("Error. La cantidad de usuarios centrales a informar debe ser un numero entero mayor a 0")
		print("Mas informacion sobre el comando 'centralidad' utilice el comando 'ayuda'")
		return

	if (cantctral <= 0):
		print("Error. La cantidad de usuarios centrales a informar debe ser un numero entero mayor a 0")
		print("Mas informacion sobre el comando 'centralidad' utilice el comando 'ayuda'")	
		return

	listafin = get_lista_centrales(grafo, cantctral)
	charf = ", ".join(listafin)									# Print final
	print(charf)


def distancia_stats(grafo, args): #Distancias
	NUM_ARGUM = 2
	if (len(args) != NUM_ARGUM):
		print("Error. El comando 'distancias' admite y requiere un unico argumento")
		print("Mas informacion sobre el comando 'distancia' utilice el comando 'ayuda'")
		return

	if not grafo.vertice_exist(args[1]):
		print("Error. El usuario {} es inexistente en la red.".format(args[1]))
		print("Mas informacion sobre el comando 'distancia' utilice el comando 'ayuda'")
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


def grafo_stats(grafo, args): #Estadisticas
	NUM_ARGUM = 1
	if (len(args) != NUM_ARGUM):
		print("Error. El comando 'estadisticas' no admite argumento.")
		print("Mas informacion sobre el comando 'estadisticas' utilice el comando 'ayuda'")
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


def comunidades(grafo, args):
	NUM_ARGUM = 1
	if (len(args) != NUM_ARGUM):
		print("Error. El comando 'comunidades' no admite argumentos")
		print("Mas informacion sobre el comando 'comunidades' utilice el comando 'ayuda'")
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
			print("Integrantes: ", end='')
			charf = ", ".join(aux[comunidad])									# Print final
			print(charf)
			print("")



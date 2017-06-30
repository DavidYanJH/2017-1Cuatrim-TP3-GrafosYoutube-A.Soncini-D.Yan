import os
import random
import heapq
import queue


def cargar_grafo(grafo, archivo):
	print("Cargando archivo < {} >... Aguarde unos instantes...\n".format(archivo))
	if not os.path.isfile(archivo):
		print("Error al Abrir el Archivo < {} > con los Datos de la Red Social.\n".format(archivo))
		raise IOError
	try:
		file = open(archivo, 'r')
	except IOError:
		raise IOError

	linea = file.readline()
	linea = linea.rstrip("\n")

	while (linea != ''):
		if not (linea[0] == '#'): # IGNORAR LAS LINEAS DE COMENTARIO
			lista = linea.split("\t")
			v_actual = lista[0]
			grafo.add_vertice(v_actual)
			while (linea != '') and (v_actual == lista[0]):
				grafo.add_vertice(lista[1])
				grafo.add_arista(v_actual, lista[1])
				linea = file.readline()
				linea = linea.rstrip("\n")
				lista = linea.split("\t")
		else:
			linea = file.readline()
			linea = linea.rstrip("\n")
	file.close()
	print("Archivo cargado con exito!\n")



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



def get_lista_similares(grafo, userid, cantsimil):
	lista_walks = random_walks(grafo, userid, 10000, 100)
	
	dicc = {}
	for walk in lista_walks:
		for vertice in walk:
			if vertice in dicc: dicc[vertice] += 1
			else: dicc[vertice] = 1
	dicc.pop(userid)
	
	lista_inicial = []
	for user in dicc:
		lista_inicial.append((dicc[user], user))
	
	lista_total = []
	if cantsimil != 0: 
		lista_total = heapq.nlargest(cantsimil, lista_inicial) # HEAP DE MAXIMO TOP K = CANTSIMIL
	else: 
		lista_total = heapq.nlargest(len(lista_inicial), lista_inicial) # HEAPSORT DE MAXIMO
	
	lista_final = []
	for i in range(len(lista_total)):
		lista_final.append(lista_total[i][1])
	return lista_final



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



def get_lista_centrales(grafo, cantctral):
	vertices = grafo.get_vertices()								# Obtengo todos los vertices del grafo en una lista
	centrales = {}												# Creo diccionario de conteo de apariciones

	for i in range(100):										# Iteraciones suficientes para determinar centralidad. 
		v_inicial = random.choice(vertices)						# Elijo un vertice aleatorio de partida
		temp = random_walks(grafo, v_inicial, 200000, 1)		# Hago caminata random de una porcion significativa del grafo
		caminata = temp[0]										# Guardo lista de vertices obtenida
		for paso in caminata:
			if paso not in centrales:
				centrales[paso] = 1
			else:
				centrales[paso] += 1

	lista = []
	for vertice in centrales:								
		lista.append((centrales[vertice], vertice))

	lista = heapq.nlargest(cantctral, lista)                    # Heap de TOP K
	listafin = []
	for usuario in range(cantctral):							# Armado de la lista con n usuarios centrales
		listafin.append(lista[usuario][1])
	return listafin	



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



def ayuda_specific(menu, args):
	NUM_ARGUM = 2
	if (len(args) != 2 or args[1] not in menu):
		print("Argumento desconocido. Ayuda Imposible de Realizar...")
		return
	if (args[1] == "similares"):
		print("Similares: busca los usuarios más similares al usuario indicado.")
		print("\tParámetros Necesarios:")
		print("\t\tid: el id del usuario.")
		print("\t\tn: la cantidad de usuarios similares a listar.")
		print("\tSalida: un listado de n usuarios más similares al indicado, ordenados de mayor a menor similaridad.")
		print("\tEjemplo:")
		print("\t\t> similares 1 6")
		print("\t\t> 11 23 21338 1219 786")
		print("")
		return 
	if (args[1] == "recomendar"):
		print("Recomendar: recomienda usuario/s similar/es al usuario indicado, con el/los cual/es aún no tenga relación.")
		print("\tParámetros Necesarios:")
		print("\t\tid: el id del usuario indicado.")
		print("\t\tn: la cantidad de usuarios similares a recomendar.")
		print("\tSalida: un listado con los n usuarios más similares al indicado, ordenados de mayor a menor similaridad.")
		print("\tEjemplo:")
		print("\t\t> recomendar 3 8")
		print("\t\t> 1072, 883, 29663, 29686, 769, 2392, 80, 100")
		print("")
		return 
	if (args[1] == "camino"):
		print("Camino: informa un trayecto minimo tal que un comunicado llegue lo más rápido posible de un usuario A a un usuario B (a traves de contactos directos).")
		print("\tParámetros Necesarios:")
		print("\t\tid1: el id del usuario de partida.")
		print("\t\tid2: el id del usuario de llegada.")
		print("\tSalida: camino minimo desde el usuario con id1 al usuario con id2 en caso de existir uno.")
		print("\tEjemplo:")
		print("\t\t> camino 11 1991")
		print("\t\t> 11 -> 663535 -> 106 -> 1991")
		print("")
		return
	if (args[1] == "centralidad"):
		print("Centralidad (o Betweeness): informa un listado con una cantidad dada de los usuarios más centrales, importantes e influyentes en la red social.")
		print("\tParámetros Necesarios:")
		print("\t\tn: la cantidad de usuarios centrales a mostrar.")
		print("\tSalida: los n usuarios más centrales de la red, ordenados de mayor a menor centralidad.")
		print("\tEjemplo:")
		print("\t\t> centralidad 3")
		print("\t\t> 83 663869 832")
		print("")	
		return
	if (args[1] == "distancias"):
		print("Distancias: dado un usuario, informa la cantidad de usuarios que se encuentran a cada una de las distancias posibles.")
		print("\tParámetro Necesario:")
		print("\t\tid: el id del usuario al cual se desea obtener las distancias.")
		print("\tSalida:")
		print("\t\tDistancia 1: cantidad de usuarios adyacentes al usuario en cuestión.")
		print("\t\tDistancia 2: cantidad de usuarios a distancia 2 del usuario en cuestión.")
		print("\t\tetc.")
		print("\tEjemplo:")
		print("\t\t> distancias 9")
		print("\t\t> Distancia 1: 1")
		print("\t\t> Distancia 2: 28")
		print("\t\t> Distancia 3: 7147")
		print("\t\t> etc.")
		print("")
		return
	if (args[1] == "estadisticas"):
		print("Estadísticas: informa determinados estadísticos relevantes sobre las uniones del grafo de la red social.")
		print("\tParámetro: (ninguno)")
		print("\tEjemplo de Salida: ")
		print("\t\t> estadisticas")
		print("\t\t> Cantidad de vértices: 12")
		print("\t\t> Cantidad de aristas: 144")
		print("\t\t> Promedio de grado de entrada de cada vértice: 11")
		print("\t\t> Promedio de grado de salida de cada vértice: 11")
		print("\t\t> Densidad del grafo: 1")
		print("")
		return
	if (args[1] == "comunidades"):
		print("Comunidades: informa las distintas comunidades existentes en la red social.")
		print("\tParámetros: (ninguno)")
		print("\tSalida: Por cada comunidad, la cantidad de integrantes, y un listado con los integrantes.")
		print("\tEjemplo:")
		print("\t\t> comunidades")
		print("\t\t> Comunidad 386613 tiene 6 integrantes.")
		print("\t\t  Integrantes: 880540, 573868, 573867, 621437, 621436, 386613")
		print("\t\t> Comunidad 76283 tiene 8 integrantes")
		print("\t\t  Integrantes: 761998, 761997, 761995, 761996, 761999, 370028, 76283, 370027")
		print("\t\t> etc.")
		print("")
		return
	if (args[1] == "ayuda"):
		print("Ayuda: informa las caracteristicas especificas de un comando disponible del Programa")
		print("\tParametro: comando al cual se desea obtener la ayuda")
		print("\tSalida: los detalles del funcionamiento del comando indicado")
		print("\tEjemplo:")
		print("\t\t> ayuda comando")
		print("")
		return	
	if (args[1] == "?"):
		print("Acceso al Manual con la informacion detallada y especifica de todos los comandos disponibles del Programa")
		print("\tParametros: (ninguno)")
		print("\tEjemplo:")
		print("\t\t> ?")
		print("")
		return	
	if (args[1] == "exit"):
		print("Exit (Salir de la Ejecucion del Programa): Finaliza la Ejecucion del Programa")
		print("\tParámetros: (ninguno)")
		print("\tEjemplo:")
		print("\t\t> exit")
		print("")
		return


def ayuda_general(menu, args):
	NUM_ARGUM = 1
	if (len(args) != NUM_ARGUM):
		print("Error. El comando '?' no admite argumentos")
		return
	print("\t\t************AYUDA DEL PROGRAMA TP3 - YOUTUBE EN GRAFO*************\n")
	print("\t\t\t--------LISTADO DE LOS COMANDOS DISPONIBLES---------\n") 
	args.append("option")
	for option in menu:
		args[1] = option
		ayuda_specific(menu, args)



		
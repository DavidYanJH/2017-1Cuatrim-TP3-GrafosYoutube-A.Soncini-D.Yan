import random
import heapq

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

def similares(grafo, userid, cantsem, lista_walks):
	print(type(lista_walks))
	diccionario = {}
	largo = len(lista)

	for i in range(largo):
		print(lista[i])
	print("")

	for caminos in lista_walks:
		for vertice in caminos:
			if vertice in diccionario:
				diccinario[vertice] +=1
			else:
				diccionario[vertice] = 0
	heap = []
	cont = 0
	for user in diccionario:
		tupla = (diccionario[user], user)
		if cont < cantsem:
			heappush(heap, tupla)
		else:
			heappushpop(heap, tupla)

	listaord = []
	for i in range(cantsem):
		listaord.append(heappop(heap))

	print("Similares: ", end='')
	for i in range(cantsem):
		tupla = (listaord.pop())
		print("{} ".format(tupla[1]), end='')
	print(".")
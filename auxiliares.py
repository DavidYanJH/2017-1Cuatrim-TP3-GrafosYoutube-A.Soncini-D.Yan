import random
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

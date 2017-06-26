import heapq

def get_lista_similares(grafo, userid, cantsimil):
	lista_walks = random_walks(grafo, userid, 10000, 200)
	
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
		lista_total = heapq.nlargest(cantsimil, lista_inicial)
	else: 
		lista_total = heapq.nlargest(len(lista_inicial), lista_inicial)
	
	lista_final = []
	for i in range(len(lista_total)):
		lista_final.append(lista_total[i][1])
	return lista_final	
			
		
def similares(grafo, userid, cantsimil):
	"""Calcula la cantidad 'cantsimil' de usuarios similares al usuario 'userid'. 
	   Siendo usuarios similares aquellos con mayor cantidad de apariciones en
	   los sucesivos caminos aleatorios o random walks."""
	listafin = get_lista_similares(grafo, userid, cantsimil)
	charf = ", ".join(listafin)
	print(charf)


def recomendar(grafo, userid, cantrecom):
	listaord = get_lista_similares(grafo, userid, 0)
	listafin = []
	for i in range(len(listaord)):
		if not grafo.son_adyacentes(userid, listaord[i]):
			listafin.append(listaord[i])
			if len(listafin) == cantrecom: break
	charf = ", ".join(listafin)
	print(charf)

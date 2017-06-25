from heapq import heapify, heappop

def get_lista_semejantes(grafo, userid):
	lista_walks = random_walks(grafo, userid, 20000, 100)
	dicc = {}
	for walk in lista_walks:
		for vertice in walk:
			if vertice in dicc: dicc[vertice] += 1
			else: dicc[vertice] = 1
	dicc.pop(userid)		
	lista_total = []
	for user in dicc:
		lista_total.append((dicc[user], user))
	heapify(lista_total) 
	lista_final = []
	total = len(lista_total)
	for i in range(total):
		lista_final.append(heappop(lista_total))	
	return lista_final
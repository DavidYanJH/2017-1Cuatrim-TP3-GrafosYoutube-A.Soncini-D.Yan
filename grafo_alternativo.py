import random

class Grafo:
	def __init__(self):
		""" Inicializacion del objeto Grafo No Dirigido No Pesado.
			Se inicializa como un diccionario vacio con 
				vertices como claves y listas de adyacencia como dato asociado.
			Se inicializa con cantidad total de vertices en cero.
			Se inicializa con cantidad total de aristas en cero.
		"""
		self.grafo = {}
		self.vertices = 0
		self.aristas = 0

	
	def vertice_exist(self, vertice):
		return vertice in self.grafo

	def add_vertice(self, vertice):
		if not self.vertice_exist(vertice):
			self.grafo[vertice] = []
			self.vertices +=1
			return True
		return False	

	def remove_vertice(self, vertice):
		if self.vertice_exist(vertice):
			for adyacente in self.grafo.pop(vertice):
				self.grafo[adyacente].remove(vertice)
				self.aristas -=1	
			self.vertices -=1

		
	def get_vertices(self):
		"""Retorna una lista desordenada de todos los vertices del grafo"""
		return self.grafo.keys()


	def add_arista(self, verticeA, verticeB):
		if verticeA in self.grafo and verticeB in self.grafo:
			if not self.son_adyacentes(verticeA, verticeB):
				self.grafo[verticeB].append(verticeA)
				self.grafo[verticeA].append(verticeB)
				self.aristas +=1
				return True
		return False		


	def remove_arista(self, verticeA, verticeB):
		if verticeA in self.grafo and verticeB in self.grafo:
			if self.son_adyacentes(verticeA, verticeB):
				self.grafo[verticeA].remove(verticeB)
				self.grafo[verticeB].remove(verticeA)
				self.aristas -=1


	def get_adyacentes(self, vertice):
		if self.vertice_exist(vertice):
			return self.grafo[vertice]
		return None

	def son_adyacentes(self, verticeA, verticeB):
		adyacentes = self.get_adyacentes(verticeA)
		if verticeB in adyacentes:
			return True
		return False


	def random_walks(self, v_inicial, lenght_walk, total_walk):
		"""Realiza una serie de random walks o recorridos aleatorios en el grafo dado.
		   la variable total_walk determina la cantidad de recorridos a realizar;
		   la variable lenght_walk determina la longitud de cada recorrido aleatorio;
		   la variable v_inicial determina el vertice de partida de cada recorrido:
		   si v_inicial is None entonces los recorridos partiran desde cualquier
		   vertice aleatorio del grafo dado, en cambio si v_inicial is not None y existe
		   en el grafo dado entonces sera el vertice de partida.
		   La funcion random_walks retorna una lista con los recorridos aleatorios realizados
		   en forma de listas de vertices, en caso de error retorna un None."""
		if v_inicial is not None and not self.vertice_exist(v_inicial): return None
		if lenght_walk <= 1 or total_walk <= 0: return None    
		   
		lista_walks = []
		
		if v_inicial is not None and self.vertice_exist(v_inicial):
			for i in range(total_walk):
				walk = []
				walk.append(v_inicial)
				v_actual = v_inicial
				for j in range(1, lenght_walk):
					ady_actual = self.get_adyacentes(v_actual)
					v_actual = random.choice(ady_actual)
					walk.append(v_actual)
				lista_walks.append(walk)
			return lista_walks
		
		if v_inicial is None:
			vertices = self.get_vertices()
			for i in range(total_walk):
				v_inicial = random.choice(vertices)
				walk = []
				walk.append(v_inicial)
				v_actual = v_inicial
				for j in range(1, lenght_walk):
					ady_actual = self.get_adyacentes(v_actual)
					v_actual = random.choice(ady_actual)
					walk.append(v_actual)	
				lista_walks.append(walk)
			return lista_walks		



def main():
	"""********************************Simple Test*****************************"""
	print("Simple Test de las diferentes funciones del Grafo")
	grafo = Grafo()
	print("")
	print("Un grafo vacio ha sido creado exitosamente")
	print("El grafo vacio tiene {} vertices".format(grafo.vertices))
	print("El grafo vacio tiene {} aristas".format(grafo.aristas))
	print("")

	print("Insercion de los vertices 0, 1, 2, 3, 4, 5, 6, 7, 8, 9")
	grafo.add_vertice(0)
	grafo.add_vertice(1)
	grafo.add_vertice(2)
	grafo.add_vertice(3)
	grafo.add_vertice(4)
	grafo.add_vertice(5)
	grafo.add_vertice(6)
	grafo.add_vertice(7)
	grafo.add_vertice(8)
	grafo.add_vertice(9)
	print("El grafo tiene {} vertices despues de la insercion".format(grafo.vertices))
	print("El grafo tiene {} aristas despues de la insercion".format(grafo.aristas))
	print("Los vertices existentes en el grafo son:")
	lista = grafo.get_vertices() 
	for vertice in lista:
		print("Vertice {}".format(vertice))
	print("")

	print("Agrego aristas de 0 a 1, 2, 3, 8")
	grafo.add_arista(0, 1)
	grafo.add_arista(0, 2)
	grafo.add_arista(0, 3)
	grafo.add_arista(0, 8)
	print("El grafo tiene {} aristas actualmente".format(grafo.aristas))
	print("Agrego aristas de 1 a 2, 3")
	grafo.add_arista(1, 2)
	grafo.add_arista(1, 3)
	print("El grafo tiene {} aristas actualmente".format(grafo.aristas))
	print("v1 y v0 son adyacentes entre si {}".format(grafo.son_adyacentes(1, 0)))
	print("v0 y v8 son adyacentes entre si {}".format(grafo.son_adyacentes(0, 8)))
	print("v2 y v3 no son adyacentes entre si {}".format(not grafo.son_adyacentes(2, 3)))
	print("")
	
	adyacentes = grafo.get_adyacentes(0)
	for vertice in adyacentes:
		print("Vertice 0 tiene como adyacentes a {}".format(vertice))
	print("")
	
	adyacentes = grafo.get_adyacentes(1)
	for vertice in adyacentes:
		print("Vertice 1 tiene como adyacentes a {}".format(vertice))
	print("")
		
	adyacentes = grafo.get_adyacentes(9)
	if len(adyacentes) == 0 : 
		print("El vertice 9 no tiene ningun adyacente actualmente")	
		print("")

	print("Elimino el arista entre 1 y 0")
	grafo.remove_arista(1, 0)
	print("v1 y v0 ya no son adyacentes entre si {}".format(not grafo.son_adyacentes(0, 1)))
	print("Ahora el grafo aun tiene {} aristas".format(grafo.aristas))
	print("Elimino el arista entre 0 y 8")
	grafo.remove_arista(0, 8)
	print("v0 y v8 ya no son adyacentes entre si {}".format(not grafo.son_adyacentes(0, 8)))
	print("Ahora el grafo aun tiene {} aristas".format(grafo.aristas))		
	print("")

	print("Elimino el vertice 0 del grafo")
	grafo.remove_vertice(0)
	print("El vertice 0 ya no existe en el grafo {}".format(not grafo.vertice_exist(0)))
	print("El grafo tiene {} aristas despues de eliminar el vertice 0".format(grafo.aristas))
	print("Elimino el vertice 1 del grafo")
	grafo.remove_vertice(1)
	print("El vertice 1 ya no existe en el grafo {}".format(not grafo.vertice_exist(1)))
	print("El grafo tiene {} aristas despues de eliminar el vertice 1".format(grafo.aristas))
	print("")

	print("Agrego al grafo el vertice 1 nuevamente")
	grafo.add_vertice(1)
	print("Agrego al grafo el vertice 0 nuevamente")
	grafo.add_vertice(0)
	print("Nuevamente el grafo tiene los {} vertices orginales".format(grafo.vertices))
	print("El grafo tiene ahora {} aristas".format(grafo.aristas))
	print("")

	print("Agrego aristas al grafo con 10 vertices")
	print("Agrego 4 aristas de 0 a 1, 2, 3, 8")
	grafo.add_arista(0, 1)
	grafo.add_arista(0, 2)
	grafo.add_arista(0, 3)
	grafo.add_arista(0, 8)
	print("El grafo ahora tiene {} aristas".format(grafo.aristas))
	print("Agrego 2 aristas de 1 a 2, 3")
	grafo.add_arista(1, 2)
	grafo.add_arista(1, 3)
	print("El grafo ahora tiene {} aristas".format(grafo.aristas))
	print("Agrego 1 arista entre 2 y 3")
	grafo.add_arista(2, 3)
	print("El grafo ahora tiene {} aristas".format(grafo.aristas))
	print("Agrego 3 aristas de 3 a 4, 6, 8")
	grafo.add_arista(3, 4)
	grafo.add_arista(3, 6)
	grafo.add_arista(3, 8)
	print("Agrego 1 arista entre 4 y 5")
	grafo.add_arista(4, 5)
	print("El grafo ahora tiene {} aristas".format(grafo.aristas))
	print("Agrego 1 arista entre 5 y 6")
	grafo.add_arista(5, 6)
	print("El grafo ahora tiene {} aristas".format(grafo.aristas))
	print("Agrego 3 aristas de 6 a 7, 8, 9")
	grafo.add_arista(6, 7)
	grafo.add_arista(6, 8)
	grafo.add_arista(6, 9)
	print("El grafo ahora tiene {} aristas".format(grafo.aristas))
	print("Agrego 1 arista entre 7 y 8")
	grafo.add_arista(7, 8)
	print("El grafo ahora tiene {} aristas".format(grafo.aristas))
	print("Agrego 1 arista entre 8 y 9")
	grafo.add_arista(8, 9)
	print("El grafo finalmente tiene {} aristas".format(grafo.aristas))
	print("")

	"""********************************Random Walks Test*****************************"""
	print("Test Simple de Random_Walks\n")
	print("3 random walks de longitud 6 desde el vertice 0")
	lista_walks = grafo.random_walks(0, 9, 3)
	for i in range(3):
		print(lista_walks[i])
	print("")	
	print("8 random walks de longitud 6 desde un vertice aleatorio")
	lista_walks = grafo.random_walks(None, 6, 8)
	for i in range(8):
		print(lista_walks[i])
	print("")

	print("Test de Casos Bordes de Random Walks\n")
	print("3 random walks de longitud 9 desde el vertice 11")
	lista_walks = grafo.random_walks(11, 9, 3)
	if lista_walks is None:
		print("None ya que el vertice 11 no existe en el grafo\n")
	print("3 random walks de longitud 1 desde un vertice aleatorio")	
	lista_walks = grafo.random_walks(None, 1, 3)
	if lista_walks is None:
		print("None ya que la longtitud de cada camino es menor igual a 1\n")
	print("0 random walks de longitud 3 desde un vertice aleatorio")	
	lista_walks = grafo.random_walks(None, 3, 0)
	if lista_walks is None:	
		print("None ya que la cantidad de random walks a realizar es 0\n")			

main()
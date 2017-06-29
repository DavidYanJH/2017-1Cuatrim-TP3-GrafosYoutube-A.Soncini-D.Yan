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

	
	def total_vertices(self):
		return self.vertices


	def total_aristas(self):
		return self.aristas	


	def __iter__(self):
		return iter(self.grafo.keys())	

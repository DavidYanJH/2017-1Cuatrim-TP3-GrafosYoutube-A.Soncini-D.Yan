
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


def main():
	grafo = Grafo()

	print("Inserto los vertices 1,2,3,4")
	grafo.add_vertice(1)
	grafo.add_vertice(2)
	grafo.add_vertice(3)
	grafo.add_vertice(4)
	print("El grafo tiene {} vertices".format(grafo.vertices))
	print("El grafo tiene {} aristas".format(grafo.aristas))

	print("Los vertices existentes en el grafo son:")
	lista = grafo.get_vertices() 
	for vertice in lista:
		print("Vertice {}".format(vertice))

	print("Elimino el vertice 3")
	grafo.remove_vertice(3)
	print("El grafo tiene {} vertices".format(grafo.vertices))
	print("Elimino el vertice 4")
	grafo.remove_vertice(4)
	print("El grafo tiene {} vertices".format(grafo.vertices))

	print("Agrego nuevamente los vertices 3 y 4")
	grafo.add_vertice(3)
	grafo.add_vertice(4)
	print("El grafo tiene {} vertices".format(grafo.vertices))

	print("Se agregan aristas de 1 a 2, 3, 4")
	grafo.add_arista(1, 2)
	grafo.add_arista(1, 3)
	grafo.add_arista(1, 4)
	print("El grafo tiene {} aristas".format(grafo.aristas))


	print("Se quita vertice 1")
	grafo.remove_vertice(1)
	print("El grafo tiene {} aristas".format(grafo.aristas))

	print("Se agregar vertice 1 nuevamente")
	grafo.add_vertice(1)
	print("El grafo tiene {} vertices".format(grafo.vertices))
	print("El grafo tiene {} aristas".format(grafo.aristas))
	print("Se agregan aristas de 1 a 2, 3, 4")
	grafo.add_arista(1, 2)
	grafo.add_arista(1, 3)
	grafo.add_arista(1, 4)
	print("El grafo tiene {} aristas".format(grafo.aristas))

	print("Se quita el arista 1-4")
	grafo.remove_arista(1, 4)
	print("El grafo tiene {} aristas".format(grafo.aristas))
	print("v1 y v4 no son adyacentes {}".format(not grafo.son_adyacentes(1,4)))

	adyacentes = grafo.get_adyacentes(1)
	for vertice in adyacentes:
		print("Vertice 1 tiene como adyacente a {}".format(vertice))

	adyacentes = grafo.get_adyacentes(2)
	for vertice in adyacentes:
		print("Vertice 2 tiene como adyacente a {}".format(vertice))


	print("Se quita vertice 1")
	grafo.remove_vertice(1)
	print("El vertice 1 ya no existe en el grafo {}".format(not grafo.vertice_exist(1)))


	adyacentes = grafo.get_adyacentes(2)
	print("La cantidad de adyacentes del vertice 2 es {}".format(len(adyacentes)))
main()
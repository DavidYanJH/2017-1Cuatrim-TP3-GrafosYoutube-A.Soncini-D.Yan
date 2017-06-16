class Grafo:
	def __init__(self):
		""" Inicializa el objeto Grafo.
			Se inicializa con un diccionario vacio
			Se inicializa con cantidad de vertices en cero
			Se inicializa con cantidad de aristas en cero
		"""
		self.__grafo_hash = {}
		self.vertices = 0
		self.aristas = 0

	def vertice_existe(self, vertice):
		return vertice in self.__grafo_hash

	def obtener_vertices(self):
		"""Devuelve una lista desordenada de vertices del grafo"""
		return list(self.__grafo_hash.keys())

	def obtener_vertces_ord(self):
		"""Devuelve una lista ordenada de vertices del grafo"""
		return sorted(self.obtener_vertices())

	def obtener_aristas(self):
		"""Devuelve una lista de las aristas existentes en el grafo"""
		return self.__generar_aristas()

	def agregar_vertice(self, vertice):
		""" Agrega una arista al grafo si la arista no existe
			Si la arista ya exite, se muestra mensaje de errro.
		"""
		if not self.vertice_existe(vertice):
			self.__grafo_hash[vertice] = []
			self.vertices +=1
		else:
			print("Ya existe el vertice. Imposible agregar")

	def quitar_vertice(self, vertice):
		for adyacente in self.__grafo_hash[vertice]:
			self.__grafo_hash[adyacente].remove(vertice)
			self.aristas -=1
		self.vertices -=1
		return self.__grafo_hash.pop(vertice)

	def agregar_arista(self, verticea, verticeb):
		if verticea not in self.__grafo_hash[verticeb]:
			self.__grafo_hash[verticeb].append(verticea)
			self.__grafo_hash[verticea].append(verticeb)
			self.aristas +=1
		else:
			print("Ya existe arista entra {} y {}".format(verticea, verticeb))

	def quitar_arista(self, verticea, verticeb):
		if verticea not in self.__grafo_hash[verticeb]:
			print("No existe arista entra {} y {}".format(verticea, verticeb))
		else:
			self.__grafo_hash[verticea].remove(verticeb)
			self.__grafo_hash[verticeb].remove(verticea)
			self.aristas -=1

	def obtener_adyacentes(self, vertice):
		if vertice not in self.__grafo_hash:
			print("No existe vertice {}".format(vertice))
		else:
			return list(self.__grafo_hash[vertice])

	def son_adyacentes(self, verticea, verticeb):
		adyacentes = self.obtener_adyacentes(verticea)
		if verticeb in adyacentes:
			return True
		else:
			return False

	def __generar_aristas(self):
		""" Se utilizan sets para representar las aristas y no tuplas
			La razon de esta eleccion es porque el grafo es no dirigido
			y una arista puede presentarse como a-b o b-a. En este caso
			seria la misma arista. Para el caso del set, la comparacion in
			dara un resultado true si comparamos una representacion con la 
			otra. Si fuera una tupla, no.
		"""
		aristas = []
		for vertice in self.__grafo_hash:
			for adyacente in self.__grafo_hash[vertice]:
				if {vertice, adyacente} not in aristas:
					aristas.append({vertice, adyacente})
		return aristas



def main():
	grafo = Grafo()

	grafo.agregar_vertice(1)
	grafo.agregar_vertice(2)
	grafo.agregar_vertice(3)
	grafo.agregar_vertice(4)

	print("El grafo tiene {} vertices".format(grafo.vertices))
	print("El grafo tiene {} aristas".format(grafo.aristas))

	grafo.quitar_vertice(4)
	print("El grafo tiene {} vertices".format(grafo.vertices))
	grafo.quitar_vertice(3)
	print("El grafo tiene {} vertices".format(grafo.vertices))

	grafo.agregar_vertice(3)
	grafo.agregar_vertice(4)
	print("El grafo tiene {} vertices".format(grafo.vertices))

	print("Se agregan aristas de 1 a 2, 3, 4")
	grafo.agregar_arista(1, 2)
	grafo.agregar_arista(1, 3)
	grafo.agregar_arista(1, 4)
	print("El grafo tiene {} aristas".format(grafo.aristas))

	aristas = grafo.obtener_aristas()
	for arista in aristas:
		print("-".join(str(e) for e in arista))

	print("Se quita vertice 1")
	grafo.quitar_vertice(1)

	print("El grafo tiene {} aristas".format(grafo.aristas))
	aristas = grafo.obtener_aristas()
	for arista in aristas:
		print("-".join(str(e) for e in arista))

	print("Se agregar vertice 1 nuevamente")
	grafo.agregar_vertice(1)
	print("El grafo tiene {} vertices".format(grafo.vertices))
	print("El grafo tiene {} aristas".format(grafo.aristas))
	print("Se agregan aristas de 1 a 2, 3, 4")
	grafo.agregar_arista(1, 2)
	grafo.agregar_arista(1, 3)
	grafo.agregar_arista(1, 4)
	print("El grafo tiene {} aristas".format(grafo.aristas))

	adyacentes = grafo.obtener_adyacentes(1)
	for vertice in adyacentes:
		print("Vertice 1 tiene como adyacente a {}".format(vertice))

	adyacentes = grafo.obtener_adyacentes(2)
	for vertice in adyacentes:
		print("Vertice 2 tiene como adyacente a {}".format(vertice))


	print("Se quita vertice 1")
	grafo.quitar_vertice(1)

	adyacentes = grafo.obtener_adyacentes(1)

	adyacentes = grafo.obtener_adyacentes(2)
	for vertice in adyacentes:
		print("Vertice 2 tiene como adyacente a {}".format(vertice))

	print("Se agregar vertice 1 nuevamente")
	grafo.agregar_vertice(1)
	print("El grafo tiene {} vertices".format(grafo.vertices))
	print("El grafo tiene {} aristas".format(grafo.aristas))
	print("Se agregan aristas de 1 a 2, 3, 4")
	grafo.agregar_arista(1, 2)
	grafo.agregar_arista(1, 3)
	grafo.agregar_arista(1, 4)
	adyacentes = grafo.obtener_adyacentes(3)
	for vertice in adyacentes:
		print("Vertice 3 tiene como adyacente a {}".format(vertice))

	print("Se quita arista entre 1 y 3")
	grafo.quitar_arista(1, 3)
	adyacentes = grafo.obtener_adyacentes(3)
	#Observar que este for no imprime nada.
	for vertice in adyacentes:
		print("Vertice 3 tiene como adyacente a {}".format(vertice))

	adyacentes = grafo.obtener_adyacentes(1)
	for vertice in adyacentes:
		print("Vertice 1 tiene como adyacente a {}".format(vertice))

	ady = grafo.son_adyacentes(1, 3)
	print("Vertices 1 y 3 son adyacentes: {}".format(ady))

	ady = grafo.son_adyacentes(1, 2)
	print("Vertices 1 y 2 son adyacentes: {}".format(ady))

	existe = grafo.vertice_existe(1)
	print("Vertice 1 existe: {}".format(existe))
	existe = grafo.vertice_existe(40)
	print("Vertice 40 existe: {}".format(existe))
main()
class NodoLS():
	def __init__(self):
		self.palabra=None
		self.indice=0
		self.siguiente=None

class Lista():
	def __init__(self):
		self.raiz=None
		self.ultimo=None
		self.indice=0

	def insertar(self, palabra):
		nodo = NodoLS()
		nodo.palabra=palabra
		if self.raiz==None:
			self.raiz=nodo
			self.ultimo=self.raiz
		else:
			nodo.indice = self.ultimo.indice+1
			self.ultimo.siguiente=nodo
			self.ultimo=self.ultimo.siguiente

	def borrar(self,palabra):
		if self.raiz!=None:
			aux = self.raiz
			if aux.palabra==palabra:
				if aux.siguiente==None:
					self.raiz=None
					self.ultimo=None
					return True
				else:
					aux=aux.siguiente
					return True
			while aux.siguiente!=None:
				temp=aux
				aux=aux.siguiente
				if aux.palabra==palabra:
					temp.siguiente=aux.siguiente
					return True
			return False
		else:
			return False

	def consultar(self,palabra):
		aux=self.raiz
		if aux.palabra==palabra:
			return aux.indice
		while aux.siguiente!=None:
			aux=aux.siguiente
			if aux.palabra==palabra:
				return aux.indice
		return -1








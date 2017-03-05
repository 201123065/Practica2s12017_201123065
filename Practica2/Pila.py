class NodoPila():
	def __init__(self):
		self.valor=0
		self.siguiente=None

class Pila():
	def __init__(self):
		self.tope=None
		self.base=None

	def push(self,valor):
		Npila = NodoPila()
		Npila.valor=valor
		if self.tope==None:
			self.tope=Npila
			self.base=self.tope
		else:
			self.tope.siguiente=Npila
			self.tope=self.tope.siguiente

	def pop(self):
		if self.base==None:
			return "no existe "
		elif self.base.siguiente==None:
			tmp = self.base.valor
			self.base=None
			self.tope=None
			return str(tmp)
		else:
			tmp = self.base
			while tmp.siguiente!=self.tope:
				tmp=tmp.siguiente
			temporal = str(self.tope.valor)
			tmp.siguiente=None
			self.tope=tmp
			return temporal



			




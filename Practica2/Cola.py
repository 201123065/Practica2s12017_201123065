class NodoCola():
	def __init__(self):
		self.valor=0
		self.siguiente=None

class Cola():
	def __init__(self):
		self.tope=None
		self.base=None

	def queque(self,valor):
		Ncola = NodoCola()
		Ncola.valor=valor
		if self.tope==None:
			self.tope=Ncola
			self.base=self.tope
		else:
			self.tope.siguiente=Ncola
			self.tope=self.tope.siguiente

	def dequeque(self):
		if self.base==None:
			return "esta vacio"
		else:
			tmp = self.base.valor
			if self.base.siguiente==None:
				self.base=None
				self.tope=None
			else:
				self.base=self.base.siguiente
			return str(tmp)

	def plotCola(self):
		if self.base!=None:
			tmp = self.base
			cad = " "
			if tmp.siguiente==None:
				return str(self.base.valor)+";"
			while tmp.siguiente!=None:
				cad = cad +"\n"+str(tmp.valor)+"->"+str(tmp.siguiente.valor)+";"
				tmp = tmp.siguiente
			return cad

		return " "


			




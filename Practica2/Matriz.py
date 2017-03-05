class NodoMatriz():
	def __init__(self):
		self.titulo=None
		self.abajo=None
		self.arriba=None
		self.derecha=None
		self.profundo=None


class Matriz():
	def __init__(self):
		self.raiz=None
		self.NodoDominio=None
		self.NodoLetra=None
	def agregar(self,usuario):
		# user@dom.com
		cad= usuario.split("@")
		# cad[0] user cad[1]=dom.com
		NODODOMINIO=NodoMatriz()
		# NODODOMINIO=[]
		NODODOMINIO.titulo=cad[1]
		# NODODOMINIO=[titulo=dom.com]
		NODOLETRA=NodoMatriz()
		# NODOLETRA=[]
		NODOLETRA.titulo=usuario[0]
		# NODOLETRA=[titulo=u]
		NODORAIZ=NodoMatriz()
		# NODORAIZ=[]
		NODORAIZ.titulo=usuario
		# NODORAIZ=[titulo=user@dom.com]
		if self.raiz==None:
			# si esta vacio
			self.raiz=NodoMatriz()
			#SELF:raiz=[]
			self.raiz.derecha=NODODOMINIO
			#SELF:raiz[derecha=NODODOMINIO[titulo=dom.com]]
			self.raiz.abajo=NODOLETRA
			#SELF:raiz[derecha=NODODOMINIO[titulo=dom.com], abajo=NODOLETRA[titulo=u]]
			NODODOMINIO.abajo=NODORAIZ
			# NODODOMINIO=[titulo=dom.com, abajo=NODORAIZ[titulo=user@dom.com]]
			NODOLETRA.derecha=NODORAIZ
			# NODOLETRA=[titulo=u,derecha=NODORAIZ[titulo=user@dom.com]]
			return True
		else:
			#posee al menos 1 dato
			punteroDominio=self.raiz
			# punteroDominio=[derecha=NODODOMINIO,abajo=NODOLETRA]
			punteroLetra=self.raiz
			# punteroLetra=[derecha=NODODOMINIO,abajo=NODOLETRA]
			while punteroLetra.abajo!=None:
				# consulta si existe la letra
				punteroLetra=punteroLetra.abajo
				# asigna el punteroLetra como el de abajo
				while punteroLetra.derecha!=None:
					# evalua si existe el nodo a la derecha
					punteroLetra=punteroLetra.derecha
					# asigna el valor del puntero al nodo
					if punteroLetra.titulo.split("@")[1]==cad[1]:
						# no solo se encontro que existe la letra, sino tambien el dominio
						while punteroLetra.profundo!=None:
							# mientras no se encuentre lo profundo de la lista
							punteroLetra=punteroLetra.profundo
						# se llego a lo mas profundo de la lista anidada
						punteroLetra.profundo=NODORAIZ
						# se llego a lo mas profundo, y se guarda alli
						return True
				# existia la letra, mas no el dominio
				punteroLetra.derecha=NODORAIZ
				# no existe el nodo a la derecha: o no existe el dominio, o no con esa letra
				while punteroDominio.derecha!=None:
					# ahora: a buscar si existe el dominio
					punteroDominio=punteroDominio.derecha
					# asigna al puntero derecho
					if punteroDominio.titulo==cad[1]:
						# si existe el dominio
						while punteroDominio.abajo!=None:
							# mientras el valor de abajo exista
							punteroDominio=punteroDominio.abajo
						punteroDominio.abajo=NODORAIZ
						return True
				# no existe el dominio, a crearlo
				punteroDominio.derecha=NODODOMINIO
				NODODOMINIO.abajo=NODORAIZ
				return True
			# no existe la letra, a crearla
			punteroLetra.abajo=NODOLETRA
			NODOLETRA.derecha=NODORAIZ
			# ahora a verificar si existe el dominio
			while punteroDominio.derecha!=None:
				# mientras hayan punteros derechos
				punteroDominio=punteroDominio.derecha
				if punteroDominio.titulo==cad[1]:
					# verificar si el puntero dominio es similar a la cadena ingresada
						


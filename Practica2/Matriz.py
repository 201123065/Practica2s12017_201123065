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
			print "matriz creada"
			return True
		else:
			print "ya tiene al menos uno uno"
			punteroDominio=self.raiz
			punteroLetra=self.raiz
			print "comprobando la existencia del nodo letra"
			while punteroLetra.abajo!=None:
				punteroLetra=punteroLetra.abajo
				if punteroLetra.titulo==usuario[0]:
					print "el nodo coincide con la letra del usuario"
					while punteroLetra.derecha!=None:
						punteroLetra=punteroLetra.derecha
						if punteroLetra.titulo.split("@")[1]==cad[1]:
							print " existe el dominio, a indexarlo"
							while punteroLetra.profundo!=None:
								punteroLetra = punteroLetra.profundo
							punteroLetra.profundo=NODORAIZ
							"perfectamente indexado"
							return True
					print "no existe relacion letra-dominio, consultando por dominio"
					while punteroDominio.derecha!=None:
						punteroDominio=punteroDominio.derecha
						if punteroDominio.titulo==cad[1]:
							print"el dominio parece si existir, indexando"
							while punteroDominio.abajo!=None:
								punteroDominio=punteroDominio.abajo
							punteroDominio.abajo=NODORAIZ
							print "correctamente indexado"
							return True
					print "no existe el dominio, creandolo y relacionandolo"
					punteroDominio.derecha=NODODOMINIO
					NODODOMINIO.abajo=NODORAIZ
					return True
			print " parece que no existe la letra"
			punteroLetra.abajo=NODOLETRA
			NODOLETRA.derecha=NODORAIZ

			print "consultando la existencia del dominio"
			while punteroDominio.derecha!=None:
				punteroDominio=punteroDominio.derecha
				if punteroDominio.titulo==cad[1]:
					print "se encontro el dominio"
					while punteroDominio.abajo!=None:
						punteroDominio=punteroDominio.abajo
					print "encontrando el ultimo nodo, guardando"
					punteroDominio.abajo=NODORAIZ
					return True
			print "no se encontro ni letra ni dominio"
			punteroDominio.derecha=NODODOMINIO
			NODODOMINIO.abajo=NODORAIZ
			print "creado dominio y letra"
			return True


	def consultaLetra(self,titulo):
		if self.raiz!=None:
			print "la matriz tiene datos"
			letra= self.raiz
			cad=""
			print "consultando"
			while letra.abajo!=None:
				letra=letra.abajo
				if letra.titulo==titulo:
					print "parece que se encontraron resultados"
					while letra.derecha!=None:
						letra=letra.derecha
						print letra.titulo
						cad=cad+","+letra.titulo
						if letra.profundo!=None:
							aux=letra
							print "existen datos profundos"
							while aux.profundo!=None:
								aux=aux.profundo
								cad=cad+","+aux.titulo
								print aux.titulo
					return cad
			print "no coinciden los datos"
			return "no existe esta letra"
		else:
			print "pooped"
			return "la matriz esta vacia"

	def consultarDominio(self,titulo):
		if self.raiz!=None:
			print "la matriz tiene datos"
			letra= self.raiz
			cad=""
			print "consultando"
			while letra.derecha!=None:
				letra=letra.derecha
				if letra.titulo==titulo:
					print "parece que se encontraron resultados"
					while letra.abajo!=None:
						letra=letra.abajo
						print letra.titulo
						cad=cad+","+letra.titulo
						if letra.profundo!=None:
							aux=letra
							print "existen datos profundos"
							while aux.profundo!=None:
								aux=aux.profundo
								cad=cad+","+aux.titulo
								print aux.titulo
					return cad
			print "no coinciden los datos"
			return "no existe este dominio"
		else:
			print "pooped"
			return "la matriz esta vacia"

	def eliminarDato(self,titulo):
		if self.raiz!=None:
			aux=self.raiz
			while aux.abajo!=None:
				aux=aux.abajo
				if aux.titulo==titulo[0]:
					while aux.derecha!=None:
						previo = aux
						aux=aux.derecha
						if aux.titulo==titulo:
							if aux.profundo==None:
								previo.derecha=aux.derecha
							else:
								val=aux.profundo
								val.derecha=aux.derecha
								previo.derecha=val
							return True
						if aux.profundo!=None:
							tmp=aux
							while tmp.profundo!=None:
								tempo=tmp
								tmp=tmp.profundo
								if tmp.titulo==titulo:
									tempo.profundo=tmp.profundo
									return True
		return False

	def asignaMat(self):
		if self.raiz!=None:
			cad = " node [shape=record,width=.1,height=.1];"
			cad = cad + " rankdir=LR;"
			cad = cad + "node [shape=record,width=.1,height=.1];"
			nodoletras = self.raiz
			nododominio = self.raiz
			subletras= 'node0 [label = "'
			valor=0
			while NodoLetra.abajo!=None:
				subletras=subletras+"<f"+str(valor)+">|"
				NodoLetra=NodoLetra.abajo
			subletras=subletras+'",height=2.5];'
			
			return subletras

		return " "













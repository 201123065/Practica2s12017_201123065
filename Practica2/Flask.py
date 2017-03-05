from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/')
def index():
	context=""
	return render_template('index.html')

@app.route('/rentemp')
def template():
	return render_template('index.html')

@app.route('/param')
def params():
	p= request.args.get('params','vacio')
	return 'el parametro es {}'.format(p)
 

if __name__=='__main__':
	app.run(debug=True)


class Estructura_Lista_Simple:
	def __init__(self):
		self.indice=0
		self.palabra=None
		self.siguiente= None

class Matriz_Dispersa:
	def __init__(self):
		self.derecha=None
		self.izquierda=None
		self.arriba=None
		self.abajo=None
		self.usuario=None
		self.dominio=None

class Cola:
	def __init__(self):
		self.valor=0
		self.siguiente=None

class Pila:
	def __init__(self):
		self.valor=0
		self.siguiente=None


class Lista:
	def __init__(self):
		raiz=Estructura_Lista_Simple()
	def insertar(self,Lista):
		if self.raiz.palabra==None:
			self.raiz=Lista
		else:
			aux=self.raiz
			while True:
				if aux.siguiente==None:
					aux.siguiente=Lista
					break
				else:
					aux=aux.siguiente
	def dato(self):
		aux=self.raiz
		while aux.siguiente!=None:
			aux=aux.siguiente
		return aux.dato

	def consultar(self,dato):
		aux = self.raiz
		aux2 = self.raiz
		if aux.nombre == None:
			return "NO SE ENCONTRÓ EL DATO"
		else:
			if aux.nombre == dato :
				if aux.siguiente == None:
					self.raiz = Nodo()
				else :
					self.raiz = aux.siguiente
			else:
				while aux.siguiente != None and t:
					aux = aux.siguiente
					if aux.nombre == elemento :
						aux2.siguiente = aux.siguiente
						aux = None
						return "EL DATO SE ENCUENTRA EN EL ÍNDICE "+aux.indice
					aux2 = aux2.siguiente
				return "NO SE ENCONTRÓ EL DATO"


class Estructura_cola:
	def __init__(self):
		raiz=Lista_Simple()
	def insertar(self,Lista):
		if self.raiz.palabra=None:
			self.raiz=Lista
		else:
			aux=self.raiz
			while True:
				if aux.siguiente==None:
					aux.siguiente=Lista
					break
				else:
					aux=aux.siguiente
	def dato(self):
		aux=self.raiz
		while aux.siguiente!=None:
			aux=aux.siguiente
		return aux.dato

	def consultar(self,dato):
		aux = self.raiz
		aux2 = self.raiz
		if aux.nombre == None:
			return "NO SE ENCONTRÓ EL DATO"
		else:
			if aux.nombre == dato :
				if aux.siguiente == None:
					self.raiz = Nodo()
				else :
					self.raiz = aux.siguiente
			else:
				while aux.siguiente != None and t:
					aux = aux.siguiente
					if aux.nombre == elemento :
						aux2.siguiente = aux.siguiente
						aux = None
						return "EL DATO SE ENCUENTRA EN EL ÍNDICE "+aux.indice
					aux2 = aux2.siguiente
				return "NO SE ENCONTRÓ EL DATO"








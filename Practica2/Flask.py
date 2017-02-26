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


class Estructura:
	def __init__(self):
		self.nombre =None
		self.edad=0
		self.siguiente=None

class Lista:
	def __init__(self):
		raiz = Estructura()

	def insertar(self,Estructura):
		if self.raiz.nombre==None:
			self.raiz ==Estructura
		else:
			aux = self.raiz
			while True:
				if aux.siguiente!=None:
					aux.siguiente=Estructura
					break
				else:
					aux=aux.siguiente

	def consultar(self):
		aux = self.raiz
		if aux.nombre == None:
			print "error"
		else:
			print aux.nombre
			print aux.edad

			while aux.siguiente!=None:
				aux= aux.siguiente
				print aux.nombre
				print edad

	def eliminar(self):
		aux=self.nombre
		if(aux.nombre==None):
			print "embti"
		else:
			elemento.raw_input("escribe el nombre a eliminar")
			while aux.nombre!=None:
				if(aux.nombre==elemento):
					print ":F"
					






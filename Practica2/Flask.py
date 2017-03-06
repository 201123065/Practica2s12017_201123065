from flask import Flask
from flask import request
from flask import render_template
from Lista import Lista
from Pila import Pila
from Cola import Cola
from Matriz import Matriz

app = Flask(__name__)

lista= Lista()
pila = Pila()
cola=Cola()
matriz=Matriz()

class WS():
#LISTA
	# INSERTAR
	@app.route('/insertar_lista',methods=['POST'])
	def insertar_lista():
		lista.insertar(request.form['nombre'])
		return "se ha ingresado correctamente"
	# CONSULTAR
	@app.route('/consultar_en_lista',methods=['POST'])
	def consultar_lista():
		valor= lista.consultar(request.form['nombre'])
		if valor==-1:
			return "no existe"
		else:
			return "se encuentra en el indice "+str(valor)
	# BORRAR
	@app.route('/borrar_en_lista',methods=['POST'])
	def borrar_lista():
		if lista.borrar(request.form['nombre']):
			return "borrado satisfactoriamente"
		else:
			return "el elemento no se ha encontrado"

	@app.route('/plot_Lista',methods=['POST'])
	def plotLista():
		return lista.plotLista("")
#PILA 
	# PUSH
	@app.route('/push',methods=['POST'])
	def push():
		pila.push(request.form['nombre'])
		return "se ha ingresado correctamente"
	# POP
	@app.route('/pop',methods=['POST'])
	def pop():
		valor= pila.pop()
		if valor==-1:
			return "no existe"
		else:
			return "valor pop: "+str(valor)
	
	@app.route('/plotPila',methods=['POST'])
	def plotpila():
		return pila.plotPila()
	


#COLA
	# QUEQUE
	@app.route('/queque',methods=['POST'])
	def queque():
		cola.queque(request.form['nombre'])
		return "se ha ingresado correctamente"
	# DEQUEQUE
	@app.route('/dequeque',methods=['POST'])
	def dequeque():
		valor= cola.dequeque()
		if valor==-1:
			return "no existe"
		else:
			return "valor dequeque: "+str(valor)

	@app.route('/plotCola',methods=['POST'])
	def plotCola():
		return cola.plotCola()



# MATRIZ
	# AGREGAR VALOR
	@app.route('/addMat',methods=['POST'])
	def addMat():
		if len(request.form['nombre'].split("@"))==2:
			valor = matriz.agregar(request.form['nombre'])
			return "se ha ingresado correctamente"
		else:
			return "dato no valido"
	# CONSULTAR POR LETRA
	@app.route('/byLetra',methods=['POST'])
	def byLetra():
		return matriz.consultaLetra(request.form['nombre'])
	# CONSULTAR POR DOMINIO
	@app.route('/bydomain',methods=['POST'])
	def byDomain():
		return matriz.consultarDominio(request.form['nombre'])

	@app.route('/del_val',methods=['POST'])
	def delVal():
		if matriz.eliminarDato(request.form['nombre']):
			return "elemento eliminado con exito"
		else:
			return "el elemento no existia en la matriz"

# INDEX
	@app.route('/')
	def index():
		context=""
		return render_template('index.html')


	if __name__=='__main__':
		app.run(debug=True)


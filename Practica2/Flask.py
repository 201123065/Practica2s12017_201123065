from flask import Flask
from flask import request
from flask import render_template
from Lista import Lista

app = Flask(__name__)

lista= Lista()
pila = Pila()

class WS():
	# METODOS DE LA LISTA
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
		valor= lista.consultar(request.form['nombre'])
		if valor==-1:
			return "no existe"
		else:
			return "se encuentra en el indice "+str(valor)
	# METODOS DE LA PILA 
	# PUSH
	@app.route('/push',methods=['POST'])
	def push():
		pila.push(request.form['nombre'])
		return "se ha ingresado correctamente"
	# POP
	@app.route('/pop',methods=['POST'])
	def pop():
		valor= lista.consultar(request.form['nombre'])
		if valor==-1:
			return "no existe"
		else:
			return "se encuentra en el indice "+str(valor)


	@app.route('/recuperar_lista')
	def recuperar_lista():
		lista.consultar()
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


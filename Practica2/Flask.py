from flask import Flask
from flask import request
from flask import render_template
from Lista import Lista

app = Flask(__name__)

lista= Lista()

class WS():
	@app.route('/insertar_lista',methods=['POST'])
	def insertar_lista():
		lista.insertar(request.form['nombre'])
		return "se ha ingresado correctamente"


	@app.route('/consultar',methods=['POST'])
	def consultar_lista():
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


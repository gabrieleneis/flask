from flask import Flask, render_template
app = Flask(__name__) #instanciando classe flask

#endereço do site
@app.route('/') #rota principal
@app.route('/index') #rota alternativa
def index():
   # return "Ahoy!"
   nome='Gabriele'
   dados={"Profissão": "SRE", "cidade":"Santa Rosa"}
   return render_template('index.html', nome=nome, dados=dados) 

@app.route('/contato')
def contato(): #define a rota
   return render_template('contato.html')

@app.route('/produto')
def produto():
   return render_template('produto.html')

app.run()
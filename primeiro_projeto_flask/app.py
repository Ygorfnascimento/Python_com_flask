from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    nome = request.form['nome']
    return f'Olá, {nome} seu formulário foi recebido com sucesso!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
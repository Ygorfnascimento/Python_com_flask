from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/soma', methods=['POST'])
def soma():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')

    if num1 and num2:
        try:
            resultado = int(num1) + int(num2)
        except ValueError:
            resultado = "Erro: insira apenas números."
    else:
        resultado = "Por favor, preencha os dois campos."

    return render_template('resultado.html', resultado=resultado)

@app.route('/sub', methods=['POST'])
def sub():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')

    if num1 and num2:
        try:
            resultado = int(num1) - int(num2)
        except ValueError:
            resultado = "Erro: insira apenas números."
    else:
        resultado = "Por favor, preencha os dois campos."

    return render_template('resultado.html', resultado=resultado)

@app.route('/multiplicacao', methods=['POST'])
def multiplicacao():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')

    if num1 and num2:
        try:
            resultado = int(num1) * int(num2)
        except ValueError:
            resultado = "Erro: insira apenas números."
    else:
        resultado = "Por favor, preencha os dois campos."

    return render_template('resultado.html', resultado=resultado)

@app.route('/divisao', methods=['POST'])
def divisao():
    num1 = request.form.get('num1')
    num2 = request.form.get('num2')

    if num1 and num2:
        try:
            if int(num2) == 0:
                resultado = "Erro: divisão por zero não é permitida."
            else:
                resultado = int(num1) / int(num2)
        except ValueError:
            resultado = "Erro: insira apenas números."
    else:
        resultado = "Por favor, preencha os dois campos."

    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        nome = request.form.get('nome')
        cor = request.form.get('cor')

        return redirect(url_for('saudacao', nome=nome, cor=cor))
    return render_template('index.html')

@app.route('/saudacao')
def saudacao():

    nome = request.args.get('nome')
    cor = request.args.get('cor')
    return render_template('index.html', valor=nome, cor=cor)

if __name__ == '__main__':
    app.run(debug=True)
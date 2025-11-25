from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'chave-super-secreta'

usuarios = {
    'admin': '1234',
}

agenda = []

@app.route('/')
def index():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    tarefas_usuario = [t for t in agenda if t['autor'] == session['usuario']]
    return render_template('index.html', compromissos=tarefas_usuario, usuario=session['usuario'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        if usuario in usuarios and usuarios[usuario] == senha:
            session['usuario'] = usuario
            return redirect(url_for('index'))
        else:
            return render_template('login.html', erro='Usuário ou senha incorretos!')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

@app.route('/adicionar', methods=['POST'])
def adicionar():
    if 'usuario' not in session:
        return redirect(url_for('login'))

    compromisso = request.form.get('compromisso')
    data = request.form.get('data')

    if compromisso and data:
        agenda.append({
            'compromisso': compromisso.strip(),
            'data': data,
            'autor': session['usuario'],
            'status': 'a_fazer'
        })

    return redirect(url_for('index'))

@app.route('/mudar_status/<int:index>/<novo_status>')
def mudar_status(index, novo_status):
    if 'usuario' not in session:
        return redirect(url_for('login'))

    if 0 <= index < len(agenda) and novo_status in ['a_fazer', 'fazendo', 'feito']:
        agenda[index]['status'] = novo_status

    return redirect(url_for('index'))

@app.route('/remover/<int:index>')
def remover(index):
    if 'usuario' not in session:
        return redirect(url_for('login'))

    if 0 <= index < len(agenda):
        agenda.pop(index)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
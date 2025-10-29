from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

app = Flask(__name__)
app.secret_key = 'super secret key'

USERNAME = 'admin'
PASSWORD = '123'

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USERNAME and password == PASSWORD:
            session['username'] = username
            flash('Login efetuado com sucesso!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Credenciamento inválido!', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logout efetuado com sucesso!', 'info')
    return redirect(url_for('login'))

@app.route('/user/<nome>')
def user(nome):
    return f"Olá, {nome}!"

@app.route('/api/dados')
def dados():
    return jsonify({"nome": "mariano", "idade": 92})

if __name__ == '__main__':
 app.run(debug=True)
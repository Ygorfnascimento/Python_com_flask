# 🧪 Mini Projetos em Python com Flask

Este repositório contém uma coleção de mini projetos desenvolvidos em Python com **Flask**, utilizando **HTML** para renderização de páginas, voltados à prática de conceitos essenciais de aplicações web.

---

## 🎯 Objetivo

Praticar o desenvolvimento de aplicações web com Flask, explorando:

* Criação de rotas dinâmicas
* Renderização de páginas HTML com Jinja2 (templates)
* Manipulação de requisições e formulários (POST/GET)
* Organização básica de projetos Flask e ambientes virtuais

---

## 📂 Organização dos Projetos

O repositório está dividido em pastas independentes, focando em cenários específicos de estudo:

* **`primeiro_projeto_flask`:** Estrutura inicial e primeiras rotas com Flask.
* **`projeto_agenda (flask)`:** Criação de uma agenda funcional com telas de base, index e login.
* **`projeto_calculadora (flask)`:** Recebimento de dados via formulário e exibição de resultados matemáticos.
* **`projeto_cores (flask)`:** Estudo de renderização dinâmica de dados e estilos no template.
* **`projeto_login (flask)`:** Simulação de fluxo de autenticação entre páginas restritas e formulários.

> ⚠️ **Observação:** Os mini projetos são laboratórios de estudo independentes e focam na lógica de rotas com Flask + HTML, não possuindo banco de dados relacional complexo.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Framework Back-end:** Flask
* **Frontend:** HTML5
* **Ambiente Virtual:** venv

---

## 🚀 Como Executar

Siga os passos abaixo para preparar o ambiente e rodar qualquer um dos projetos localmente:

### 1. Clone o repositório e acesse a pasta do projeto desejado:
```bash
git clone https://github.com/Ygorfnascimento/Python_com_flask.git
cd Python_com_flask/projeto_calculadora (flask)/ex_flask (1)
```
### 2. Crie e ative o ambiente virtual (opcional):
```bash
# Criar o ambiente virtual (rode apenas a primeira vez)
python -m venv venv

# Ativar no Windows:
.\venv\Scripts\activate

# Ativar no Linux/Mac:
source venv/bin/activate
```
### 3. Instale o Flask:
```bash
pip install flask
```
### 4. Execute o servidor local:
```bash
python calcular.py
```
> ⚠️ Observação: Fique atento ao arquivo principal de cada pasta. No projeto da calculadora é `calcular.py`, no de cores é `cor.py`, na agenda é `agenda.py` e nos demais costuma ser `app.py`
### 5. Acesse no seu navegador:
`http://127.0.0.1:5000`


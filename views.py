from main import app
from flask import Flask, render_template,request


@app.route("/", methods=["GET", "POST"])  # Define a rota e permite requisições GET e POST
def home():
    
    # Verifica se a requisição foi feita via POST (ou seja, envio de formulário)
    if request.method == "POST":
        
        # Pega o valor do input com name="emailForm" enviado pelo formulário
        email = request.form['emailForm']
        
        # Pega o valor do input com name="senhaForm"
        senha = request.form['senhaForm']
        
        # Exibe os dados no terminal (debug básico, não é prática segura em produção)
        print(f"email: {email}\nsenha: {senha}")

    # Sempre retorna o HTML da página (tanto no GET quanto depois do POST)
    return render_template("home.html")
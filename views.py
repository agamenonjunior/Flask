from main import app

@app.route("/")
def homepage():
    return "Homepage Flask"

@app.route("/blog")
def blog():
    return "Blog Flask"

@app.route("/contato")
def contato():
    return "contato Flask"

@app.route("/sobre")
def sobre():
    return "sobre Flask"

@app.route("/servicos")
def sobre():
    return "Meus servicos Flask"

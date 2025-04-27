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

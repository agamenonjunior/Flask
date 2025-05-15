from main import app
# página Home
@app.route("/")
def homepage():
    return "Homepage Flask"
# Página de Blog
@app.route("/blog")
def blog():
    return "Blog Flask"
# Página de Contato
@app.route("/contato")
def contato():
    return "contato Flask"
# Página Sobre
@app.route("/sobre")
def sobre():
    return "sobre Flask"
# Página de Serviços
@app.route("/servicos")
def servicos():
    return "Meus servicos Flask"

# Página de Dúvidas Frequentes
@app.route("/duvidas-frequentes")
def duvidasFrequentes():
    return "duvidas-frequentes Flask"


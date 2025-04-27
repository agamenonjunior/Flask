from main import app

@app.route("/")
def homepage():
    return "Homepage Flask"

@app.route("/blog")
def blog():
    return "Blog Flask"
from flask import Flask

app = Flask(__name__)

#Rotas

@app.route("/")
def home():
    return "Home"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

# Creating simple Routes 
@app.route('/test')
def test():
    return "inicio"

@app.route('/test/acerca/')
def about_test():
    return "acerca"

# Routes to Render Something
@app.route('/')
def home():
    return render_template("Inicio.html")

@app.route('/acerca', strict_slashes=False)
def about():
    return render_template("acerca.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)

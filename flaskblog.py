from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>HeY BOY!</h1>"

@app.route("/about")
def about():
    return "<h1>About page</h1>"

@app.route("/portfolio")
def portfolio():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/<nombre>')
def about(nombre):
    return render_template('about.html',nombre = nombre)

if __name__ == '__main__':
    app.run(debug =True)



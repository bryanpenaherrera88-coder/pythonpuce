from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Hola desde Render y Python sasd"

if __name__ == '__main__':
    app.run()
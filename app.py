from flask import Flask
                                                        # $ pipenv install Flask para instalar localmente (pipenv), no globalmente (pip) Flask
app = Flask(__name__)


@app.route("/", methods={"GET"})                         # definimos la ruta y el endpoint (GET, POST, DELETE...)
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/people", methods={"GET"})                         # definimos la ruta y el endpoint (GET, POST, DELETE...)
def hello_world2():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':                                # para levantar el puerto sería el comando $ pipenv run python app.py 
    app.run(port=3245, debug=True)

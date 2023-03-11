from flask import Flask, request
from models import Schema
from service import Service

app = Flask(__name__)


@app.route("/todo", methods=["POST"])
def create_todo():
    req = request.get_json()
    print(req)
    return Service().create(req)


if __name__ == "__main__":
    Schema()
    app.run(debug=True)

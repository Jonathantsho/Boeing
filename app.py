#Boeing
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():

    if request.method == "POST":
        data = request.get_data().decode("utf-8")
        return "Hello {} World!".format(data)
    else:
        return "Hello World!"


if __name__ == '__main__':
    app.run()
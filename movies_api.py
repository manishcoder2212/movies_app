import csv
from flask import Flask, jsonify, request
from data import data
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


with open('small_data.csv', newline="") as f:
    reader = csv.reader(f)
    movies_data = list(reader)


@app.route("/movie_rec")
def index():
    return jsonify({
        "data": movies_data,
        "message": "success"
    }), 200


if __name__ == "__main__":
    app.run()

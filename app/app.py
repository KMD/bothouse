from flask import Flask, jsonify
import certifi
from elasticsearch import Elasticsearch

from Company import Company

app = Flask(__name__)

@app.route("/<id>")
def hello(id):
    company = Company()
    return jsonify(company.fetchSimilarCompanies(id))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def link():
    data = request.get_json()
    print(data)
    return data

if __name__ == '__main__':
    app.run(debug=True, port=5000)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello")
def hello():
    name = request.args.get("name", "world")
    return jsonify({
        "message": f"Hello {name}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/batman")
def batman():
    name = request.args.get("name", "Bruce Wayne")
    return jsonify({
        "message": f"Hello {name}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


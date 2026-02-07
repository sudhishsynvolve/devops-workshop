from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello")
def hello():
    name = request.args.get("name", "World")
    return jsonify({
        "message": f"Hello {name}"
    })

@app.route("/blackwidow")
def blackwidow():
    name = request.args.get("name", "This is Black Widow")
    return jsonify({
        "message": f"Hello {name}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


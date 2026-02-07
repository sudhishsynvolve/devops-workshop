from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ironman")
def ironman():
    name = request.args.get("name", "I am ironman from avengers")
    return jsonify({
        "message": f"Hello {name}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

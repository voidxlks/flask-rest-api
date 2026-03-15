from flask import Flask, jsonify, request

app = Flask(__name__)

users = []

@app.route("/")
def home():
    return {"message": "Flask REST API is running"}

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json

    user = {
        "id": len(users) + 1,
        "name": data["name"]
    }

    users.append(user)

    return jsonify(user), 201


if __name__ == "__main__":
    app.run(debug=True)

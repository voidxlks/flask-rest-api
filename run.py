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
# Health check
@app.route("/health")
def health():
    return {"status": "ok"}

# Get a single user
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}, 404

# Delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return {"message": "User deleted"}

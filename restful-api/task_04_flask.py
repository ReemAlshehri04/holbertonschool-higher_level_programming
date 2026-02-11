#!/usr/bin/python3
"""
Simple API using Flask
"""

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

# In-memory users dictionary
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# /status endpoint
@app.route("/status")
def status():
    return "OK"


# /data endpoint → list of all usernames
@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))


# /users/<username> endpoint
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return make_response(jsonify({"error": "User not found"}), 404)


# /add_user endpoint (POST)
@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return make_response(jsonify({"error": "Invalid JSON"}), 400)

    data = request.get_json()

    username = data.get("username")
    if not username:
        return make_response(jsonify({"error": "Username is required"}), 400)

    if username in users:
        return make_response(jsonify({"error": "Username already exists"}), 409)

    # Add user
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return make_response(jsonify({"message": "User added", "user": users[username]}), 201)


if __name__ == "__main__":
    # Run Flask development server
    app.run(host="0.0.0.0", port=5000)


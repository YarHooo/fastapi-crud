from flask import Flask, request, jsonify

app = Flask(__name__)

# Приклад даних для тестування
users = [
    {"id": 1, "name": "Іван", "email": "ivan@example.com"},
    {"id": 2, "name": "Марія", "email": "maria@example.com"}
]

# GET - отримати список користувачів
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# POST - створити нового користувача
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

# DELETE - видалити користувача
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = next((user for user in users if user['id'] == id), None)
    if user:
        users.remove(user)
        return '', 204
    return 'User not found', 404

# PATCH - оновити користувача
@app.route('/users/<int:id>', methods=['PATCH'])
def update_user(id):
    user = next((user for user in users if user['id'] == id), None)
    if user:
        user_data = request.get_json()
        user.update(user_data)
        return jsonify(user)
    return 'User not found', 404

if __name__ == '__main__':
    app.run(debug=True)

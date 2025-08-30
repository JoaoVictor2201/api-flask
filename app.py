from flask import Flask, jsonify, request
from bd import users

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def getUsers():
  if not users:
    return []
  else:
    return jsonify(users)
  
@app.route("/users/<int:userId>", methods=["GET"])
def getUserById(userId):
  if not isinstance(userId, int):
    return 404

  for user in users:
    if user['id'] == userId:
      return jsonify(user)
  
  return jsonify({"erro": f"Usuário {userId} não encontrado!"}), 404

@app.route("/users", methods=["POST"])
def createUser():
  userData = request.json
  name = userData.get("nome")
  email = userData.get("email")

  if not name or not email:
    return jsonify({"erro": "Os campos 'nome' e 'email' são obrigatórios"}), 400
  
  if users:
    newId = users[-1]['id'] + 1
  else:
    newId = 1

  newUser = {
    'id': newId,
    'nome': name,
    'email': email
  }

  users.append(newUser)

  return jsonify(newUser), 201

@app.route("/users/<int:userId>", methods=["PUT"])
def updateUser(userId):
  userData = request.json

  if not userData:
    return jsonify({"erro": "corpo da requisição vazio"})

  for user in users:
    if user["id"] == userId:
      user["nome"] = userData.get("nome", user["nome"])
      user["email"] = userData.get("email", user["email"])
      return jsonify(user)
  
  return jsonify({"erro": "Usuário não encontrado!"}), 404  

@app.route("/users/<int:userId>", methods=["DELETE"])
def deleteUser(userId):
  for user in users:
    if user["id"] == userId:
      users.remove(user)
      return jsonify({"message": "Usuário removido!"})
  return jsonify({"erro": "Usuário não encontrado!"}), 404
      
if __name__ == "__main__":
  app.run(debug=True)

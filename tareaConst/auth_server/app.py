from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
import datetime

app = Flask(__name__)


app.config["JWT_SECRET_KEY"] = "superpoderosa"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=1)

jwt = JWTManager(app)


USERS_DB = {
    "admin": "password123",
    "panda": "123456"
}

# Endpoint para generar tokens de acceso OAuth 2.0
@app.route("/token", methods=["POST"])
def generate_token():
    data = request.json

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Faltan credenciales"}), 400

    username = data["username"]
    password = data["password"]

    # Verificación de credenciales
    if USERS_DB.get(username) == password:
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token})

    return jsonify({"error": "Credenciales inválidas"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
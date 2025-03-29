from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

app = Flask(__name__)


app.config["JWT_SECRET_KEY"] = "superpoderosa"

jwt = JWTManager(app)

# Endpoint protegido que requiere un token de acceso válido
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Acceso autorizado para {current_user}"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True, use_reloader=False)



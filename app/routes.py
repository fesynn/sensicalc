from flask import Blueprint, render_template, request, jsonify
from app.calculator import convert_sensitivity
from app.games import list_games

main = Blueprint("main", __name__)


@main.route("/")
def index():
    games = list_games()
    return render_template("index.html", games=games)


@main.route("/convert", methods=["POST"])
def convert():
    data = request.get_json()

    # Pega os valores obrigatórios
    from_game = data.get("from_game")
    to_game = data.get("to_game")
    sensitivity = data.get("sensitivity")

    # Valida os campos obrigatórios
    if not from_game or not to_game or sensitivity is None:
        return jsonify({"error": "Preencha jogo de origem, destino e sensibilidade."}), 400

    # Pega os opcionais (DPI e peso)
    from_dpi = data.get("from_dpi")
    to_dpi = data.get("to_dpi")
    from_weight = data.get("from_weight")
    to_weight = data.get("to_weight")

    # Converte strings para números se vieram preenchidos
    try:
        sensitivity = float(sensitivity)
        from_dpi = int(from_dpi) if from_dpi else None
        to_dpi = int(to_dpi) if to_dpi else None
        from_weight = float(from_weight) if from_weight else None
        to_weight = float(to_weight) if to_weight else None
    except ValueError:
        return jsonify({"error": "Valores numéricos inválidos."}), 400

    # Chama a lógica de cálculo
    try:
        result = convert_sensitivity(
            from_game_id=from_game,
            to_game_id=to_game,
            sensitivity=sensitivity,
            from_dpi=from_dpi,
            to_dpi=to_dpi,
            from_weight=from_weight,
            to_weight=to_weight,
        )
        return jsonify(result)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
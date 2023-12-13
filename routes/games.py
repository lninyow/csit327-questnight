from flask import Blueprint, jsonify, request
from db.games import create_game, get_game, get_games, update_game, delete_game


games = Blueprint("games", __name__)


@games.get("/")
def handle_get_all_games():
    data = get_games()
    return jsonify(data)


@games.get("/<int:id>")
def handle_get_game(id):
    data = get_game(id)
    return jsonify(data)


@games.post("/")
def handle_create_game():
    body = request.json
    title = body["title"]
    description = body["description"]
    game_id = create_game(title, description)
    return jsonify({"game_id": game_id})


@games.put("/<int:id>")
def handle_update_game(id):
    body = request.json
    title = body["title"]
    description = body["description"]
    game_id = update_game(id, title, description)
    return jsonify({"game_id": game_id})


@games.delete("/<int:id>")
def handle_delete_game(id):
    game_id = delete_game(id)
    return jsonify({"game_id": game_id})

from db.database import fetchone, fetchall


def create_game(title, description):
    query = "CALL create_game(%s, %s)"
    params = (title, description)
    result = fetchone(query, params)
    return result["game_id"]


def get_games():
    query = "SELECT * FROM games"
    result = fetchall(query)
    return result


def get_game(game_id):
    query = "SELECT * FROM games WHERE game_id = %s"
    params = (game_id,)
    result = fetchone(query, params)
    return result


def update_game(game_id, title, description):
    query = "CALL update_game(%s, %s, %s)"
    params = (game_id, title, description)
    result = fetchone(query, params)
    return result["game_id"]


def delete_game(game_id):
    query = "CALL delete_game(%s)"
    params = (game_id,)
    result = fetchone(query, params)
    return result["game_id"]

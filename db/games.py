from db.database import fetchone, fetchall

def create_game(title, cover_url, description):
    query = "CALL create_game(%s, %s, %s)"
    params = (title, cover_url, description)
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

def update_game(game_id, title, cover_url, description):
    query = "CALL update_game(%s, %s, %s, %s)"
    params = (game_id, title, cover_url, description)
    result = fetchone(query, params)
    return result["game_id"]

def delete_game(game_id):
    query = "CALL delete_game(%s)"
    params = (game_id,)
    result = fetchone(query, params)
    return result["game_id"]

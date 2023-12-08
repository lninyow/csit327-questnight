from database import fetchone, fetchall

def create_game(title, cover_url, description):
    query = "INSERT INTO games (title, coverUrl, description) VALUES (%s, %s, %s)"
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
    query = "UPDATE games SET title = %s, coverUrl = %s, description = %s WHERE game_id = %s"
    params = (title, cover_url, description, game_id)
    result = fetchone(query, params)
    return result["game_id"]

def delete_game(game_id):
    query = "DELETE FROM games WHERE game_id = %s"
    params = (game_id,)
    result = fetchone(query, params)
    return result["game_id"]

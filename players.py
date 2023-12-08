from database import fetchone, fetchall

def create_player(name, total_wins):
    query = "INSERT INTO players (name, total_wins) VALUES (%s, %s)"
    params = (name, total_wins)
    result = fetchone(query, params)
    return result["player_id"]

def get_players():
    query = "SELECT * FROM players"
    result = fetchall(query)
    return result

def get_player(player_id):
    query = "SELECT * FROM players WHERE player_id = %s"
    params = (player_id,)
    result = fetchone(query, params)
    return result

def update_player(player_id, name, total_wins):
    query = "UPDATE players SET name = %s, total_wins = %s WHERE player_id = %s"
    params = (name, total_wins, player_id)
    result = fetchone(query, params)
    return result["player_id"]

def delete_player(player_id):
    query = "DELETE FROM players WHERE player_id = %s"
    params = (player_id,)
    result = fetchone(query, params)
    return result["player_id"]

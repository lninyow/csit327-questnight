from db.database import fetchone, fetchall


def create_player(name, gender):
    query = "CALL create_player(%s,%s)"
    params = (name, gender)
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


def update_player(player_id, name, gender, total_wins):
    query = "CALL update_player(%s, %s, %s, %s)"
    params = (player_id, name, gender, total_wins)
    result = fetchone(query, params)
    return result["player_id"]


def delete_player(player_id):
    query = "CALL delete_player(%s)"
    params = (player_id,)
    result = fetchone(query, params)
    return result["player_id"]

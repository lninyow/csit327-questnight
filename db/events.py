from db.database import fetchone, fetchall


def create_event(start_date, end_date, game_id, winner_id):
    query = "INSERT INTO events (start_date, end_date, game_id, winner_id) VALUES (%s, %s, %s, %s)"
    params = (start_date, end_date, game_id, winner_id)
    result = fetchone(query, params)
    return result["event_id"]


def get_events():
    query = "SELECT * FROM events"
    result = fetchall(query)
    return result


def get_event(event_id):
    query = "SELECT * FROM events WHERE event_id = %s"
    params = (event_id,)
    result = fetchone(query, params)
    return result


def update_event(event_id, start_date, end_date, game_id, winner_id):
    query = "UPDATE events SET start_date = %s, end_date = %s, game_id = %s, winner_id = %s WHERE event_id = %s"
    params = (start_date, end_date, game_id, winner_id, event_id)
    result = fetchone(query, params)
    return result["event_id"]


def delete_event(event_id):
    query = "DELETE FROM events WHERE event_id = %s"
    params = (event_id,)
    result = fetchone(query, params)
    return result["event_id"]

from db.database import fetchone, fetchall


def create_event(start_date, end_date, game_id):
    query = "CALL create_event(%s, %s, %s)"
    params = (start_date, end_date, game_id)
    result = fetchone(query, params)
    return result["event_id"]


def get_events():
    query = "SELECT * FROM event_details"
    result = fetchall(query)
    return result


def get_event(event_id):
    query = "SELECT * FROM event_details WHERE event_id = %s"
    params = (event_id,)
    result = fetchone(query, params)
    return result


def update_event(event_id, start_date, end_date, game_id, winner_id):
    query = "CALL update_event(%s, %s, %s, %s, %s)"
    params = (event_id, start_date, end_date, game_id, winner_id)
    result = fetchone(query, params)
    return result["event_id"]


def delete_event(event_id):
    query = "CALL delete_event(%s)"
    params = (event_id,)
    result = fetchone(query, params)
    return result["event_id"]


def add_participant_to_event(event_id, player_id):
    query = "CALL add_participant_to_event(%s, %s)"
    params = (event_id, player_id)
    result = fetchone(query, params)
    return result


def remove_participant_from_event(event_id, player_id):
    query = "CALL remove_participant_from_event(%s, %s)"
    params = (event_id, player_id)
    result = fetchone(query, params)
    return result


def get_event_participants(event_id):
    query = "SELECT * FROM event_participants_view WHERE event_id = %s"
    params = (event_id,)
    result = fetchall(query, params)
    return result

from flask import Blueprint, jsonify, request
from db.events import create_event, get_events, get_event, update_event, delete_event

events = Blueprint("events", __name__)


@events.get("/")
def handle_get_all_events():
    data = get_events()
    return jsonify(data)


@events.get("/<int:id>")
def handle_get_event(id):
    data = get_event(id)
    return jsonify(data)


@events.post("/")
def handle_create_event():
    body = request.json
    # destructure the json body into their own variables
    start_date = body["start_date"]
    end_date = body["end_date"]
    game_id = body["game_id"]
    winner_id = body["winner_id"]

    event_id = create_event(start_date, end_date, game_id, winner_id)
    # return the id of the newly created event in a json response
    return jsonify({"event_id": event_id})


@events.put("/<int:id>")
def handle_update_event(id):
    body = request.json
    # destructure the json body into their own variables
    start_date = body["start_date"]
    end_date = body["end_date"]
    game_id = body["game_id"]
    winner_id = body["winner_id"]

    event_id = update_event(id, start_date, end_date, game_id, winner_id)
    # return the id of the updated event in a json response
    return jsonify({"event_id": event_id})


@events.delete("/<int:id>")
def handle_delete_event(id):
    event_id = delete_event(id)
    # return the id of the deleted event in a json response
    return jsonify({"event_id": event_id})

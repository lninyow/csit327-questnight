CREATE TABLE games (
    game_id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    coverUrl VARCHAR(255),
    description VARCHAR(255)
);

CREATE TABLE players (
    player_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    total_wins INT
);

CREATE TABLE events (
    event_id INT PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE,
    game_id INT,
    winner_id INT,
    FOREIGN KEY (game_id) REFERENCES games(game_id),
    FOREIGN KEY (winner_id) REFERENCES players(player_id)
);

CREATE TABLE event_participants (
    event_participant_id INT PRIMARY KEY,
    added_date DATE,
    event_id INT,
    player_id INT,
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);

DELIMITER $$
CREATE PROCEDURE add_game_to_event(IN event_id INT, IN game_id INT)
BEGIN
   UPDATE events
   SET game_id = game_id
   WHERE event_id = event_id;
END
$$


CREATE TRIGGER update_winner_wins
AFTER UPDATE OF winner_id ON events
FOR EACH ROW
BEGIN
   UPDATE players
   SET total_wins = total_wins + 1
   WHERE player_id = NEW.winner_id;
END
$$


CREATE PROCEDURE add_participant_to_event(IN event_id INT, IN player_id INT)
BEGIN
   INSERT INTO event_participants(event_id, player_id)
   VALUES (event_id, player_id);
END
$$

DELIMITER ;

CREATE TRIGGER set_added_date
BEFORE INSERT ON event_participants
FOR EACH ROW
SET NEW.added_date = CURRENT_DATE;

CREATE VIEW event_details AS
SELECT 
    e.event_id,
    g.title AS game_title,
    p.name AS winner_name
FROM 
    events e
JOIN 
    games g ON e.game_id = g.game_id
LEFT JOIN 
    players p ON e.winner_id = p.player_id;

CREATE VIEW event_participants_view AS
SELECT 
    ep.event_id,
    p.name AS participant_name
FROM 
    event_participants ep
JOIN 
    players p ON ep.player_id = p.player_id;

SELECT 
    ed.event_id,
    ed.game_title,
    ed.winner_name,
    ep.participant_name
FROM 
    event_details ed
JOIN 
    event_participants_view ep ON ed.event_id = ep.event_id;



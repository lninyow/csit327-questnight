CREATE TABLE games (
    game_id INT  AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(255)
);

CREATE TABLE players (
    player_id INT  AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    total_wins INT
);

CREATE TABLE events (
    event_id INT  AUTO_INCREMENT PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE,
    game_id INT,
    winner_id INT,
    FOREIGN KEY (game_id) REFERENCES games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (winner_id) REFERENCES players(player_id) ON DELETE SET NULL
);

CREATE TABLE event_participants (
    event_participant_id INT  AUTO_INCREMENT PRIMARY KEY,
    added_date DATE,
    event_id INT,
    player_id INT,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES players(player_id) ON DELETE CASCADE
);

DELIMITER $$
-- Player Procedures
CREATE PROCEDURE create_player(IN p_name VARCHAR(255))
BEGIN
    INSERT INTO players(name, total_wins) 
    VALUES (p_name, 0);
    SELECT LAST_INSERT_ID() AS player_id;
END
$$


CREATE PROCEDURE update_player(IN p_player_id INT, IN p_name VARCHAR(255), IN p_total_wins INT)
BEGIN
    UPDATE players
    SET name = p_name, total_wins = p_total_wins
    WHERE player_id = p_player_id;
    SELECT p_player_id AS player_id;
END
$$


CREATE PROCEDURE delete_player(IN p_player_id INT)
BEGIN
    DELETE FROM players WHERE player_id = p_player_id;
    SELECT p_player_id AS player_id;
END
$$


-- Game Procedures
CREATE PROCEDURE create_game(IN p_title VARCHAR(255), IN p_description VARCHAR(255))
BEGIN
    INSERT INTO games(title, description)
    VALUES (p_title, p_description);
    SELECT LAST_INSERT_ID() AS game_id;
END
$$


CREATE PROCEDURE update_game(IN p_game_id INT, IN p_title VARCHAR(255), IN p_description VARCHAR(255))
BEGIN
    UPDATE games
    SET title = p_title, description = p_description
    WHERE game_id = p_game_id;
    SELECT p_game_id AS game_id;
END
$$


CREATE PROCEDURE delete_game(IN p_game_id INT)
BEGIN
    DELETE FROM games WHERE game_id = p_game_id;
    SELECT p_game_id AS game_id;
END
$$


-- Event Procedures
CREATE PROCEDURE create_event(IN p_start_date DATE, IN p_end_date DATE, IN p_game_id INT)
BEGIN
    INSERT INTO events(start_date, end_date, game_id)
    VALUES (p_start_date, p_end_date, p_game_id);
    SELECT LAST_INSERT_ID() AS event_id;
END
$$


CREATE PROCEDURE update_event(IN p_event_id INT, IN p_start_date DATE, IN p_end_date DATE, IN p_game_id INT, IN p_winner_id INT)
BEGIN
    UPDATE events
    SET start_date = p_start_date, end_date = p_end_date, game_id = p_game_id, winner_id = p_winner_id
    WHERE event_id = p_event_id;
    SELECT p_event_id AS event_id;
END
$$


CREATE PROCEDURE delete_event(IN p_event_id INT)
BEGIN
    DELETE FROM events WHERE event_id = p_event_id;
    SELECT p_event_id AS event_id;
END
$$


CREATE PROCEDURE add_participant_to_event(IN p_event_id INT, IN p_player_id INT)
BEGIN
    INSERT INTO event_participants(event_id, player_id)
    VALUES (p_event_id, p_player_id);
    SELECT LAST_INSERT_ID() AS event_participant_id;
END
$$


CREATE PROCEDURE remove_participant_from_event(IN p_event_id INT, IN p_player_id INT)
BEGIN
    DELETE FROM event_participants 
    WHERE event_id = p_event_id AND player_id = p_player_id;
    SELECT p_event_id AS event_id;
END
$$

CREATE TRIGGER update_winner_wins
AFTER UPDATE ON events
FOR EACH ROW
BEGIN
   IF NEW.winner_id IS NOT NULL AND OLD.winner_id IS NULL THEN
      UPDATE players
      SET total_wins = total_wins + 1
      WHERE player_id = NEW.winner_id;
   END IF;
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
    e.start_date,
    e.end_date,
    g.game_id AS game_id,
    g.title AS game_title,
    p.name AS winner_name,
    p.player_id AS winner_id
FROM 
    events e
JOIN 
    games g ON e.game_id = g.game_id
LEFT JOIN 
    players p ON e.winner_id = p.player_id;

CREATE VIEW event_participants_view AS
SELECT 
    ep.event_id,
    p.name AS participant_name,
    p.player_id AS participant_id
FROM 
    event_participants ep
JOIN 
    players p ON ep.player_id = p.player_id;
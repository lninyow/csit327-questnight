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
    added_date DATE NOT NULL,
    event_id INT,
    player_id INT,
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);

CREATE VIEW get_users AS
SELECT
  p.name,
  p.age,
  p.occupation,
  p.email,
  u.id,
  u.username,
  u.password
FROM persons p
INNER JOIN users u ON u.person_id = p.id;

DELIMITER $$
CREATE PROCEDURE create_user(
  IN p_name varchar(200),
  IN p_age int,
  IN p_occupation varchar(200),
  IN p_email varchar(200),
  IN p_username varchar(200),
  IN p_password varchar(200)
)
BEGIN
  DECLARE v_person_id int;
  INSERT INTO persons(name, age, occupation, email) VALUES(p_name, p_age, p_occupation, p_email);
  SET v_person_id = LAST_INSERT_ID();
  INSERT INTO users(person_id, username, password) VALUES(v_person_id, p_username, p_password);
  SELECT LAST_INSERT_ID() AS id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE update_user(
  IN user_id int,
  IN p_name varchar(200),
  IN p_age int,
  IN p_occupation varchar(200),
  IN p_email varchar(200),
  IN p_username varchar(200),
  IN p_password varchar(200)
)
BEGIN
  UPDATE persons
  INNER JOIN users ON users.person_id = persons.id
  SET name = p_name, age = p_age, occupation = p_occupation, email = p_email
  WHERE users.id = user_id;
  UPDATE users SET username = p_username, password = p_password
  WHERE id = user_id;
  SELECT user_id AS id;
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE delete_user(IN user_id int)
BEGIN
  DELETE FROM persons WHERE id = (SELECT person_id FROM users WHERE id = user_id);
  DELETE FROM users WHERE id = user_id;
  SELECT user_id AS id;
END$$
DELIMITER ;
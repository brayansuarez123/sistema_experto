USE DATABASE movie_expert

CREATE TABLE `game` (
  `id` int PRIMARY KEY,
  `title` varchar(255),
  `description` varchar(255),
  `image_url` varchar(255)
);

CREATE TABLE `game_genre` (
  `id` int PRIMARY KEY,
  `value` varchar(255),
  `id_game` int,
  `id_genre` int
);

CREATE TABLE `genre` (
  `id` int PRIMARY KEY,
  `name` varchar(255)
);

CREATE TABLE `history` (
  `id` int PRIMARY KEY,
  `date` date,
  `game_selected` int,
  `client_id` int
);

CREATE TABLE `client` (
  `id` int PRIMARY KEY,
  `username` varchar(255)
);

CREATE TABLE `genre_question` (
  `id` int PRIMARY KEY,
  `question` varchar(255),
  `genre_id` int
);

CREATE TABLE `client_preferences` (
  `id` int PRIMARY KEY,
  `client_id` int,
  `genre_id` int,
  `response` varchar(255)
);

ALTER TABLE `game_genre` ADD FOREIGN KEY (`id_game`) REFERENCES `game` (`id`);

ALTER TABLE `game_genre` ADD FOREIGN KEY (`id_genre`) REFERENCES `genre` (`id`);

ALTER TABLE `history` ADD FOREIGN KEY (`game_selected`) REFERENCES `game` (`id`);

ALTER TABLE `history` ADD FOREIGN KEY (`client_id`) REFERENCES `client` (`id`);

ALTER TABLE `genre_question` ADD FOREIGN KEY (`genre_id`) REFERENCES `genre` (`id`);

ALTER TABLE `client_preferences` ADD FOREIGN KEY (`client_id`) REFERENCES `client` (`id`);

-- a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT `title`, `name`
FROM `tv_shows`
LEFT JOIN `tv_show_genres` AS `show_genre`
ON tv_shows.id = show_genre.show_id
LEFT JOIN `tv_genres` AS `genre`
ON show_genre.genre_id = genre.id
ORDER BY `title` ASC. `name` ASC;

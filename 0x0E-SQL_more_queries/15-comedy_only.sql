-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT `title`
FROM `tv_shows`
LEFT JOIN `tv_show_genres` AS `show_genre`
ON tv_shows.id = show_genre.show_id
LEFT JOIN `tv_genres` AS `genre`
ON show_genre.genre_id = genre.id
WHERE genre.name = 'Comedy'
GROUP BY `title`
ORDER BY `title` ASC;

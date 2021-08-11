SELECT name FROM people WHERE id IN (SELECT DISTINCT(directors.person_id) FROM
    directors JOIN movies ON directors.movie_id = movies.id
WHERE id IN (SELECT movie_id FROM ratings WHERE rating >= '9.0'))
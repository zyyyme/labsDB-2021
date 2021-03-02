/* Selecting essential columns which are either needed in query or in final data. Then, filtering by rating and maximum return date. If film is not in the rental list, we can guarantee that film is in stock right now. Then we check for entry in film_category with given categories' ids.  */

SELECT film_id, title, rating FROM film WHERE NOT EXISTS (SELECT inventory_id FROM rental WHERE (SELECT max(return_date) FROM rental WHERE inventory_id = film_id) < rental.last_update AND inventory_id = film_id) AND (film.rating = 'R' OR film.rating = 'PG-13') AND EXISTS (SELECT category_id, film_id FROM film_category WHERE film_category.film_id = film_id AND film_category.category_id IN (11, 14)); 



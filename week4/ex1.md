## Order countries by id asc, then show the 12th to 17th rows.

σ(country_id>=12) (σ(country_id<=17) (country))

SELECT * FROM country WHERE country_id BETWEEN 12 and 17;

## List all addresses in a city whose name starts with 'A’.

σ(LIKE 'A%') (city)

SELECT * FROM city WHERE city LIKE 'A%';

## List all customers' first name, last name and the city they live in.

π(first_name, last_name, city) (customer ⋈(customer.address_id=city.city_id) city)

SELECT first_name, last_name, city FROM customer INNER JOIN city ON (customer.address_id = city.city_id);

## Find all customers with at least one payment whose amount is greater than 11 dollars.

π(first_name, last_name, city) (σ(payment.amount>11) (payment ⋈(payment.customer_id=customer.customer_id) customer))

SELECT * from customer INNER JOIN payment ON (customer.customer_id = payment.customer_id) WHERE payment.amount>11;

## Find all duplicated first names in the customer table.

π(S.first_name) (S = σ(P1.customer_id != P2.customer_id, 

P1.first_name = P2.first_name) ((P1 = π(first_name, customer_id) (customer)) x (P2 = π(first_name, customer_id) (customer))))
SELECT first_name, count(*) FROM customer GROUP BY first_name HAVING count(*)>1;
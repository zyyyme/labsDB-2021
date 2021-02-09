## Views

View that gets all customer with first names starting from "A": 

CREATE VIEW NamesOnA AS SELECT * FROM customer WHERE first_name LIKE 'A%';

View that gets all cities in Brazil from database:

CREATE VIEW CitiesInBrazil AS SELECT * FROM city WHERE country_id=15;

Execution of first view:

SELECT first_name, last_update FROM NamesOnA;

## Trigger

Trigger that updates customer's "active" status when customer entry updates:

CREATE FUNCTION update_activity() RETURNS trigger AS 'BEGIN NEW.active=1; END' LANGUAGE 'plpgsql';
CREATE TRIGGER UpdateActivity AFTER UPDATE ON customer FOR EACH ROW EXECUTE PROCEDURE update_activity();

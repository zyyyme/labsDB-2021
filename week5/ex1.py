import psycopg2

conn = psycopg2.connect(
    database='customers',
    user='postgres',
    host='127.0.0.1',
    port='5432'
    )

cur = conn.cursor()

# CREATE INDEX btree ON CUSTOMER (ID);
cur.execute('CREATE INDEX btree ON CUSTOMER (ID);')
cur.execute('EXPLAIN  SELECT * FROM CUSTOMER WHERE ID BETWEEN 10000 AND 20000')
print(cur.fetchall()) # [('Index Scan using customer_pkey on customer  (cost=0.29..649.28 rows=10344 width=215)',), ('  Index Cond: ((id >= 10000) AND (id <= 20000))',)]

# CREATE INDEX hash ON CUSTOMER USING hash (NAME);
cur.execute('CREATE INDEX hash ON CUSTOMER USING hash (NAME);')
cur.execute('EXPLAIN  SELECT * FROM CUSTOMER WHERE NAME = \'Scott Davis\' ')
print(cur.fetchall()) # [('Bitmap Heap Scan on customer  (cost=4.02..11.89 rows=2 width=215)',), ("  Recheck Cond: (name = 'Scott Davis'::text)",), ('  ->  Bitmap Index Scan on hash  (cost=0.00..4.01 rows=2 width=0)',), ("Index Cond: (name = 'Scott Davis'::text)",)]
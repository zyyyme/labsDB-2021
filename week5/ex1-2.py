import psycopg2

conn = psycopg2.connect(
    database='customers',
    user='postgres',
    host='127.0.0.1',
    port='5432'
    )

cur = conn.cursor()

cur.execute('CREATE INDEX btree ON CUSTOMER (ID);')
cur.execute('EXPLAIN  SELECT * FROM CUSTOMER WHERE ID BETWEEN 10000 AND 20000')
print(cur.fetchall()) # [('Index Scan using customer_pkey on customer  (cost=0.29..649.28 rows=10344 width=215)',), ('  Index Cond: ((id >= 10000) AND (id <= 20000))',)]

cur.execute('CREATE INDEX hash ON CUSTOMER USING hash (NAME);')
cur.execute('EXPLAIN  SELECT * FROM CUSTOMER WHERE NAME = \'Scott Davis\' ')
print(cur.fetchall()) # [('Bitmap Heap Scan on customer  (cost=4.02..11.89 rows=2 width=215)',), ("  Recheck Cond: (name = 'Scott Davis'::text)",), ('  ->  Bitmap Index Scan on hash  (cost=0.00..4.01 rows=2 width=0)',), ("Index Cond: (name = 'Scott Davis'::text)",)]

cur.execute('EXPLAIN ANALYZE SELECT * FROM CUSTOMER WHERE REVIEW = \'Develop until traditional good. Hotel degree general.\'')
print(cur.fetchall()) # [('Seq Scan on customer  (cost=0.00..4284.00 rows=1 width=215) (actual time=16.264..16.265 rows=0 loops=1)',), ("  Filter: (review = 'Develop until traditional good. Hotel degree general.'::text)",), ('  Rows Removed by Filter: 100000',), ('Planning Time: 0.023 ms',), ('Execution Time: 16.274 ms',)]

cur.execute('ALTER TABLE CUSTOMER ADD COLUMN review_tsv tsvector;')
cur.execute('CREATE INDEX gin on CUSTOMER USING gin(review_tsv) WITH (fastupdate=true)')
cur.execute('EXPLAIN ANALYZE SELECT * FROM CUSTOMER WHERE review_tsv = to_tsvector(\'Develop until traditional good. Hotel degree general.\')')
print(cur.fetchall()) # [('Gather  (cost=1000.00..19525.18 rows=500 width=247) (actual time=450.752..453.031 rows=0 loops=1)',), ('  Workers Planned: 1',), ('  Workers Launched: 1',), ('  ->  Parallel Seq Scan on customer  (cost=0.00..18475.18 rows=294 width=247) (actual time=449.576..449.576 rows=0 loops=2)',), ("        Filter: (review_tsv = to_tsvector('Develop until traditional good. Hotel degree general.'::text))",), ('        Rows Removed by Filter: 50000',), ('Planning Time: 1.664 ms',), ('Execution Time: 453.060 ms',)]

cur.execute('CREATE INDEX gist on CUSTOMER USING gist(review_tsv)')
cur.execute('EXPLAIN ANALYZE SELECT * FROM CUSTOMER WHERE review_tsv = to_tsvector(\'Develop until traditional good. Hotel degree general.\')')
print(cur.fetchall()) # [('Gather  (cost=1000.00..19525.18 rows=500 width=247) (actual time=481.070..482.373 rows=0 loops=1)',), ('  Workers Planned: 1',), ('  Workers Launched: 1',), ('  ->  Parallel Seq Scan on customer  (cost=0.00..18475.18 rows=294 width=247) (actual time=479.794..479.794 rows=0 loops=2)',), ("        Filter: (review_tsv = to_tsvector('Develop until traditional good. Hotel degree general.'::text))",), ('        Rows Removed by Filter: 50000',), ('Planning Time: 0.105 ms',), ('Execution Time: 482.382 ms',)]
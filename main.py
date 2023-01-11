import psycopg2

username = 'diubakin'
password = 'postgres'
database = 'lab2_Netflix_Top'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT
    TRIM(shows.show_title),
    count(countries.country_name)
FROM top10_by_contries
    JOIN shows ON shows.show_id = top10_by_contries.show_id
    JOIN countries ON countries.country_iso2 = top10_by_contries.country_iso2
WHERE
    top10_by_contries.show_id = 1
    OR top10_by_contries.show_id = 2
    OR top10_by_contries.show_id = 3
    OR top10_by_contries.show_id = 4
GROUP BY shows.show_title;
'''

query_2 = '''
SELECT
    TRIM(shows.show_title),
    count(
        top10_by_contries.cumulative_weeks_in_top_10
    )
FROM shows
    JOIN top10_by_contries ON shows.show_id = top10_by_contries.show_id
WHERE
    cumulative_weeks_in_top_10 = 1
    AND (
        top10_by_contries.show_id = 1
        OR top10_by_contries.show_id = 2
        OR top10_by_contries.show_id = 3
        OR top10_by_contries.show_id = 4
    )
GROUP BY shows.show_title;
'''

query_3 = '''
SELECT
    shows.category,
    count(shows.category)
FROM shows
GROUP BY shows.category;
'''

conn = psycopg2.connect(user=username, password=password,
                        dbname=database, host=host, port=port)
print(type(conn))

with conn:

    print("Database opened successfully")

    cur = conn.cursor()

    print('1.\n')
    cur.execute(query_1)
    for row in cur:
        print(row)

    cur.execute(query_2)
    print('2.\n')
    for row in cur:
        print(row)

    cur.execute(query_3)
    print('3.\n')
    for row in cur:
        print(row)

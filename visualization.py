import psycopg2
import matplotlib.pyplot as plt


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
GROUP BY shows.show_title;
'''

query_3 = '''
SELECT
    TRIM(shows.category),
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

    cur.execute(query_1)
    show_titles = []
    count = []
    for row in cur:
        show_titles.append(row[0])
        count.append(row[1])

    cur.execute(query_2)
    shows = []
    count_2 = []
    for row in cur:
        shows.append(row[0])
        count_2.append(row[1])

    cur.execute(query_3)
    categories = []
    count_3 = []
    for row in cur:
        categories.append(row[0])
        count_3.append(row[1])

    fig, (bar_ax, pie_ax, bar1_ax) = plt.subplots(3, 1)

    bar_ax.bar(show_titles, count)
    bar_ax.set_title('Кількість разів згадування кожного шоу в базі даних')
    bar_ax.set_xlabel('Назва шоу')
    bar_ax.set_ylabel('Кількість країн')

    pie_ax.pie(count_2, labels=shows)
    pie_ax.set_title(
        'Країні та кількість разів займання ними першого місця в топі')

    bar1_ax.bar(categories, count_3)
    bar1_ax.set_title('Кількість кожного жанру шоу')
    bar1_ax.set_xlabel('Назва категорії')
    bar1_ax.set_ylabel('Кількість')

    fig.tight_layout()
    plt.show()

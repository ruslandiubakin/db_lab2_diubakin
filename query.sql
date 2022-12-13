SELECT
    TRIM(shows.show_title),
    count(countries.country_name)
FROM top10_by_contries
    JOIN shows ON shows.show_id = top10_by_contries.show_id
    JOIN countries ON countries.country_iso2 = top10_by_contries.country_iso2
GROUP BY shows.show_title;

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

SELECT
    TRIM(shows.category),
    count(shows.category)
FROM shows
GROUP BY shows.category;
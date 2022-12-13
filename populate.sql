INSERT INTO
    countries(country_iso2, country_name)
VALUES ('GR', 'Greece'), ('HK', 'Hong Kong '), ('IS', 'Iceland '), ('PT', 'Portugal '), ('UA', 'Ukraine');

INSERT INTO
    shows(
        show_id,
        show_title,
        season_title,
        category
    )
VALUES (
        1,
        'The Good Doctor',
        'The Good Doctor: Season 4',
        'TV'
    ), (
        2,
        'Winter on Fire: Ukraine`s Fight for Freedom',
        NULL,
        'Films'
    ), (
        3,
        'Stranger Things',
        'Stranger Things 4',
        'TV'
    ), (
        4,
        'The Umbrella Academy',
        'The Umbrella Academy: Season 3',
        'TV'
    ), (
        5,
        'Manifest',
        'Manifest: Season 1',
        'TV'
    );

INSERT INTO
    top10_by_contries(
        country_iso2,
        show_id,
        week,
        weekly_rank,
        cumulative_weeks_in_top_10
    )
VALUES ('GR', 1, '2021-08-15', 8, 2), ('GR', 2, '2022-03-06', 9, 1), ('HK', 2, '2022-02-27', 10, 1), ('HK', 3, '2022-05-29', 1, 1), ('IS', 2, '2022-03-06', 9, 1), ('IS', 1, '2021-12-12', 7, 6), ('PT', 4, '2022-07-17', 10, 4), ('PT', 5, '2022-07-10', 2, 1), ('UA', 1, '2021-08-15', 9, 3), ('UA', 3, '2022-06-12', 1, 3);
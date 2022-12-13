CREATE TABLE
    countries(
        country_iso2 char(10) NOT NULL,
        country_name char(50) NOT NULL,
        PRIMARY KEY(country_iso2)
    );

CREATE TABLE
    shows(
        show_id int NOT NULL,
        show_title char(100) NOT NULL,
        season_title char(100),
        category char(50),
        PRIMARY KEY(show_id)
    );

CREATE TABLE
    top10_by_contries(
        country_iso2 char(10) NOT NULL,
        show_id int NOT NULL,
        week DATE,
        weekly_rank int,
        cumulative_weeks_in_top_10 int,
        Foreign Key (country_iso2) REFERENCES countries(country_iso2),
        Foreign Key (show_id) REFERENCES shows(show_id)
    );
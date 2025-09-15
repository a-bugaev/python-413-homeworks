-- HW 32_200425
-- used db: marvel_not_normal.db
-- Основные задания
-- 1
SELECT
    ALIVE,
    count(*)
FROM
    MarvelCharacters
WHERE
    ALIVE NOT NULL
GROUP BY
    ALIVE;

-- 2
SELECT
    EYE,
    round(avg(APPEARANCES), 2)
FROM
    MarvelCharacters
WHERE
    EYE NOT NULL
GROUP BY
    EYE;

-- 3
SELECT
    HAIR,
    max(APPEARANCES)
FROM
    MarvelCharacters
WHERE
    HAIR NOT NULL
GROUP BY
    HAIR;

-- 4
SELECT
    identify,
    min(APPEARANCES)
FROM
    MarvelCharacters
WHERE
    identify = 'Public Identity'
GROUP BY
    identify;

-- 5
SELECT
    SEX,
    count(*) as gender_count
FROM
    MarvelCharacters
WHERE
    SEX NOT NULL
GROUP BY
    SEX
ORDER BY
    gender_count DESC;

-- 6
SELECT
    identify,
    round(avg(Year)) as avg_app_year
FROM
    MarvelCharacters
WHERE
    identify NOT NULL
GROUP BY
    identify
ORDER BY
    avg_app_year DESC;

-- 7
SELECT
    EYE,
    count(*) as count
FROM
    MarvelCharacters
WHERE
    ALIVE = 'Living Characters'
    AND EYE NOT NULL
GROUP BY
    EYE
ORDER BY
    count DESC;

-- 8
SELECT
    HAIR,
    max(APPEARANCES) as max_apps,
    min(APPEARANCES)
FROM
    MarvelCharacters
WHERE
    HAIR NOT NULL
GROUP BY
    HAIR
ORDER BY
    max_apps DESC;

-- 9
SELECT
    identify,
    count(*) as identity_count
FROM
    MarvelCharacters
WHERE
    ALIVE = 'Deceased Characters'
    AND identify NOT NULL
GROUP BY
    identify
ORDER BY
    identity_count DESC;

-- 10
SELECT
    EYE,
    round(avg(Year)) avg_app_year
FROM
    MarvelCharacters
WHERE
    EYE NOT NULL
GROUP BY
    EYE
ORDER BY
    avg_app_year ASC;

-- 11
SELECT
    name,
    APPEARANCES
FROM
    MarvelCharacters
WHERE
    APPEARANCES = (
        SELECT
            max(APPEARANCES)
        FROM
            MarvelCharacters
    );

-- 12
SELECT
    name,
    Year
FROM
    MarvelCharacters
WHERE
    Year = (
        SELECT
            Year
        FROM
            MarvelCharacters
        WHERE
            APPEARANCES = (
                SELECT
                    max(APPEARANCES)
                FROM
                    MarvelCharacters
            )
    );

-- 13
SELECT
    name,
    APPEARANCES,
    ALIVE
FROM
    MarvelCharacters
WHERE
    APPEARANCES = (
        SELECT
            min(APPEARANCES)
        FROM
            MarvelCharacters
        WHERE
            ALIVE = 'Living Characters'
    )
    AND ALIVE = 'Living Characters';
-- rows: 3628

-- 14
SELECT
    name,
    HAIR,
    APPEARANCES
FROM
    MarvelCharacters
WHERE
    APPEARANCES = (
        SELECT
            max(APPEARANCES)
        FROM
            MarvelCharacters
        WHERE
            HAIR = 'White Hair'
    )
    AND HAIR = 'White Hair';
-- rows: 1

-- 15
SELECT
    name,
    identify,
    APPEARANCES
FROM
    MarvelCharacters
WHERE
    identify = 'Public Identity'
    AND APPEARANCES = (
        SELECT
            min(APPEARANCES)
        FROM
            MarvelCharacters
        WHERE
            identify = 'Public Identity'
    );
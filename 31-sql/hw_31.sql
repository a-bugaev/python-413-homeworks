
-- HW 31. used db: marvel_not_normal.db

-- 1
SELECT
    name,
    FIRST_APPEARANCE,
    Year,
    APPEARANCES
FROM
    MarvelCharacters
WHERE
    HAIR = 'Bald'
    AND ALIGN = 'Bad Characters'
    AND Year >= 1990
    AND Year <= 1999;
-- rows: 94

-- 2
SELECT
    name,
    FIRST_APPEARANCE,
    EYE
FROM
    `MarvelCharacters`
WHERE
    identify = 'Secret Identity'
    AND EYE NOT IN('Blue Eyes', 'Brown Eyes', 'Green Eyes')
    AND FIRST_APPEARANCE IS NOT NULL;
-- rows: 1028

-- 3
SELECT
    name,
    HAIR
FROM
    `MarvelCharacters`
WHERE
    HAIR = 'Variable Hair';
-- rows: 32

-- 4
SELECT
    name,
    EYE
FROM
    `MarvelCharacters`
WHERE
    SEX = 'Female Characters'
    AND EYE IN ('Gold Eyes', 'Amber Eyes');
-- rows: 5

-- 5
SELECT
    name,
    FIRST_APPEARANCE
FROM
    `MarvelCharacters`
WHERE
    identify = 'No Dual Identity'
ORDER BY
    Year DESC;
-- rows: 1788

-- 6
SELECT
    name,
    ALIGN,
    HAIR
FROM
    `MarvelCharacters`
WHERE
    HAIR NOT IN('Brown Hair', 'Black Hair', 'Blond Hair', 'Red Hair')
    AND ALIGN IN ('Good Characters', 'Bad Characters');
-- rows: 2744

-- 7
SELECT
    name,
    Year
FROM
    `MarvelCharacters`
WHERE
    Year >= 1960
    AND Year <= 1969;
-- rows: 1306

-- 8
SELECT
    name,
    EYE,
    HAIR
FROM
    `MarvelCharacters`
WHERE
    EYE = 'Yellow Eyes'
    AND HAIR = 'Red Hair';
-- rows: 13

-- 9
SELECT
    name,
    APPEARANCES
FROM
    `MarvelCharacters`
WHERE
    APPEARANCES < 10;
-- rows: 11938

-- 10
SELECT
    name,
    APPEARANCES
FROM
    `MarvelCharacters`
ORDER BY
    APPEARANCES DESC
LIMIT 5;
-- rows: 5
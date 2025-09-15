-- HW 34, part 1
PRAGMA foreign_keys = OFF;

BEGIN TRANSACTION;

-- 1. Создание таблиц и связей
-- a. Запись на услуги
CREATE TABLE appointments (
    id INTEGER PRIMARY KEY,
    client_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    Date DATETIME DEFAULT CURRENT_TIMESTAMP,
    comment TEXT,
    master_id INTEGER NOT NULL,
    status TEXT NOT NULL CHECK (
        status IN (
            'Подана заявка',
            'Запись подтверждена',
            'Услуга оплачена',
            'Услуга оказана'
        )
    ),
    FOREIGN KEY (master_id) REFERENCES masters (id)
);

-- b. Мастера
CREATE TABLE masters (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    middle_name TEXT,
    phone TEXT NOT NULL
);

-- c. Услуги
CREATE TABLE services (
    id INTEGER PRIMARY KEY,
    title TEXT UNIQUE NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
);

-- d. Связующие таблицы
-- мастера и услуги
CREATE TABLE masters_services (
    master_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    FOREIGN KEY (master_id) REFERENCES masters (id),
    FOREIGN KEY (service_id) REFERENCES services (id),
    PRIMARY KEY (master_id, service_id)
);

-- Записи и услуги
CREATE TABLE appointments_services (
    appointment_id INTEGER,
    service_id INTEGER,
    PRIMARY KEY (appointment_id, service_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments (id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services (id)
);


-- 2. Внесение данных
-- Мастера
INSERT INTO
    masters (first_name, last_name, middle_name, phone)
VALUES
    ('Татьяна', 'Иванова', 'Михайловна', '+53778541390'),
    ('Василий', 'Сидоров', 'Петрович', '+06997643570');

-- Услуги
INSERT INTO
    services (title, description, price)
VALUES
    ('Стрижка мужская модельная', '-', 600),
    ('Помывка головы', '-', 300),
    ('Окрашивание волос', '-', 1000),
    ('Простое бритье', '-', 200),
    ('Стайлинг бороды', '-', 500);

-- Связывание мастеров и услуг
INSERT INTO
    masters_services (master_id, service_id)
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (2, 5);

-- Добавление записей на услуги
INSERT INTO
    appointments (client_name, phone, master_id, comment, status)
VALUES
    (
        'Клиент Первый',
        '+70527416207',
        1,
        'текст комментария для Первого',
        'Подана заявка'
    ),
    (
        'Клиентка Вторая',
        '+72655470674',
        2,
        'текст комментария для Второй',
        'Запись подтверждена'
    ),
    (
        'Клиент Третий',
        '+39699848096',
        1,
        'текст комментария для Третьего',
        'Услуга оплачена'
    ),
    (
        'Клиентка Четвертая',
        '+75926060365',
        2,
        'текст комментария для Четвёртой',
        'Услуга оказана'
    );

-- Связывание добавленных записей с услугами
INSERT INTO
    appointments_services (appointment_id, service_id)
VALUES
    (1, 1),
    (1, 4),
    (2, 2),
    (3, 2),
    (3, 3),
    (4, 3);

COMMIT;

PRAGMA foreign_keys = ON;


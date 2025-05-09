-- HW 33: Barbershop db
-- 1. Создание таблиц и связей
-- a. Запись на услуги
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY,
    client_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    Date DATETIME DEFAULT CURRENT_TIMESTAMP,
    master_id INTEGER NOT NULL,
    status TEXT NOT NULL CHECK (
        status IN (
            'Подана заявка',
            'Запись подтверждена',
            'Услуга оплачена',
            'Услуга оказана'
        )
    ),
    FOREIGN KEY (master_id) REFERENCES masters (id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- b. Мастера
CREATE TABLE IF NOT EXISTS masters (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    middle_name TEXT,
    phone TEXT NOT NULL
);

-- c. Услуги
CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY,
    title TEXT UNIQUE NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
);

-- d. Связующие таблицы
-- мастера и услуги
CREATE TABLE IF NOT EXISTS masters_services (
    master_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    FOREIGN KEY (master_id) REFERENCES masters (id),
    FOREIGN KEY (service_id) REFERENCES services (id),
    PRIMARY KEY (master_id, service_id)
);

-- Записи и услуги
CREATE TABLE IF NOT EXISTS appointments_services (
    appointment_id INTEGER,
    service_id INTEGER,
    PRIMARY KEY (appointment_id, service_id),
    FOREIGN KEY (appointment_id) REFERENCES appointments (id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services (id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- 2. Внесение данных
-- Мастера
INSERT INTO
    masters (first_name, last_name, middle_name, phone)
VALUES
    ('Татьяна', 'Иванова', 'Михайловна', '1234567890'),
    ('Василий', 'Сидоров', 'Петрович', '0987654321');

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
    (2, 2),
    (2, 3),
    (1, 4),
    (2, 5);

-- Добавление записей на услуги
INSERT INTO
    appointments (client_name, phone, master_id, status)
VALUES
    ('Клиент Первый', '2233445566', 1, 'Подана заявка'),
    (
        'Клиентка Вторая',
        '7788991122',
        2,
        'Запись подтверждена'
    ),
    (
        'Клиент Третий',
        '2233445566',
        1,
        'Услуга оплачена'
    ),
    (
        'Клиентка Четвертая',
        '7788991122',
        2,
        'Услуга оказана'
    );

-- Связывание добавленных записей с услугами
INSERT INTO
    appointments_services (appointment_id, service_id)
VALUES
    (1, 1),
    (2, 2),
    (3, 2),
    (4, 3);
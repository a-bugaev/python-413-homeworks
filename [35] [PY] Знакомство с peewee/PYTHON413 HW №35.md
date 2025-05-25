---
project: "[[Академия TOP]]"
journal: "[[PYTHON411]]"
tags:
  - PYTHON413
date: 2025-05-23
type:
  - home work
hw_num: 35
topic: В этом задании вы опишете ORM‑модели и реализуете единый Python‑скрипт на основе PeeWee, который при запуске создаёт файл БД, создаёт таблицы, заполняет их тестовыми данными и выводит результаты в консоль.
hw_theme:
  - sqlite
  - CREATE
  - INSERT
  - UPDATE
  - python
  - PeeWee
st_group: python 413
links:
---
# Домашнее задание 📃  
**PeeWee‑модели и скрипт наполнения БД «Барбершоп»**  

## Краткое содержание  
В этом задании вы опишете ORM‑модели и реализуете единый Python‑скрипт на основе PeeWee, который при запуске создаёт файл БД, создаёт таблицы, заполняет их тестовыми данными и выводит результаты в консоль.

> [!info]  
> **Технологии:** Python, SQLite, PeeWee ORM  

## Задание 👷‍♂️  

### 1. Описание моделей и полей  
Опишите модели PeeWee, соответствующие таблицам проекта «Барбершоп». Поле `id` не объявляйте явно — PeeWee автоматически создаёт первичные ключи `AutoField`. Для каждого поля укажите тип PeeWee и основные параметры.

| Модель                 | Поле         | Тип PeeWee                     | Параметры                            |
| ---------------------- | ------------ | ------------------------------ | ------------------------------------ |
| **Master**             | first_name   | `CharField`                    | `max_length=50`, `null=False`        |
|                        | last_name    | `CharField`                    | `max_length=50`, `null=False`        |
|                        | middle_name  | `CharField`                    | `max_length=50`, `null=True`         |
|                        | phone        | `CharField`                    | `max_length=20`, `unique=True`       |
| **Service**            | title        | `CharField`                    | `max_length=100`, `unique=True`      |
|                        | description  | `TextField`                    | `null=True`                          |
|                        | price        | `DecimalField`                 | `max_digits=7`, `decimal_places=2`   |
| **Appointment**        | client_name  | `CharField`                    | `max_length=100`, `null=False`       |
|                        | client_phone | `CharField`                    | `max_length=20`, `null=False`        |
|                        | date         | `DateTimeField`                | `default=datetime.now`               |
|                        | master       | `ForeignKeyField[Master]`      | `backref='appointments'`             |
|                        | status       | `CharField`                    | `max_length=20`, `default='pending'` |
| **MasterService**      | master       | `ForeignKeyField[Master]`      |                                      |
|                        | service      | `ForeignKeyField[Service]`     |                                      |
| **AppointmentService** | appointment  | `ForeignKeyField[Appointment]` |                                      |
|                        | service      | `ForeignKeyField[Service]`     |                                      |

Таблица методов и функций PeeWee, которые понадобятся в этом ДЗ:

|Метод / Функция|Описание|
|---|---|
|`DB.connect()`|Устанавливает соединение с базой данных.|
|`DB.create_tables([Model1, Model2, …])`|Создаёт указанные модели (таблицы) в БД, если их ещё нет.|
|`DB.close()`|Закрывает соединение с базой после всех операций.|
|`Model.create(**fields)`|Создаёт и сразу сохраняет в БД одну запись с переданными значениями полей.|
|`Model.insert_many(list_of_dicts).execute()`|Пакетно вставляет несколько записей (полезно для создания сразу 2–3 мастеров или 3–4 услуг).|
|`Model.select()`|Начинает запрос на выборку всех записей из таблицы.|
|`Model.select().where(condition)`|Возвращает записи, удовлетворяющие условию (например, `Master.select().where(Master.phone=='123')`).|
|`Model.get(condition)`|Возвращает ровно одну запись по условию или бросает исключение, если ни одной или больше одной записи не найдено.|
|`Model.update(**fields).where(condition).execute()`|Обновляет поля выбранных записей по условию.|
|`Model.delete().where(condition).execute()`|Удаляет записи по заданному условию.|
|`model_instance.save()`|Сохраняет изменения в уже загруженном объекте модели (если нужны правки после `get()`).|
|`Model.select().join(OtherModel)`|Выполняет SQL‑JOIN с другой моделью, чтобы получить связанные через ForeignKeyField записи.|
|`ForeignKeyField(backref='…')`|При объявлении модели создаёт удобный атрибут в связанной модели (например, `master.appointments` для доступа ко всем записям этого мастера).|
|`Model.get_or_create(**fields)`|Ищет запись по полям, если не найдена — создаёт её; возвращает кортеж `(instance, created_flag)`.|
|`Model.count()`|Возвращает число записей, подходящих под параметры запроса.|


### 2. Реализация скрипта  
Создайте файл `homework_35.py`, в котором:

- Подключите базу:
  ```python
  from peewee import SqliteDatabase
  DB = SqliteDatabase('barbershop.db')
  ```

- Зарегистрируйте модели этой БД:
  ```python
  # Пример:
  # DB.connect()
  # DB.create_tables([Master, Service, Appointment, MasterService, AppointmentService])
  ```

- Добавьте тестовые данные через ORM:
  - не менее 2–3 мастеров;
  - не менее 3–4 услуг;
  - не менее 3 заявок, каждая привязана к одному мастеру и ровно двум услугам.

- После вставки сделайте выборку и выведите результаты в консоль:
  ```python
  # Пример вывода:
  # for m in Master.select(): ...
  # for s in Service.select(): ...
  # for a in Appointment.select(): ...
  ```

---

> [!warning]  
> ### Критерии проверки 👌  
> 1. Все модели описаны с корректными полями и параметрами, `id` не объявляется явно.  
> 2. Связи «многие‑ко‑многим» реализованы через `MasterService` и `AppointmentService`.  
> 3. Скрипт при запуске (`python homework_35.py`) создаёт или подключается к `barbershop.db`, создаёт таблицы и наполняет их тестовыми данными без ошибок.  
> 4. В базе есть минимум 2–3 мастера, 3–4 услуги и ≥3 заявок, каждая с двумя услугами.  
> 5. В консоли отображается список мастеров, услуг и заявок с указанием связанных услуг.  
> 6. Код соответствует PEP‑8, использует аннотации типов и методы PeeWee для всех операций.  

---

**Что сдавать:**  
- Python‑скрипт `homework_15.py`  
- Файл базы данных `barbershop.db`  

Запустите `python homework_15.py` — всё должно автоматически создаться, наполниться и отобразиться в консоли.
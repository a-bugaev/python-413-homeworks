"""
HW 36. Flask API
app.py: эндпоинты
"""

import sys
from flask import Flask
from dotenv import load_dotenv
from hw_37.blueprints import (
    masters_bp,
    appointments_bp,
)
from hw_37.peewee_db import (
    check_db_file_existance,
    check_tables_existance,
    create_tables,
    populate_db,
    remove_db_file,
)

load_dotenv()

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

app.register_blueprint(masters_bp)
app.register_blueprint(appointments_bp)

def main():
    if not sys.argv[1]:
        # Создание базы данных и таблиц если те не существуют
        if (not check_db_file_existance()) or (not check_tables_existance()):
            create_tables()
            populate_db()

    if sys.argv[1] == "--test":
        # перезапись бд в изначальное состояние для тестирования
        remove_db_file()
        create_tables()
        populate_db()

    # Запуск веб-сервера
    app.run(debug=True, host="127.0.0.1")


if __name__ == "__main__":
    main()

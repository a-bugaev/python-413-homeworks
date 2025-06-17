"""
HW 36. Flask API
test.py: запросы к каждому эндпоинту
"""

import os
from time import sleep
import re
from re import Match
from json import JSONDecodeError, dumps
import requests
from requests.models import Response


TIMEOUT = 1

responses: list[Response] = []
requests_data: list[dict] = [
    # @app.route("/masters")
    # ep_get_masters
    {"method": "get", "url": "http://127.0.0.1:5000/masters", "json": ""},
    {"method": "get", "url": "http://127.0.0.1:5000/mastes", "json": ""},
    # @app.route("/masters/<int:master_id>")
    # ep_get_master_by_id
    {"method": "get", "url": "http://127.0.0.1:5000/masters/1", "json": ""},
    {"method": "get", "url": "http://127.0.0.1:5000/masters/5", "json": ""},
    # @app.route("/masters", methods=["POST"])
    # ep_add_master
    {
        "method": "post",
        "url": "http://127.0.0.1:5000/masters",
        "json": dumps(
            {
                "first_name": "Имя",
                "last_name": "Нового",
                "middle_name": "Мастера",
                "phone": "И его номер телефона",
            }
        ),
    },
    {
        "method": "post",
        "url": "http://127.0.0.1:5000/masters",
        "json": dumps(
            {
                "first_name": "Имя",
                "middle_name": "Мастера",
                "phone": "Без фамилии",
            }
        ),
    },
    # @app.route("/masters/<int:master_id>", methods=["PUT"])
    # ep_update_master
    {
        "method": "put",
        "url": "http://127.0.0.1:5000/masters/3",
        "json": dumps({"phone": "88005553535"}),
    },
    {"method": "put", "url": "http://127.0.0.1:5000/masters/3", "json": ""},
    # @app.route("/masters/<int:master_id>", methods=["DELETE"])
    # ep_delete_master
    {"method": "delete", "url": "http://127.0.0.1:5000/masters/3", "json": ""},
    {"method": "delete", "url": "http://127.0.0.1:5000/masters/5", "json": ""},
    # @app.route("/appointments?sort_by=<string:sort_by>&direction=<string:direction>")
    # ep_get_appointments
    {"method": "get", "url": "http://127.0.0.1:5000/appointments", "json": ""},
    {
        "method": "get",
        "url": "http://127.0.0.1:5000/appointments?sort_by=master&direction=desc",
        "json": "",
    },
    # @app.route("/appointments/<int:appointment_id>")
    # ep_get_appointment_by_id
    {"method": "get", "url": "http://127.0.0.1:5000/appointments/1", "json": ""},
    {"method": "get", "url": "http://127.0.0.1:5000/appointments/three", "json": ""},
    # @app.route("/appointointments/master/<int:master_id>")
    # ep_get_appointments_by_master
    {"method": "get", "url": "http://127.0.0.1:5000/appointments/master/1", "json": ""},
    {"method": "get", "url": "http://127.0.0.1:5000/appointments/master/5", "json": ""},
    # @app.route("/appointments", methods=["POST"])
    # ep_add_appointment
    {
        "method": "post",
        "url": "http://127.0.0.1:5000/appointments",
        "json": dumps(
            {
                "client_name": "Имя",
                "client_phone": "Телефон",
                "comment": "Комментарий к записи",
                "master": "1",
            }
        ),
    },
    {
        "method": "post",
        "url": "http://127.0.0.1:5000/appointments",
        "json": dumps(
            {
                "client_name": "Имя",
                "client_phone": "Телефон",
                "comment": "Комментарий к записи",
                "master": "1",
                "status": "невалидный статус",
            }
        ),
    },
    # @app.route("/appointments/<int:appointment_id>", methods=["PUT"])
    # ep_update_appointment
    {
        "method": "put",
        "url": "http://127.0.0.1:5000/appointments/5",
        "json": dumps({"status": "Запись подтверждена"}),
    },
    {
        "method": "put",
        "url": "http://127.0.0.1:5000/appointments/5",
        "json": dumps({"несуществующий ключ": "новое значение"}),
    },
    # @app.route("/appointments/<int:appointment_id>", methods=["DELETE"])
    # ep_delete_appointment
    {"method": "delete", "url": "http://127.0.0.1:5000/appointments/5", "json": ""},
    {"method": "delete", "url": "http://127.0.0.1:5000/appointments/5", "json": ""},
]

for request_dict in requests_data:

    # с временным промежутком выполнить верные
    # и неверные запросы к каждому эндпоинту, Response объекты собрать в список

    response = requests.request(
        request_dict["method"], request_dict["url"], json=request_dict["json"], timeout=TIMEOUT
    )
    responses.append(response)
    sleep(0.25)
    print(".", end=" ", flush=True)

OUT_TEXT = "\n"

if not os.path.isdir('./test_htmls'):
    os.mkdir('./test_htmls')

for idx, response in enumerate(responses):

    # создать html файл если текст доступен
    if response.text:
        pattern = re.compile(r"http://[^\/]+/(.+)")
        url_path = re.match(pattern, response.url)
        if isinstance(url_path, Match):
            url_path_clean = url_path.group(1).replace("/", "_")
            with open(
                f"./test_htmls/[{idx}][{response.request.method}]_{url_path_clean}.html",
                "w",
                encoding="utf-8",
            ) as f:
                f.write(response.text)

    # вывести в консоль данные ответа и json при наличии
    try:
        JSON = response.json()
    except JSONDecodeError:
        JSON = ""
    OUT_TEXT += f"""
        idx: {idx}
        method: {response.request.method}
        url: {response.url}
        status_code: {response.status_code}
        text: {'<file saved to tests_html>' if response.text else '<not available>'}
        json:
        {str(JSON) if str(JSON) else '<not available>'}
    """.replace(
        "    ", ""
    )

print(OUT_TEXT)

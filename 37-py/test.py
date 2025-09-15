"""
HW 36. Flask API
test.py: запросы к каждому эндпоинту

######

hw 37: каждый запрос теперь делается с админским,
пользовательским и неправильным ключами
+ запрос как раньше без ключа

"""

from time import sleep
from json import JSONDecodeError, dumps
from copy import deepcopy
import requests

REQ_TIMEOUT = 1

SLEEP_S = 0.1

REQUESTS_DATA: list[dict] = [
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

ADMIN_API_KEY = "uUXf(pvDD)*Qkj(Js@puV9vVAHwst9Ry"
USER_API_KEY = "x4Y_%$b7z(Mvec_anrK82^vyTy^)8TvS"
DUMMY_API_KEY = "letmein"

# модификация списка запросов

REQUESTS_AS_ADMIN = deepcopy(REQUESTS_DATA)
for request_dict in REQUESTS_AS_ADMIN:
    request_dict["headers"] = {"API-KEY": ADMIN_API_KEY}

REQUESTS_AS_USER = deepcopy(REQUESTS_DATA)
for request_dict in REQUESTS_AS_USER:
    request_dict["headers"] = {"API-KEY": USER_API_KEY}

REQUESTS_AS_DUMMY = deepcopy(REQUESTS_DATA)
for request_dict in REQUESTS_AS_DUMMY:
    request_dict["headers"] = {"API-KEY": DUMMY_API_KEY}


def make_reqs(reqs_data):
    """
    сделать запросы и вывести результат в консоль
    """

    responses = []

    for request_dict in reqs_data:

        # с временным промежутком выполнить верные
        # и неверные запросы к каждому эндпоинту, Response объекты собрать в список

        if "headers" in request_dict:
            r_headers = request_dict["headers"]
        else:
            r_headers = None

        response = requests.request(
            request_dict["method"],
            request_dict["url"],
            headers=r_headers,
            json=request_dict["json"],
            timeout=REQ_TIMEOUT,
        )
        responses.append(response)
        sleep(SLEEP_S)
        print(".", end=" ", flush=True)

    out_text = ''

    for idx, response in enumerate(responses):
        # вывести в консоль данные ответа и json при наличии
        try:
            r_json = response.json()
        except JSONDecodeError:
            r_json = ""
        out_text += f"""
            idx: {idx}
            method: {response.request.method}
            url: {response.url}
            status_code: {response.status_code}
            json:
            {str(r_json) if str(r_json) else '<not available>'}
        """.replace(
            "    ", ""
        )

    return out_text


print_str = f"""

БЕЗ КЛЮЧА       ###############################################################

{make_reqs(REQUESTS_DATA)}

КЛЮЧ АДМИНА     ###############################################################

{make_reqs(REQUESTS_AS_ADMIN)}

КЛЮЧ ЮЗЕРА      ###############################################################

{make_reqs(REQUESTS_AS_USER)}

НЕВЕРНЫЙ КЛЮЧ   ###############################################################

{make_reqs(REQUESTS_AS_DUMMY)}
"""

with open("./test.txt", "w", encoding="utf-8") as f:
    f.write(print_str)

print(print_str)

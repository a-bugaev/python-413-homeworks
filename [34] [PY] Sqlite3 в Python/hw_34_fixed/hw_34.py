"""
HW 34: sqlite3
"""

import os
import sqlite3
import pprint

DB_FILE = "./barbershop.db"
SQL_FILE = "./barbershop.sql"


def read_sql_file(filepath: str) -> str:
    """
    Reads the contents of a SQL file and returns it as a string
    """
    with open(filepath, "r", encoding="utf-8") as sql_file:
        return sql_file.read()


def execute_script(conn, script: str) -> None:
    """
    Executes a script in the given database connection
    """
    cursor = conn.cursor()
    cursor.executescript(script)
    conn.commit()
    cursor.close()


def find_master_id_by_name(conn, master_name_fio: str) -> int:
    """
    Finds a master by name
    """
    last_name, first_name, middle_name = master_name_fio.split(" ")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM masters WHERE last_name=? AND first_name=? AND middle_name=?",
        (last_name, first_name, middle_name),
    )

    fetch_out = cursor.fetchall()

    if len(fetch_out) == 0:
        raise ValueError(f"Master with name {master_name_fio} not found")
    if not isinstance(fetch_out[0][0], int):
        raise ValueError(f"Master with name {master_name_fio} has not id")

    cursor.close()

    return fetch_out[0][0]


def find_master_name_by_id(conn, master_id: int) -> str:
    """
    Finds a master name by id
    """

    cursor = conn.cursor()
    cursor.execute(
        "SELECT last_name, first_name, middle_name FROM masters WHERE id=?",
        (str(master_id)),
    )

    fetch_out = cursor.fetchall()

    if len(fetch_out) == 0:
        raise ValueError(f"Master with id {master_id} not found")

    if not any(isinstance(name_part, str) for name_part in fetch_out[0]):
        raise ValueError(f"Data type error for master with id {master_id}")

    cursor.close()

    return " ".join(fetch_out[0])


def find_service_id_by_name(conn, service_title: str) -> int:
    """
    Finds a service by title
    """
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM services WHERE title=?", (service_title,))

    fetch_out = cursor.fetchall()

    if len(fetch_out) == 0:
        raise ValueError(f"Service with name {service_title} not found")
    if not isinstance(fetch_out[0][0], int):
        raise ValueError(f"Service with name {service_title} has not id")

    cursor.close()

    return fetch_out[0][0]


def find_service_name_by_id(conn, service_id: int) -> str:
    """
    Finds a service title by id
    """
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM services WHERE id=?", (str(service_id),))

    fetch_out = cursor.fetchall()

    if len(fetch_out) == 0:
        raise ValueError(f"Service with id {service_id} not found")
    if not isinstance(fetch_out[0][0], str):
        raise ValueError(f"Data type error for service with id {service_id}")

    cursor.close()

    return fetch_out[0][0]


def find_service_ids_for_appointment(conn, appointment_id: int) -> list[int]:
    """
    Finds all services by appointment id
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT service_id FROM appointments_services WHERE appointment_id=?",
        (appointment_id,),
    )

    fetch_out = cursor.fetchall()

    if len(fetch_out) == 0:
        raise ValueError(f"No services for appointment with id {appointment_id}")

    services_ids = []
    for service in fetch_out:
        if not isinstance(service[0], int):
            raise ValueError("Index data type error")
        services_ids.append(service[0])

    return services_ids


def find_appointments_by_phone(conn, phone: str) -> list[tuple]:
    """
    Finds an appointment by phone number
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM appointments WHERE phone=?", (phone,))
    appointments = cursor.fetchall()
    cursor.close()

    # appontment tuple structure:
    # 0 - id
    # 1 - client_name
    # 2 - phone
    # 3 - Date
    # 4 - comment
    # 5 - master_id
    # 6 - status

    hr_list: list[tuple] = []

    for appointment in appointments:

        master_name = find_master_name_by_id(conn, int(appointment[5]))

        services_list: list[str] = []
        for service_id in find_service_ids_for_appointment(conn, appointment[0]):
            services_list.append(find_service_name_by_id(conn, service_id))
        services_hr = ", ".join(services_list)

        hr_tuple = (
            f"Appointment ID: {appointment[0]}",
            f"Client name: {appointment[1]}",
            f"Client phone number: {appointment[2]}",
            f"DateTime of creation: {appointment[3]}",
            f"Comment: {appointment[4]}",
            f"Master name: {master_name}",
            f"Services: {services_hr}",
            f"Status: {appointment[6]}",
        )

        hr_list.append(hr_tuple)

    return hr_list


def find_appointments_by_comment(conn, comment_part: str) -> list[tuple]:
    """
    Finds appointments by comment part
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM appointments WHERE comment LIKE ?",
        ("%" + comment_part + "%",),
    )
    appointments = cursor.fetchall()
    cursor.close()

    # appontment tuple structure:
    # 0 - id
    # 1 - client_name
    # 2 - phone
    # 3 - Date
    # 4 - comment
    # 5 - master_id
    # 6 - status

    hr_list: list[tuple] = []

    for appointment in appointments:
        master_name = find_master_name_by_id(conn, int(appointment[5]))

        services_list: list[str] = []
        for service_id in find_service_ids_for_appointment(conn, appointment[0]):
            services_list.append(find_service_name_by_id(conn, service_id))
        services_hr = ", ".join(services_list)

        hr_tuple = (
            f"Appointment ID: {appointment[0]}",
            f"Client name: {appointment[1]}",
            f"Client phone number: {appointment[2]}",
            f"DateTime of creation: {appointment[3]}",
            f"Comment: {appointment[4]}",
            f"Master name: {master_name}",
            f"Services: {services_hr}",
            f"Status: {appointment[6]}",
        )

        hr_list.append(hr_tuple)

    return hr_list


def create_appointment(
    conn,
    client_name_fio: str,
    client_phone: str,
    master_name_fio: str,
    services_list: list[str],
    comment: str,
) -> int:
    """
    Creates a new appointment
    """

    # Find the master ID
    master_id = find_master_id_by_name(conn, master_name_fio)
    if not master_id:
        raise ValueError(f"Master with name {master_name_fio} not found")

    # Find the services IDs
    service_ids = []
    for service_title in services_list:
        service_id = find_service_id_by_name(conn, service_title)
        if not service_id:
            raise ValueError(f"Service with title {service_title} not found")
        service_ids.append(service_id)

    # Insert the appointment
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO appointments (client_name, phone, master_id, comment, status) VALUES (?, ?, ?, ?, 'Подана заявка')",
        (
            client_name_fio,
            client_phone,
            master_id,
            comment,
        ),
    )
    appointment_id = cursor.lastrowid

    # Junction table insertion: appointments_services
    for service_id in service_ids:
        cursor.execute(
            "INSERT INTO appointments_services (appointment_id, service_id) VALUES (?, ?)",
            (appointment_id, service_id),
        )

    conn.commit()
    cursor.close()
    return appointment_id


if __name__ == "__main__":
    # Tests

    os.chdir(os.path.dirname(__file__))

    # Delete the database file if it exists
    try:
        os.remove(DB_FILE)
    except FileNotFoundError:
        pass

    conn_inst = sqlite3.connect(DB_FILE)
    sql_str = read_sql_file(SQL_FILE)
    execute_script(conn_inst, sql_str)

    print("Найти запись по номеру телефона 2233445566:")
    pprint.pprint(find_appointments_by_phone(conn_inst, "2233445566"))
    print("")

    print("Найти запись по частичному совпадению комментария ('Третьего'):")
    pprint.pprint(find_appointments_by_comment(conn_inst, "Третьего"))
    print("")

    print("Найти ID мастера по ФИО Иванова Татьяна Михайловна:")
    print(find_master_id_by_name(conn_inst, "Иванова Татьяна Михайловна"), "\n")

    print("Найти ID услуги по названию Стрижка мужская модельная:")
    print(find_service_id_by_name(conn_inst, "Стрижка мужская модельная"), "\n")

    print("Создать запись:")
    print(
        create_appointment(
            conn_inst,
            "Иванов Иван Иванович",
            "89101234567",
            "Сидоров Василий Петрович",
            ["Стрижка мужская модельная", "Стайлинг бороды"],
            "коммент",
        ),
        "\n",
    )

    conn_inst.close()

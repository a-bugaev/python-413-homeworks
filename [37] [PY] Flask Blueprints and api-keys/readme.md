### запустить сервер:
```bash
python -c "import hw_37; hw_37.run()"
```

### запустить сервер с пересозданием .db файла для тестов:
```bash
python -c "import hw_37; hw_37.run()" --test
```

### тест:

```bash
python ./test.py
```

### авторизация:

```bash
    curl -H "API-KEY: <--your-key-->" <url>
```

### эндпоинты:

| Маршрут | Метод | Администратор | Обычный пользователь |
|---------|-------|---------------|---------------------|
| `/masters` | GET | <center>✅<center/> | <center>✅<center/> |
| `/masters/<master_id>` | GET | <center>✅<center/> | <center>✅<center/> |
| `/masters` | POST | <center>✅<center/> | <center>❌<center/> |
| `/masters/<master_id>` | PUT | <center>✅<center/> | <center>❌<center/> |
| `/masters/<master_id>` | DELETE | <center>✅<center/> | <center>❌<center/> |
| `/appointments` | GET | <center>✅<center/> | <center>✅<center/> |
| `/appointments/<appointment_id>` | GET | <center>✅<center/> | <center>✅<center/> |
| `/appointments/master/<master_id>` | GET | <center>✅<center/> | <center>✅<center/> |
| `/appointments` | POST | <center>✅<center/> | <center>❌<center/> |
| `/appointments/<appointment_id>` | PUT | <center>✅<center/> | <center>❌<center/> |
| `/appointments/<appointment_id>` | DELETE | <center>✅<center/> | <center>❌<center/> |

### создание эндпоинта/блюпринта:

 - структура папок и фалов аналогично существующим

 - авторизация:

    ```python
        from hw_37.auth import auth_check

        ...

        @bp_name.route("/path", methods=["GET"])
        def ep_method() -> tuple[str, int, dict]:
            auth_result = auth_check(request.headers.get("API-KEY"), request.endpoint)
            if auth_result is not True:
                return auth_result
    ```

 - внести правила в auth.ACCESS_TABLE

### [Git](https://github.com/a-bugaev/python-413-homeworks)
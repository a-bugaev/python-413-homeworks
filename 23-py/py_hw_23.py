"""
    23. Декораторы
"""

from typing import Callable, Any
import re
import os
import csv

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_PATH)

#   Часть 1: Декоратор для валидации пароля


def password_checker(
    pswd_arg_name: str = "password") -> Callable:
    """Позволяет передать декоратору аргументы"""

    def decorator_factory(func: Callable) -> Callable:
        """Проверяет сложность пароля."""

        def wrapper(*args, **kwargs):
            password = kwargs[pswd_arg_name]
            if len(password) < 8:
                raise ValueError("Password is too short")
            if not any(char.isdigit() for char in password):
                raise ValueError("Password must contain at least one digit")
            if not any(char.isupper() for char in password):
                raise ValueError("Password must contain at least one uppercase letter")
            if not any(char.islower() for char in password):
                raise ValueError("Password must contain at least one lowercase letter")
            if not re.search(r"[^a-zA-Z0-9]", password):
                raise ValueError("Password must contain at least one special character")
            return func(*args, **kwargs)

        return wrapper

    return decorator_factory


@password_checker(pswd_arg_name="custom_name_for_password_argument")
def register_user(username: str, custom_name_for_password_argument: str) -> Any:
    """Регистрирует пользователя."""
    print(
        f"User {username} registered with password {custom_name_for_password_argument}"
    )


# call register_user with different passwords,
# including those which meets all conditions and
# those which don't meets at least one condition

testing_data = [
    {"username": "user01", "custom_name_for_password_argument": "passwor"},
    {"username": "user02", "custom_name_for_password_argument": "password"},
    {"username": "user04", "custom_name_for_password_argument": "PASSWORD1"},
    {"username": "user03", "custom_name_for_password_argument": "password1"},
    {"username": "user05", "custom_name_for_password_argument": "Password1"},
    {"username": "user05", "custom_name_for_password_argument": "Password1&"},
    {"username": "user06", "custom_name_for_password_argument": r"*fSP(2rv*%GOtO_6"},
]

for case in testing_data:
    try:
        register_user(**case)
    except ValueError as e:
        print(f"Error: {e}")

# Часть 2: Декораторы для валидации данных

def password_validator(
    pswd_arg_name: str = "password",
    length: int = 8,
    digits: int = 1,
    uppercase: int = 1,
    lowercase: int = 1,
    special_chars: int = 1) -> Callable:
    """Проверяет сложность пароля по заданным параметрам"""

    def decorator_factory(func: Callable) -> Callable:

        def wrapper(*args, **kwargs):
            password = kwargs[pswd_arg_name]
            min_length = length
            min_digits = digits
            min_uppercase = uppercase
            min_lowercase = lowercase
            min_special_chars = special_chars
            if len(password) < min_length:
                raise ValueError(f"Password must be at least {min_length} characters long")
            if sum(char.isdigit() for char in password) < min_digits:
                raise ValueError(f"Password must contain at least {min_digits} digits")
            if sum(char.isupper() for char in password) < min_uppercase:
                raise ValueError(
                    f"Password must contain at least {min_uppercase} uppercase letters")
            if sum(char.islower() for char in password) < min_lowercase:
                raise ValueError(
                    f"Password must contain at least {min_lowercase} lowercase letters")
            if len(re.findall(r"[^a-zA-Z0-9]", password)) < min_special_chars:
                raise ValueError(
                    f"Password must contain at least {min_special_chars} special characters")
            return func(*args, **kwargs)

        return wrapper

    return decorator_factory

def username_validator(username_arg_name: str = 'username') -> Callable:
    """ Проверяет, что в имени пользователя отсутствуют пробелы. """
    def decorator_factory(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            if ' ' in kwargs[username_arg_name]:
                raise ValueError("Username must not contain spaces")
            return func(*args, **kwargs)
        return wrapper
    return decorator_factory

@username_validator(username_arg_name = "user")
@password_validator(pswd_arg_name="passwd",
                    length=10,
                    digits=2,
                    uppercase=2,
                    lowercase=2,
                    special_chars=2)
def register_user_part_2(user: str, passwd: str) -> Any:
    """ Дозаписывает имя пользователя и пароль в CSV файл. """
    with open("users.csv", "a", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([user, passwd])
    print(
        f"User {user} registered with password {passwd}"
    )

# call register_user with different passwords,
# including those which meets all conditions and
# those which don't meets at least one condition

testing_data_part_2 = [
    {"user": "user07", "passwd": "passwordd"},
    {"user": "user08", "passwd": "passwordd1"},
    {"user": "user09", "passwd": "passwordd11"},
    {"user": "user11", "passwd": "pASSWORDD11"},
    {"user": "user10", "passwd": "PAsswordd11"},
    {"user": "user12", "passwd": "PAssword12&#"},
    {"user": "user13", "passwd": r"*fSP(2rv*%GOtO_6"},
    {"user": "user 14", "passwd": r"*fSP(2rv*%GOtO_6"},
]

for case in testing_data_part_2:
    try:
        register_user_part_2(**case)
    except ValueError as e:
        print(f"Error: {e}")

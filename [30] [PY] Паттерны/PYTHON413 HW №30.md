---
project: "[[Академия TOP]]"
journal: "[[PYTHON413]]"
tags:
  - PYTHON413
date: 2025-04-05
type:
  - home work
hw_num: 30
topic: "В этом задании вы на практике освоите два шаблона проектирования: **Стратегия** и **Фасад**.  Ваша задача — создать систему для проверки палиндромов, где **Стратегия** будет отвечать за выбор способа проверки, а **Фасад** — за упрощение взаимодействия с пользователем."
hw_theme:
  - ООП
  - python
  - Стратегия
  - Фасад
  - Палиндром
st_group: python 413
links:
  - "[[PYTHON412 HW №31]]"
  - "[[PYTHON413 HW №28]]"
---
# Домашнее задание 📃  
**Применение паттернов 'Стратегия' и 'Фасад' в проверке палиндромов**

## Краткое содержание  
В этом задании вы на практике освоите два шаблона проектирования: **Стратегия** и **Фасад**.  
Ваша задача — создать систему для проверки палиндромов, где **Стратегия** будет отвечать за выбор способа проверки, а **Фасад** — за упрощение взаимодействия с пользователем.

>[!info]
>### Технологии: 🦾
>- Python  
>- ООП  
>- Паттерны проектирования: Стратегия и Фасад

## Задание 👷‍♂️

### Описание классов и их функциональности

1. **PalindromeStrategy**  
   - Абстрактный интерфейс для всех стратегий проверки палиндромов.
   - Методы:
     - `is_palindrome(self, text: str) -> bool`  
       Принимает строку и возвращает `True`, если строка является палиндромом в рамках выбранной стратегии.

2. **SingleWordPalindrome**  
   - Конкретная реализация стратегии для проверки **одиночных слов**.
   - Методы:
     - `is_palindrome(self, text: str) -> bool`  
       Проверяет, является ли отдельное слово палиндромом (без учета регистра).

3. **MultiWordPalindrome**  
   - Конкретная реализация стратегии для проверки **многословных выражений**.
   - Методы:
     - `is_palindrome(self, text: str) -> bool`  
       Проверяет, является ли выражение палиндромом, игнорируя пробелы и регистр.

4. **PalindromeContext**  
   - Класс, отвечающий за использование текущей стратегии.
   - Атрибуты:
     - `strategy: PalindromeStrategy` — текущая выбранная стратегия.
   - Методы:
     - `set_strategy(self, strategy: PalindromeStrategy) -> None`  
       Позволяет установить новую стратегию.
     - `check(self, text: str) -> bool`  
       Проверяет, является ли текст палиндромом, используя установленную стратегию.

5. **PalindromeFacade**  
   - Фасад для упрощения работы с проверкой палиндромов.
   - Атрибуты:
     - `context: PalindromeContext` — экземпляр `PalindromeContext`.
   - Методы:
     - `check_palindrome(self, text: str) -> bool`  
       Определяет, какое правило проверки применить (слово или выражение) и проводит проверку через `PalindromeContext`.
   
>[!info]
>### Логика работы через Фасад:
>- Если переданный текст состоит из одного слова — используется стратегия `SingleWordPalindrome`.
>- Если в тексте несколько слов — используется стратегия `MultiWordPalindrome`.

## Дополнительные указания

- **Аннотации типов:**  
  Во всех методах используйте аннотации типов.
  
- **Проверка палиндромов:**  
  При проверке игнорируйте регистр. В многословных выражениях игнорируйте также пробелы.

- **Фасад:**  
  В фасаде реализуйте автоматический выбор стратегии на основе количества слов в строке.

### Таблица классов и методов

| Класс                  | Методы                                                      | Описание                                                                 |
| ---------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `PalindromeStrategy`   | `is_palindrome(self, text: str) -> bool`                     | Абстрактный метод для проверки палиндрома                                |
| `SingleWordPalindrome` | `is_palindrome(self, text: str) -> bool`                     | Проверка палиндрома для одного слова                                     |
| `MultiWordPalindrome`  | `is_palindrome(self, text: str) -> bool`                     | Проверка палиндрома для выражения                                         |
| `PalindromeContext`    | `set_strategy(self, strategy: PalindromeStrategy) -> None`   | Установка новой стратегии                                                |
|                        | `check(self, text: str) -> bool`                             | Проверка текста через установленную стратегию                           |
| `PalindromeFacade`     | `check_palindrome(self, text: str) -> bool`                  | Упрощённый интерфейс для проверки палиндромов через контекст             |

---

>[!warning]
>### Критерии проверки 👌
>1. **Корректная реализация паттернов:**  
>   Реализованы оба паттерна — `Стратегия` и `Фасад`.
>
>2. **Качество кода:**  
>   Код чистый, аккуратный, с корректными названиями классов и методов.
>
>3. **Логика проверки:**  
>   Правильный выбор стратегии на основе количества слов в строке.
>
>4. **Документирование:**  
>   Во всех классах и методах присутствуют аннотации типов.
>
>5. **Формат сдачи:**  
>   Сдайте работу в виде одного файла `.py`, содержащего все классы.

---

## Пример использования

 Вот пример тестового скрипта, который можно добавить в конец файла или выдать студентам для самостоятельной проверки работы системы:

```python
if __name__ == "__main__":
    facade = PalindromeFacade()
    
    # Тест 1: Одиночное слово-палиндром
    word = "Racecar"
    print(f"'{word}' — палиндром? {facade.check_palindrome(word)}")  # True

    # Тест 2: Одиночное слово не палиндром
    word = "Python"
    print(f"'{word}' — палиндром? {facade.check_palindrome(word)}")  # False

    # Тест 3: Многословное выражение-палиндром
    phrase = "A man a plan a canal Panama"
    print(f"'{phrase}' — палиндром? {facade.check_palindrome(phrase)}")  # True

    # Тест 4: Многословное выражение не палиндром
    phrase = "Hello World"
    print(f"'{phrase}' — палиндром? {facade.check_palindrome(phrase)}")  # False

    # Тест 5: Одно слово с разными регистрами
    word = "Deified"
    print(f"'{word}' — палиндром? {facade.check_palindrome(word)}")  # True

    # Тест 6: Сложная фраза с пробелами
    phrase = "Was it a car or a cat I saw"
    print(f"'{phrase}' — палиндром? {facade.check_palindrome(phrase)}")  # True
```

---

### Пояснения:
- Скрипт автоматически создаёт экземпляр `PalindromeFacade`.
- Проверяет несколько разных случаев:
  - одиночные слова (палиндромы и не палиндромы),
  - многословные выражения (с пробелами),
  - корректность работы без учета регистра,
  - правильный выбор стратегии (`SingleWordPalindrome` или `MultiWordPalindrome`).
  
>💡 **Важно:** перед запуском убедись, что все классы (`PalindromeStrategy`, `SingleWordPalindrome`, `MultiWordPalindrome`, `PalindromeContext`, `PalindromeFacade`) корректно реализованы в файле.

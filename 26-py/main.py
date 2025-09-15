"""
pip install pillow pillow-heif
"""

import os
from PIL import Image
from pillow_heif import register_heif_opener

QUALITY: int = 50  # Можно настроить качество сжатия


class ImageCompressor:
    """
    Класс для сжатия изображений и обработки директорий.
    """

    def __init__(self, quality: int = 50):
        self.__quality = quality
        self.supported_formats = (".jpg", ".jpeg", ".png")

    @property
    def quality(self) -> int:
        """
        quality getter
        """
        return self.__quality

    @quality.setter
    def quality(self, value: int) -> None:
        """
        qulity setter + validation
        """
        if not isinstance(value, int) or value < 1 or value > 100:
            raise ValueError("Quality must be an integer between 1 and 100.")
        self.__quality = value

    def compress_image(self, input_path: str, output_path: str) -> None:
        """
        Сжимает изображение и сохраняет его в формате HEIF.
        """
        with Image.open(input_path) as img:
            img.save(output_path, "HEIF", quality=self.quality)

    def process_directory(self, directory: str) -> None:
        """
        Обрабатывает все изображения в указанной директории и её поддиректориях.

        Args:
            directory (str): Путь к директории для обработки.

        Returns:
            None
        """
        for root, _, files in os.walk(directory):
            for file in files:
                # Проверяем расширение файла
                if file.lower().endswith(self.supported_formats):
                    input_path = os.path.join(root, file)
                    output_path = os.path.splitext(input_path)[0] + ".heic"
                    self.compress_image(input_path, output_path)


def main(input_path: str) -> None:
    """
    Основная функция программы. Обрабатывает входной путь и запускает сжатие изображений.

    Args:
        input_path (str): Путь к файлу или директории для обработки.

    Returns:
        None
    """
    register_heif_opener()
    input_path = input_path.strip('"')  # Удаляем кавычки, если они есть

    image_compressor_instance = ImageCompressor()

    if os.path.exists(input_path):
        if os.path.isfile(input_path):
            # Если указан путь к файлу, обрабатываем только этот файл
            print(f"Обрабатываем файл: {input_path}")
            output_path = os.path.splitext(input_path)[0] + ".heic"
            image_compressor_instance.compress_image(input_path, output_path)
        elif os.path.isdir(input_path):
            # Если указан путь к директории, обрабатываем все файлы в ней
            print(f"Обрабатываем директорию: {input_path}")
            image_compressor_instance.process_directory(input_path)
            # Функция process_directory рекурсивно обойдет все поддиректории
            # и обработает все поддерживаемые изображения
    else:
        print("Указанный путь не существует")


if __name__ == "__main__":
    user_input: str = input("Введите путь к файлу или директории: ")
    main(user_input)

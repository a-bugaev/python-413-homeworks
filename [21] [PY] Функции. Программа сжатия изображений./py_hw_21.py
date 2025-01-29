"""
Домашнее задание №21

Оптимизатор изображений v2.0
"""

import os
from PIL import Image
import pillow_heif
import pillow_avif
from tqdm import tqdm

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "JPG", "JPEG"}
DEFAULT_QUALITY = 40
DEFAULT_FORMAT = "AVIF"
AVAILABLE_FORMATS = {"WEBP", "HEIF", "AVIF"}


def check_extension(image_path:str, allowed:list = None) -> bool:
    """ check if file format sapported;
    also can just check if file has ext from 'allowed' list """

    if not allowed:
        allowed = ALLOWED_EXTENSIONS
    ext = os.path.splitext(image_path)[1][1:].lower()
    for allowed_ext in allowed:
        if not ext.lower() in allowed_ext.lower():
            return False
    return True


def get_images_paths(
    source_path: str, target_exts: list = None) -> list[str]:
    """ recursively gets all images paths from source_path,
    checking them for ext """

    if not target_exts:
        target_exts = ALLOWED_EXTENSIONS
    images_paths = []
    if os.path.isfile(source_path):
        check_extension(source_path, target_exts)

    if os.path.isdir(source_path):
        for root, dirs, files in os.walk(source_path):
            for file in files:
                if check_extension(file):
                    images_paths.append(os.path.join(root, file))

    return images_paths


def get_images_disk_space(images_paths: list[str]) -> float:
    """ returns total disk space used by images in MB """
    _bytes = 0
    for image_path in images_paths:
        _bytes += os.stat(image_path).st_size
    return _bytes / (1024**2)


def compress_image(
    image_path: str, output_format: str = DEFAULT_FORMAT, quality: int = DEFAULT_QUALITY
):
    """ compress image with Pillow """
    image = Image.open(image_path)

    if output_format == "WEBP":
        image.save(
            f"{os.path.splitext(image_path)[0]}.webp", format="WEBP", quality=quality
        )

    if output_format == "HEIF":
        image.save(f"{os.path.splitext(image_path)[0]}.heif", quality=quality)

    if output_format == "AVIF":
        image.save(f"{os.path.splitext(image_path)[0]}.avif", quality=quality)


def main() -> None:
    """ Manages the image processing and progress output,
    checks user input also"""
    while True:
        source_path = input("Введите путь к изображению или директории: ")
        if not (os.path.isfile(source_path) or os.path.isdir(source_path)):
            print("Неверный путь")
            continue
        else:
            break

    while True:
        output_format = input(
            """Введите формат выходного файла (AVIF, WEBP, HEIF):
                Нажмите Enter для AVIF по умолчанию"""
        )
        if output_format not in AVAILABLE_FORMATS:
            print("Неверный формат")
            continue
        else:
            break

    while True:
        quality = input(
            """Введите качество (от 1 до 100):
                Нажмите Enter для 40 по умолчанию"""
        )
        if not quality.isdigit() or int(quality) < 1 or int(quality) > 100:
            print("Число от 1 до 100")
            continue
        else:
            break

    images_paths = get_images_paths(source_path)

    size_before = get_images_disk_space(images_paths)

    for i in tqdm(range(size_before * 1024), desc="Compressing... "):
        for image_path in images_paths:
            compress_image(image_path, output_format, int(quality))
            i += get_images_disk_space([image_path])

    size_after = get_images_disk_space(get_images_paths(source_path, [output_format]))

    print(f"Исходный размер: {size_before:.2f} МБ")
    print(f"Текущий размер: {size_after:.2f} МБ")
    print(f"Разница: {size_before - size_after:.2f} МБ")
    print(
        f"Процент сжатия: {round((size_before - size_after) / size_before * 100, 2)}%"
    )

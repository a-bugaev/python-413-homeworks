"""
Домашнее задание №21

Оптимизатор изображений v2.0
"""

import sys
import os
from time import sleep
import pillow_avif
from PIL import Image
from pillow_heif import from_pillow as heif_from_pillow
from tqdm import tqdm


ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "JPG", "JPEG"}
DEFAULT_QUALITY = 40
DEFAULT_FORMAT = "AVIF"
AVAILABLE_FORMATS = {"WEBP", "HEIF", "AVIF"}


def check_extension(image_path: str, allowed: list = None) -> bool:
    """check if file format sapported;
    also can just check if file has ext from 'allowed' list"""

    if not allowed:
        allowed = ALLOWED_EXTENSIONS
    ext = os.path.splitext(image_path)[1][1:].lower()
    for item in allowed:
        if item.lower() == ext.lower():
            return True

    return False


def get_images_paths(source_path: str, target_exts: list = None) -> list[str]:
    """recursively gets all images paths from source_path,
    checking them for ext"""

    if not target_exts:
        target_exts = ALLOWED_EXTENSIONS

    images_paths = []

    if os.path.isfile(source_path):
        if check_extension(source_path, target_exts):
            images_paths.append(source_path)

    if os.path.isdir(source_path):
        for dirpath, dirnames, filenames in os.walk(source_path):
            for filename in filenames:
                abspath = os.path.join(dirpath, filename)
                if check_extension(abspath, target_exts):
                    images_paths.append(abspath)

    return images_paths


def get_images_disk_space_mb(images_paths: list[str]) -> float:
    """returns total disk space used by images in MB"""
    _bytes = 0
    for image_path in images_paths:
        _bytes += os.stat(image_path).st_size
    return _bytes / (1024**2)


def compress_image(
    image_path: str, output_format: str = DEFAULT_FORMAT, quality: int = DEFAULT_QUALITY):
    """compress image with Pillow"""
    image = Image.open(image_path)
    output_format = output_format.upper()

    if output_format == "WEBP":
        image.save(
            f"{os.path.splitext(image_path)[0]}.webp", format="WEBP", quality=quality
        )

    if output_format == "HEIF":
        heif_from_pillow(image).save(
            f"{os.path.splitext(image_path)[0]}.heif", quality=quality
        )

    if output_format == "AVIF":
        image.save(f"{os.path.splitext(image_path)[0]}.avif", quality=quality)


def main() -> None:
    """Manages the image processing and progress output,
    checks user input also"""
    while True:
        source_path = input("Введите путь к изображению или директории: ")
        if os.path.isfile(source_path) or os.path.isdir(source_path):
            break

    while True:
        output_format = input(
            "Введите формат выходного файла (AVIF, WEBP, HEIF)\n"
            + "(Нажмите Enter для AVIF по умолчанию): "
        )
        if not output_format:
            output_format = DEFAULT_FORMAT.lower()
            break
        check_passed = False
        for _format in AVAILABLE_FORMATS:
            if output_format.upper() == _format.upper():
                output_format = _format.lower()
                check_passed = True
                break
        if check_passed:
            break

    while True:
        quality = input(
            "Введите качество (от 1 до 100)\n" + "(Нажмите Enter для 40 по умолчанию): "
        )
        if not quality:
            quality = DEFAULT_QUALITY
            break
        if quality.isdigit() and int(quality) >= 1 and int(quality) <= 100:
            break

    images_paths = get_images_paths(source_path=source_path)

    size_before = get_images_disk_space_mb(images_paths)

    progress_in_kb = int(0)
    progressbar = tqdm(
        desc="Compressing...", unit="KB", total=round(size_before * 1024)
    )

    for image_path in images_paths:
        compress_image(image_path, output_format, int(quality))
        sleep(0.5)
        progress_in_kb += round(get_images_disk_space_mb([image_path]) * 1024)
        progressbar.update(progress_in_kb)
    progressbar.close()

    size_after = get_images_disk_space_mb(
        get_images_paths(source_path, [output_format])
    )

    print(f"Исходный размер: {size_before:.2f} МБ")
    print(f"После сжатия: {size_after:.2f} МБ")
    print(f"Разница: {size_before - size_after:.2f} МБ")
    print(
        f"Процент сжатия: {round((size_before - size_after) / size_before * 100, 2)}%"
    )


main()

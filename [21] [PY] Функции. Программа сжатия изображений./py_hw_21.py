
"""
Домашнее задание №21

Оптимизатор изображений v2.0
"""

import os
import pillow_avif
from PIL import Image
from pillow_heif import HeifImagePlugin
import math

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'JPG', 'JPEG'}
DEFAULT_QUALITY = 40
DEFAULT_FORMAT = 'AVIF'
AVAILABLE_FORMATS = {'WEBP', 'HEIF', 'AVIF'}

def get_images_paths(source_path: str) -> list[str]:

def get_images_disk_space(images_paths: list[str]) -> float:
    _bytes = 0
    for image_path in images_paths:
        _bytes += os.stat(image_path).st_size
    return _bytes / (1024**2)

def compress_image(
    image_path: str,
    output_format: str = 'AVIF',
    quality: int = 40,
    output_dir: str) -> str:

def main() -> None:
    while True:
        source_path = input('Введите путь к изображению или директории: ')
        if not (os.path.isfile(source_path) or os.path.isdir(source_path)):
            print('Неверный путь')
            continue
        else:
            break
    
    while True:
        output_format = input('Введите формат выходного файла (AVIF, WEBP, HEIF): ')
        if output_format not in AVAILABLE_FORMATS:
            print('Неверный формат')
            continue
        else:
            break
    
    while True:
        quality = input('Введите качество (от 1 до 100): ')
        if not quality.isdigit() or int(quality) < 1 or int(quality) > 100:
            print('Число от 1 до 100')
            continue
        else:
            break
    
    while True:
        output_dir = input('Введите путь к директории для сохранения: ')
        if not os.path.isdir(output_dir):
            print('Неверный путь')
            continue
        else:
            break
    
    images_paths = get_images_paths(source_path)

    size_before = get_images_disk_space(images_paths)

    for i in tqdm(range(10000)):
        for image_path in images_paths:
            compress_image(image_path, output_format, int(quality), output_dir)
        pass

    size_after = get_images_disk_space(get_images_paths(output_dir))

    print(f'Исходный размер: {size_before:.2f} МБ')
    print(f'Текущий размер: {size_after:.2f} МБ')
    print(f'Разница: {size_before - size_after:.2f} МБ')
    print(f'Процент сжатия: {round((size_before - size_after) / size_before * 100, 2)}%')
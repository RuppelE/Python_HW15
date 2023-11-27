import os
import logging

# Настройка логирования
logging.basicConfig(filename='last.log', level=logging.INFO)

# Функция для получения информации о содержимом директории
def get_directory_info(directory_path):
    try:
        directory_content = os.listdir(directory_path)

        for item in directory_content:
            item_path = os.path.join(directory_path, item)
            is_directory = os.path.isdir(item_path)

            # Если это папка, то выводим ее имя и вызываем функцию рекурсивно
            if is_directory:
                logging.info(f'Папка: {item}')
                get_directory_info(item_path)
            # Если это файл, то выводим его имя и расширение
            else:
                name, extension = os.path.splitext(item)
                logging.info(f'Файл: {name}.{extension}')

    except Exception as e:
        logging.error(f'Ошибка при получении информации о содержимом директории: {str(e)}')

if __name__ == '__main__':
    import sys

    # Проверяем, что передан путь к директории
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите путь до директории")
    else:
        directory_path = sys.argv[1]
        get_directory_info(directory_path)
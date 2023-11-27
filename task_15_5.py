import argparse
import logging
from datetime import date, datetime
from collections import namedtuple

# Класс пользовательского исключения
class CustomException(Exception):
    "Пользовательское исключение для всех случаев:"
    pass

# Конфигурация логирования
logging.basicConfig(filename="task15_4.log", level=logging.DEBUG) 
logger = logging.getLogger("log")

# Словари для месяцев и дней недели
MONTH = {
    'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
    'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12
}
WEEKDAYS = {
    'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3,
    'пятница': 4, 'суббота': 5, 'воскресенье': 6
}

# Именованный кортеж для даты
DATE = namedtuple("DATE", "day month year")

# Функция для поиска и форматирования даты
def get_date(query):
    try:
        logger.info("START: %s", datetime.now())
        num_week, week_day, month = query.split()
        num_week = int(num_week.split("-")[0])
        week_day = WEEKDAYS.get(week_day)
        if week_day is None:
            raise CustomException("Неверный день недели! Пожалуйста, исправьте запрос.")
        month = MONTH.get(month)
        if month is None:
            raise CustomException("Неверный месяц! Пожалуйста, исправьте запрос.")
        
        count_week = 0
        return_date = None
        tuple_data = None
        
        for day in range(1, 31+1):
            new_date = date(year=datetime.now().year, month=month, day=day)
            if new_date.weekday() == week_day:
                count_week += 1
                if count_week == num_week:
                    return_date = new_date
                    tuple_data = DATE(return_date.day, return_date.month, return_date.year)
                    break
        
        if return_date is None:
            raise CustomException("Дата не найдена. Попробуйте изменить запрос.")
    
    except Exception as e:
        logger.error("Ошибка: %s", e)
        print("Ошибка! Подробности в лог-файле.")
    
    else:
        logger.info("Искомая дата: %s", tuple_data)
        print("Искомая дата: ", return_date)
    
    finally:
        logger.debug("Данные пользователя: %s", query)

# Тело программы
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Пользовательский запрос')
    parser.add_argument('-q', '--query', type=str, help='Введите запрос пользователя')
    args = parser.parse_args()
    
    if args.query:
        get_date(args.query)
    else:
        get_date(input("Введите текст (например: “1 четверг ноября”): "))
import datetime


class BirthDateException(Exception):
    def __init__(self, year, message=None):
        self.year = year
        self.message = message if message else f"Введенный год рождения {year} не соответсвует условиям"

    def __str__(self):
        return self.message


def calculate_age(birth_year):
    if 2023 < birth_year or birth_year < 1900:
        raise BirthDateException(birth_year)
    return datetime.datetime.now().year - birth_year


while True:
    birth_year = input('Введите год своего рождения!')
    if birth_year == 'q':
        break
    errors = {}
    try:
        age = calculate_age(int(birth_year))
    except Exception as e:
        errors = {'age': f'Во время выполнения произошла ошибка: {e}'}
    else:
        print(age)
    finally:
        if errors:
            print(errors)

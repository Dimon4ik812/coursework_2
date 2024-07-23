import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class FileAbstractClass(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def write_data(self, vacancies):
        """Абстрактный метод записи данных"""
        pass

    @abstractmethod
    def get_vacancies(self):
        """Абстрактный метод для"""
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(FileAbstractClass):
    def __init__(self, filename="data/vacancies.json"):
        self.filename = filename

    def write_data(self, vacancies):
        with open(self.filename, "w") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_vacancies(self) -> list:
        with open(self.filename) as file:
            data = json.load(file)
        vacancies = []
        for vacancy in data:
            vacancies.append(
                Vacancy(
                    name=vacancy["name"],
                    salary=vacancy["salary"],
                    url=vacancy["alternate_url"],
                    employer=vacancy["employer"]["name"],
                    requirement=vacancy["snippet"]["requirement"],
                    responsibility=vacancy["snippet"]["responsibility"],
                )
            )
        return vacancies

    def delete_vacancy(self):
        """Метод удаления данных из файла"""
        list_vacancies_del = []
        list_del = json.dumps(list_vacancies_del, ensure_ascii=False)
        with open(self.filename, "w", encoding="utf8") as f:
            f.write(list_del)

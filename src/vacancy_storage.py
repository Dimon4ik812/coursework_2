import json
import csv
import pandas as pd
from abc import ABC, abstractmethod
from typing import List, Dict

class VacancyStorage(ABC):
    """Абстрактный класс для работы с хранилищем вакансий."""

    @abstractmethod
    def add_vacancy(self, vacancy: Dict):
        """Добавить вакансию в хранилище."""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Dict = None) -> List[Dict]:
        """Получить вакансии из хранилища, используя заданные критерии."""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id: int):
        """Удалить вакансию из хранилища по ID."""
        pass

class JSONVacancyStorage(VacancyStorage):
    """Класс для работы с JSON-файлом для хранения вакансий."""

    def __init__(self, file_path: str = "data/vacancies.json"):
        self.file_path = file_path
        self.load_vacancies()

    def load_vacancies(self):
        """Загрузка вакансий из JSON-файла."""
        try:
            with open(self.file_path, "r") as f:
                self.vacancies = json.load(f)
        except FileNotFoundError:
            self.vacancies = []

    def save_vacancies(self):
        """Сохранение вакансий в JSON-файл."""
        with open(self.file_path, "w") as f:
            json.dump(self.vacancies, f, indent=4)

    def add_vacancy(self, vacancy: Dict):
        """Добавить вакансию в JSON-файл."""
        self.vacancies.append(vacancy)
        self.save_vacancies()

    def get_vacancies(self, criteria: Dict = None) -> List[Dict]:
        """Получить вакансии из JSON-файла, используя заданные критерии."""
        if criteria is None:
            return self.vacancies
        filtered_vacancies = []
        for vacancy in self.vacancies:
            match = True
            for key, value in criteria.items():
                if key not in vacancy or vacancy[key] != value:
                    match = False
                    break
            if match:
                filtered_vacancies.append(vacancy)
        return filtered_vacancies

    def delete_vacancy(self, vacancy_id: int):
        """Удалить вакансию из JSON-файла по ID."""
        self.vacancies = [vacancy for vacancy in self.vacancies if vacancy["id"] != vacancy_id]
        self.save_vacancies()

class CSVVacancyStorage(VacancyStorage):
    """Класс для работы с CSV-файлом для хранения вакансий."""

    def __init__(self, file_path: str = "data/vacancies.csv"):
        self.file_path = file_path
        self.load_vacancies()

    def load_vacancies(self):
        """Загрузка вакансий из CSV-файла."""
        try:
            with open(self.file_path, "r") as f:
                reader = csv.DictReader(f)
                self.vacancies = list(reader)
        except FileNotFoundError:
            self.vacancies = []

    def save_vacancies(self):
        """Сохранение вакансий в CSV-файл."""
        with open(self.file_path, "w", newline="") as f:
            fieldnames = self.vacancies[0].keys() if self.vacancies else ["id", "title", "link", "salary", "description"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.vacancies)

    def add_vacancy(self, vacancy: Dict):
        """Добавить вакансию в CSV-файл."""
        self.vacancies.append(vacancy)
        self.save_vacancies()

    def get_vacancies(self, criteria: Dict = None) -> List[Dict]:
        """Получить вакансии из CSV-файла, используя заданные критерии."""
        if criteria is None:
            return self.vacancies
        filtered_vacancies = []
        for vacancy in self.vacancies:
            match = True
            for key, value in criteria.items():
                if key not in vacancy or vacancy[key] != value:
                    match = False
                    break
            if match:
                filtered_vacancies.append(vacancy)
        return filtered_vacancies

    def delete_vacancy(self, vacancy_id: int):
        """Удалить вакансию из CSV-файла по ID."""
        self.vacancies = [vacancy for vacancy in self.vacancies if vacancy["id"] != vacancy_id]
        self.save_vacancies()

class ExcelVacancyStorage(VacancyStorage):
    """Класс для работы с Excel-файлом для хранения вакансий."""

    def __init__(self, file_path: str = "data/vacancies.xlsx", sheet_name: str = "Вакансии"):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.load_vacancies()

    def load_vacancies(self):
        """Загрузка вакансий из Excel-файла."""
        try:
            df = pd.read_excel(self.file_path, sheet_name=self.sheet_name)
            self.vacancies = df.to_dict(orient="records")
        except FileNotFoundError:
            self.vacancies = []

    def save_vacancies(self):
        """Сохранение вакансий в Excel-файл."""
        df = pd.DataFrame(self.vacancies)
        df.to_excel(self.file_path, sheet_name=self.sheet_name, index=False)

    def add_vacancy(self, vacancy: Dict):
        """Добавить вакансию в Excel-файл."""
        self.vacancies.append(vacancy)
        self.save_vacancies()

    def get_vacancies(self, criteria: Dict = None) -> List[Dict]:
        """Получить вакансии из Excel-файла, используя заданные критерии."""
        if criteria is None:
            return self.vacancies
        filtered_vacancies = []
        for vacancy in self.vacancies:
            match = True
            for key, value in criteria.items():
                if key not in vacancy or vacancy[key] != value:
                    match = False
                    break
            if match:
                filtered_vacancies.append(vacancy)
        return filtered_vacancies

    def delete_vacancy(self, vacancy_id: int):
        """Удалить вакансию из Excel-файла по ID."""
        self.vacancies = [vacancy for vacancy in self.vacancies if vacancy["id"] != vacancy_id]
        self.save_vacancies()

class TextVacancyStorage(VacancyStorage):
    """Класс для работы с TXT-файлом для хранения вакансий."""

    def __init__(self, file_path: str = "vacancies.txt"):
        self.file_path = file_path
        self.load_vacancies()

    def load_vacancies(self):
        """Загрузка вакансий из TXT-файла."""
        try:
            with open(self.file_path, "r") as f:
                self.vacancies = []
                for line in f:
                    vacancy = {}
                    parts = line.strip().split(";")
                    vacancy["id"] = int(parts[0])
                    vacancy["title"] = parts[1]
                    vacancy["link"] = parts[2]
                    vacancy["salary"] = parts[3]
                    vacancy["description"] = parts[4]
                    self.vacancies.append(vacancy)
        except FileNotFoundError:
            self.vacancies = []

    def save_vacancies(self):
        """Сохранение вакансий в TXT-файл."""
        with open(self.file_path, "w") as f:
            for vacancy in self.vacancies:
                f.write(
                    f"{vacancy['id']};{vacancy['title']};{vacancy['link']};{vacancy['salary']};{vacancy['description']}\n"
                )

    def add_vacancy(self, vacancy: Dict):
        """Добавить вакансию в TXT-файл."""
        self.vacancies.append(vacancy)
        self.save_vacancies()

    def get_vacancies(self, criteria: Dict = None) -> List[Dict]:
        """Получить вакансии из TXT-файла, используя заданные критерии."""
        if criteria is None:
            return self.vacancies
        filtered_vacancies = []
        for vacancy in self.vacancies:
            match = True
            for key, value in criteria.items():
                if key not in vacancy or vacancy[key] != value:
                    match = False
                    break
            if match:
                filtered_vacancies.append(vacancy)
        return filtered_vacancies

    def delete_vacancy(self, vacancy_id: int):
        """Удалить вакансию из TXT-файла по ID."""
        self.vacancies = [vacancy for vacancy in self.vacancies if vacancy["id"] != vacancy_id]
        self.save_vacancies()

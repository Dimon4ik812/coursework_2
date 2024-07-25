from abc import ABC, abstractmethod

import requests
from requests import Response


class ApiVacancies(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def get_response(self, *args, **kwargs):
        """Абстрактный метод запроса к api"""
        pass

    @abstractmethod
    def get_vacancies_response(self, *args, **kwargs):
        """Абстрактный метод получения вакансий"""
        pass

    @abstractmethod
    def get_filter_vacancies(self, *args, **kwargs):
        """Абстрактный метод сортировки вакансий"""
        pass


class HeadHunterAPI(ApiVacancies):
    """Класс HeadHunter выполняет запрос к API HH.ru и получает вакансии."""

    def __init__(self):
        """Инициализация класса HeadHunter"""
        self.url = "https://api.hh.ru/vacancies"

    def get_response(self, text: str, per_page: int) -> Response:
        """Запрос на API HH.ru"""
        params = {"text": f"NAME:{text}", "per_page": per_page}
        response = requests.get(self.url, params=params)
        return response

    def get_vacancies_response(self, text: str, per_page: int) -> list:
        """Получение вакансий с HH.ru"""
        vacancies = self.get_response(text, per_page).json()["items"]
        return vacancies

    def get_filter_vacancies(self, text: str, per_page: int = 30) -> list:
        """Фильтрация вакансий"""
        filtered_vacancies = []
        vacancies_filtered = self.get_vacancies_response(text, per_page)
        for vacancy in vacancies_filtered:
            filtered_vacancies.append(
                {
                    "name": vacancy["name"],
                    "salary_from": vacancy["salary"]["from"],
                    "salary_to": vacancy["salary"]["to"],
                    "salary_currency": vacancy["salary"]["currency"],
                    "url": vacancy["alternate_url"],
                    "employer": vacancy["employer"]["name"],
                    "requirement": vacancy["snippet"]["requirement"],
                    "responsibility": vacancy["snippet"]["responsibility"],
                }
            )
            return filtered_vacancies

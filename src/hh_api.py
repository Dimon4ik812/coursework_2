from abc import ABC, abstractmethod
import requests

class VacancyAPI(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями."""

    @abstractmethod
    def get_vacancies(self, keyword):
        """Получение списка вакансий по ключевому слову."""
        pass

class HHVacancyAPI(VacancyAPI):
    """Класс для работы с API HeadHunter."""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 20}

    def get_vacancies(self, keyword):
        """Получение списка вакансий по ключевому слову."""
        self.params['text'] = keyword
        vacancies = []
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies.extend(response.json()['items'])
            self.params['page'] += 1
        return vacancies

class Vacancy:
    """Класс для работы с вакансиями."""

    def __init__(self, title, link, salary, description, id=None):
        self.id = id
        self.title = title
        self.link = link
        self.salary = self._validate_salary(salary)
        self.description = description

    def _validate_salary(self, salary):
        """Валидация зарплаты."""
        if salary:
            return salary
        else:
            return "Зарплата не указана"

    def __lt__(self, other):
        """Сравнение вакансий по зарплате."""
        if self.salary == "Зарплата не указана":
            return False
        elif other.salary == "Зарплата не указана":
            return True
        else:
            return self.salary < other.salary

    def __gt__(self, other):
        """Сравнение вакансий по зарплате."""
        if self.salary == "Зарплата не указана":
            return True
        elif other.salary == "Зарплата не указана":
            return False
        else:
            return self.salary > other.salary

    def __eq__(self, other):
        """Сравнение вакансий по зарплате."""
        if self.salary == "Зарплата не указана":
            return False
        elif other.salary == "Зарплата не указана":
            return False
        else:
            return self.salary == other.salary

# Пример использования
hh_api = HHVacancyAPI()
vacancies = hh_api.get_vacancies('JavaScript Developer')

for vacancy_data in vacancies:
    vacancy = Vacancy(
        title=vacancy_data['name'],
        link=vacancy_data['alternate_url'],
        salary=vacancy_data['salary'],
        description=vacancy_data['snippet']['requirement'],
    )
    print(f"Название вакансии: {vacancy.title}")
    print(f"Ссылка на вакансию: {vacancy.link}")
    print(f"Зарплата: {vacancy.salary}")
    print(f"Описание: {vacancy.description}")
    print("-" * 20)
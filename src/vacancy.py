class Vacancy:
    """Класс для обработки вакансий"""

    def __init__(
        self,
        name: str,
        salary: dict,
        url: str,
        employer: str,
        requirement: str,
        responsibility: str,
    ):
        """Инициализация экземпляра класса"""
        self.name = name
        self.url = url
        self.validate_salary(salary)
        self.employer = employer
        self.requirement = requirement
        self.responsibility = responsibility

    def validate_salary(self, salary):
        """Метод для проверки и корректного вывода зарплаты"""
        if salary is None:
            self.salary_from = 0
            self.salary_to = 0
            self.salary_currency = "валюта не указана"
        else:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0
            self.salary_currency = salary["currency"] if salary["currency"] else "валюта не указана"

    def __str__(self):
        """Вывод данных по вакансии"""
        if self.salary_from == 0:
            self.salary_from = "Нижний предел зарплаты не указан"
        if self.salary_to == 0:
            self.salary_to = "Верхний предел зарплаты не указан"
        return (
            f"Название: {self.name}\n"
            f"Зарплата: от {self.salary_from} до {self.salary_to} {self.salary_currency}\n"
            f"Ссылка: {self.url}\n"
            f"Название компании: {self.employer}\n"
            f"Требования: {self.requirement}\n"
            f"Обязанности: {self.responsibility}\n"
        )

    def __repr__(self):
        """Вывод для разработчика, данных по вакансии"""
        return (
            f"Vacancy({self.name}, {self.salary_from}, {self.salary_to}, {self.url}, {self.employer}, "
            f"{self.requirement}, {self.responsibility})"
        )

    def __gt__(self):
        """Метод для сравнения зарплат"""
        return self.salary_to > self.salary_to

    def __lt__(self, other):
        """сортировка"""
        return (self.salary_from, self.salary_to) <= (
            other.salary_from,
            other.salary_to,
        )

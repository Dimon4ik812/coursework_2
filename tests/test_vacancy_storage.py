import unittest
from src import vacancy_storage
from src.hh_api import HHVacancyAPI

class TestVacancyStorage(unittest.TestCase):

    def test_json_vacancy_storage(self):
        storage = vacancy_storage.JSONVacancyStorage("test_vacancies.json")
        self.assertEqual(storage.get_vacancies(), [])

        vacancy1 = {"id": 1, "title": "Вакансия 1", "link": "link1", "salary": "100000", "description": "Описание 1"}
        vacancy2 = {"id": 2, "title": "Вакансия 2", "link": "link2", "salary": "150000", "description": "Описание 2"}

        storage.add_vacancy(vacancy1)
        storage.add_vacancy(vacancy2)

        self.assertEqual(storage.get_vacancies(), [vacancy1, vacancy2])
        self.assertEqual(storage.get_vacancies(criteria={"id": 1}), [vacancy1])
        self.assertEqual(storage.get_vacancies(criteria={"title": "Вакансия 2"}), [vacancy2])

        storage.delete_vacancy(1)
        self.assertEqual(storage.get_vacancies(), [vacancy2])

    def test_csv_vacancy_storage(self):
        storage = vacancy_storage.CSVVacancyStorage("test_vacancies.csv")
        self.assertEqual(storage.get_vacancies(), [])

        vacancy1 = {"id": 1, "title": "Вакансия 1", "link": "link1", "salary": "100000", "description": "Описание 1"}
        vacancy2 = {"id": 2, "title": "Вакансия 2", "link": "link2", "salary": "150000", "description": "Описание 2"}

        storage.add_vacancy(vacancy1)
        storage.add_vacancy(vacancy2)

        self.assertEqual(storage.get_vacancies(), [vacancy1, vacancy2])
        self.assertEqual(storage.get_vacancies(criteria={"id": 1}), [vacancy1])
        self.assertEqual(storage.get_vacancies(criteria={"title": "Вакансия 2"}), [vacancy2])

        storage.delete_vacancy(1)
        self.assertEqual(storage.get_vacancies(), [vacancy2])

    def test_excel_vacancy_storage(self):
        storage = vacancy_storage.ExcelVacancyStorage("test_vacancies.xlsx")
        self.assertEqual(storage.get_vacancies(), [])

        vacancy1 = {"id": 1, "title": "Вакансия 1", "link": "link1", "salary": "100000", "description": "Описание 1"}
        vacancy2 = {"id": 2, "title": "Вакансия 2", "link": "link2", "salary": "150000", "description": "Описание 2"}

        storage.add_vacancy(vacancy1)
        storage.add_vacancy(vacancy2)

        self.assertEqual(storage.get_vacancies(), [vacancy1, vacancy2])
        self.assertEqual(storage.get_vacancies(criteria={"id": 1}), [vacancy1])
        self.assertEqual(storage.get_vacancies(criteria={"title": "Вакансия 2"}), [vacancy2])

        storage.delete_vacancy(1)
        self.assertEqual(storage.get_vacancies(), [vacancy2])

    def test_text_vacancy_storage(self):
        storage = vacancy_storage.TextVacancyStorage("test_vacancies.txt")
        self.assertEqual(storage.get_vacancies(), [])

        vacancy1 = {"id": 1, "title": "Вакансия 1", "link": "link1", "salary": "100000", "description": "Описание 1"}
        vacancy2 = {"id": 2, "title": "Вакансия 2", "link": "link2", "salary": "150000", "description": "Описание 2"}

        storage.add_vacancy(vacancy1)
        storage.add_vacancy(vacancy2)

        self.assertEqual(storage.get_vacancies(), [vacancy1, vacancy2])
        self.assertEqual(storage.get_vacancies(criteria={"id": 1}), [vacancy1])
        self.assertEqual(storage.get_vacancies(criteria={"title": "Вакансия 2"}), [vacancy2])

        storage.delete_vacancy(1)
        self.assertEqual(storage.get_vacancies(), [vacancy2])

if __name__ == '__main__':
    unittest.main()
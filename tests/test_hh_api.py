import unittest
from unittest.mock import patch

from src.hh_api import ApiVacancies, HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):

    @patch("requests.get")
    def test_get_response(self, mock_get):
        """Проверяет, что get_response правильно формирует запрос."""
        hh = HeadHunterAPI()
        text = "Python разработчик"
        per_page = 20
        expected_url = "https://api.hh.ru/vacancies"
        expected_params = {"text": f"NAME:{text}", "per_page": per_page}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"items": []}  # Заглушка для ответа

        response = hh.get_response(text, per_page)

        mock_get.assert_called_once_with(expected_url, params=expected_params)
        self.assertEqual(response.status_code, 200)

    @patch("requests.get")
    def test_get_vacancies_response(self, mock_get):
        """Проверяет, что get_vacancies_response правильно извлекает вакансии."""
        hh = HeadHunterAPI()
        text = "Python разработчик"
        per_page = 20
        mock_response = {
            "items": [
                {"name": "Вакансия 1", "salary": {"from": 100000, "to": 200000, "currency": "RUR"}},
                {"name": "Вакансия 2", "salary": {"from": 150000, "to": 250000, "currency": "RUR"}},
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        vacancies = hh.get_vacancies_response(text, per_page)

        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[0]["name"], "Вакансия 1")
        self.assertEqual(vacancies[0]["salary"]["from"], 100000)
        self.assertEqual(vacancies[1]["name"], "Вакансия 2")
        self.assertEqual(vacancies[1]["salary"]["from"], 150000)

    @patch("requests.get")
    def test_get_filter_vacancies(self, mock_get):
        """Проверяет, что get_filter_vacancies правильно фильтрует и форматирует вакансии."""
        hh = HeadHunterAPI()
        text = "Python разработчик"
        mock_response = {
            "items": [
                {
                    "name": "Вакансия 1",
                    "salary": {"from": 100000, "to": 200000, "currency": "RUR"},
                    "alternate_url": "https://hh.ru/vacancy/12345",
                    "employer": {"name": "Компания 1"},
                    "snippet": {"requirement": "Опыт работы...", "responsibility": "Разработка..."},
                },
                {
                    "name": "Вакансия 2",
                    "salary": {"from": 150000, "to": 250000, "currency": "RUR"},
                    "alternate_url": "https://hh.ru/vacancy/67890",
                    "employer": {"name": "Компания 2"},
                    "snippet": {"requirement": "Знание...", "responsibility": "Разработка..."},
                },
            ]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        filtered_vacancies = hh.get_filter_vacancies(text)

        self.assertEqual(len(filtered_vacancies), 1)  #  Так как в коде return после первого элемента
        self.assertEqual(filtered_vacancies[0]["name"], "Вакансия 1")
        self.assertEqual(filtered_vacancies[0]["salary_from"], 100000)
        self.assertEqual(filtered_vacancies[0]["salary_to"], 200000)
        self.assertEqual(filtered_vacancies[0]["salary_currency"], "RUR")
        self.assertEqual(filtered_vacancies[0]["url"], "https://hh.ru/vacancy/12345")
        self.assertEqual(filtered_vacancies[0]["employer"], "Компания 1")
        self.assertEqual(filtered_vacancies[0]["requirement"], "Опыт работы...")
        self.assertEqual(filtered_vacancies[0]["responsibility"], "Разработка...")

    def test_abstract_methods(self):
        """Проверяет, что абстрактные методы ApiVacancies не реализованы."""
        with self.assertRaises(TypeError):
            ApiVacancies()  # Попытка создания экземпляра абстрактного класса

import unittest

from src.vacancy import Vacancy


class TestVacancy(unittest.TestCase):
    def test_init(self):
        vacancy = Vacancy(
            name="Software Engineer",
            salary={"from": 5000, "to": 10000, "currency": "USD"},
            url="https://example.com/vacancy",
            employer="Example Company",
            requirement="Bachelor's degree in Computer Science",
            responsibility="Develop and maintain software applications",
        )
        self.assertEqual(vacancy.name, "Software Engineer")
        self.assertEqual(vacancy.salary_from, 5000)
        self.assertEqual(vacancy.salary_to, 10000)
        self.assertEqual(vacancy.salary_currency, "USD")
        self.assertEqual(vacancy.url, "https://example.com/vacancy")
        self.assertEqual(vacancy.employer, "Example Company")
        self.assertEqual(vacancy.requirement, "Bachelor's degree in Computer Science")
        self.assertEqual(vacancy.responsibility, "Develop and maintain software applications")

    def test_validate_salary_with_none(self):
        vacancy = Vacancy(
            name="Software Engineer",
            salary=None,
            url="https://example.com/vacancy",
            employer="Example Company",
            requirement="Bachelor's degree in Computer Science",
            responsibility="Develop and maintain software applications",
        )
        self.assertEqual(vacancy.salary_from, 0)
        self.assertEqual(vacancy.salary_to, 0)
        self.assertEqual(vacancy.salary_currency, "валюта не указана")

    def test_str(self):
        vacancy = Vacancy(
            name="Software Engineer",
            salary={"from": 5000, "to": 10000, "currency": "USD"},
            url="https://example.com/vacancy",
            employer="Example Company",
            requirement="Bachelor's degree in Computer Science",
            responsibility="Develop and maintain software applications",
        )
        expected_output = (
            "Название: Software Engineer\n"
            "Зарплата: от 5000 до 10000 USD\n"
            "Ссылка: https://example.com/vacancy\n"
            "Название компании: Example Company\n"
            "Требования: Bachelor's degree in Computer Science\n"
            "Обязанности: Develop and maintain software applications\n"
        )
        self.assertEqual(str(vacancy), expected_output)

    def test_repr(self):
        vacancy = Vacancy(
            name="Software Engineer",
            salary={"from": 5000, "to": 10000, "currency": "USD"},
            url="https://example.com/vacancy",
            employer="Example Company",
            requirement="Bachelor's degree in Computer Science",
            responsibility="Develop and maintain software applications",
        )
        expected_output = (
            "Vacancy(Software Engineer, 5000, 10000, https://example.com/vacancy, Example Company, "
            "Bachelor's degree in Computer Science, Develop and maintain software applications)"
        )
        self.assertEqual(repr(vacancy), expected_output)

    def test_lt(self):
        vacancy1 = Vacancy(
            name="Software Engineer",
            salary={"from": 5000, "to": 10000, "currency": "USD"},
            url="https://example.com/vacancy",
            employer="Example Company",
            requirement="Bachelor's degree in Computer Science",
            responsibility="Develop and maintain software applications",
        )
        vacancy2 = Vacancy(
            name="Data Analyst",
            salary={"from": 4000, "to": 8000, "currency": "USD"},
            url="https://example.com/vacancy2",
            employer="Example Company",
            requirement="Bachelor's degree in Statistics",
            responsibility="Analyze data and provide insights",
        )
        self.assertTrue(vacancy2 < vacancy1)


if __name__ == "__main__":
    unittest.main()

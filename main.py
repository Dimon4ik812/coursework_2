from src.hh_api import HeadHunterAPI
from src.utils import get_salary, get_vacancies_by_salary
from src.vacancy_storage import JSONSaver


def main() -> None:
    """Главная функция работы с пользователем"""
    print("Добро пожаловать в приложения для поиска вакансий на hh.ru")
    hh = HeadHunterAPI()
    print("Получаем вакансии с сайта")
    text = input("Введите слова для поиска вакансий: ")
    per_page = input("Введите количество вакансий которое хотите вывести на экран: ")
    vacancies = hh.get_vacancies_response(text, per_page)

    print("Сохраняем вакансии в файл")
    saver = JSONSaver()
    saver.write_data(vacancies)

    min_salary, max_salary = get_salary()
    vacancies = get_vacancies_by_salary(min_salary, max_salary)
    counter_vacancy = 0
    for vacancy in vacancies:
        counter_vacancy += 1
        print(f"№ вакансии: {counter_vacancy}")
        print(vacancy)


main()

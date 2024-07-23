from src.vacancy_storage import JSONSaver


def get_salary():
    """Функция ввода зарплаты для поиска по вакансиям"""
    while True:
        salary = input(
            'Введите диапазон зарплат в формате "минимальная зарплата - максимальная зарплата", '
            "если хотите вывести вакансии где зарплата не указана укажите минимальную зарплату равную 0: "
        )
        try:
            min_salary_str, max_salary_str = salary.split(" - ")
            min_salary = int(min_salary_str)
            max_salary = int(max_salary_str)
            if min_salary > max_salary:
                raise ValueError
            return min_salary, max_salary
        except ValueError:
            print(
                "Неправильно введен диапазон. Пожалуйста, введите зарплаты в формате "
                '"минимальная зарплата - максимальная зарплата"'
            )


def get_vacancies_by_salary(min_salary, max_salary):
    """Функция получения вакансий по зарплате"""
    result = []
    saver = JSONSaver()
    all_vacancies = saver.get_vacancies()
    for vac in all_vacancies:
        salary_from = vac.salary_from
        salary_to = vac.salary_to

        if salary_from >= min_salary and salary_to <= max_salary:
            result.append(vac)
    result.sort(key=lambda x: (x.salary_from, x.salary_to))
    return result

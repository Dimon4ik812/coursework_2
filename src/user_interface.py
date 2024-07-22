from src import vacancy_storage
from src.hh_api import HHVacancyAPI

def main():
    """Взаимодействие с пользователем через консоль."""

    storage_type = input(
        "Выберите тип хранилища (JSON/CSV/Excel/TXT): "
    ).strip().upper()

    if storage_type == "JSON":
        storage = vacancy_storage.JSONVacancyStorage()
    elif storage_type == "CSV":
        storage = vacancy_storage.CSVVacancyStorage()
    elif storage_type == "EXCEL":
        storage = vacancy_storage.ExcelVacancyStorage()
    elif storage_type == "TXT":
        storage = vacancy_storage.TextVacancyStorage()
    else:
        print("Неверный тип хранилища.")
        return

    hh_api = HHVacancyAPI()

    while True:
        print("\nМеню:")
        print("1. Поиск вакансий на hh.ru")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии с ключевым словом в описании")
        print("4. Вывести все вакансии из хранилища")
        print("5. Удалить вакансию по ID")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            keyword = input("Введите поисковый запрос: ")
            vacancies = hh_api.get_vacancies(keyword)
            for vacancy_data in vacancies:
                vacancy = {
                    "id": vacancy_data.get("id"),
                    "title": vacancy_data["name"],
                    "link": vacancy_data["alternate_url"],
                    "salary": vacancy_data["salary"],
                    "description": vacancy_data["snippet"]["requirement"],
                }
                storage.add_vacancy(vacancy)
            print(f"Найдено {len(vacancies)} вакансий. Они добавлены в хранилище.")

        elif choice == "2":
            try:
                n = int(input("Введите число вакансий (N): "))
                vacancies = storage.get_vacancies()
                sorted_vacancies = sorted(vacancies, key=lambda x: x["salary"], reverse=True)
                top_vacancies = sorted_vacancies[:n]
                for vacancy in top_vacancies:
                    print(
                        f"Название: {vacancy['title']}, Зарплата: {vacancy['salary']}"
                    )
            except ValueError:
                print("Неверный формат ввода.")

        elif choice == "3":
            keyword = input("Введите ключевое слово: ")
            criteria = {"description": keyword}
            vacancies = storage.get_vacancies(criteria)
            if vacancies:
                for vacancy in vacancies:
                    print(
                        f"Название: {vacancy['title']}, Описание: {vacancy['description']}"
                    )
            else:
                print("Вакансий с этим ключевым словом не найдено.")

        elif choice == "4":
            vacancies = storage.get_vacancies()
            if vacancies:
                for vacancy in vacancies:
                    print(
                        f"ID: {vacancy['id']}, Название: {vacancy['title']}, Зарплата: {vacancy['salary']}"
                    )
            else:
                print("Хранилище вакансий пусто.")

        elif choice == "5":
            try:
                vacancy_id = int(input("Введите ID вакансии для удаления: "))
                storage.delete_vacancy(vacancy_id)
                print(f"Вакансия с ID {vacancy_id} удалена из хранилища.")
            except ValueError:
                print("Неверный формат ввода.")

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Неверный выбор.")

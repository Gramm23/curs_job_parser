import sys
from utils import save_vacancies_to_file, display_vacancy_options

if __name__ == "__main__":
    while True:
        print("Добро пожаловать в программу по поиску вакансий")
        print()
        print("""Выберете платформу для поиска вакансии:
        1. HeadHunter            - 1
        2. SuperJob              - 2
        3. HeadHunter и SuperJob - 3
        """)

        answer_platform = int(input("Введите номер платформы для поиска вакансии: "))

        if answer_platform not in (1, 2, 3):
            print()
            print("Под таким номером поисковая платформа отсутствует")
            print()
            user_answer = input('Введите другой номер или введите "0" для выхода: ')
            if user_answer == '0':
                print()
                print("Нам жаль, что Вы ничего для себя не нашли, ждем Вас снова")
                sys.exit()

        save_vacancies_to_file(answer_platform)

        print()
        print("Выберете значение по которому сделать выборку")
        print()
        print("""
        1. Показать все вакансии                          - 1
        2. Показать вакансии по городу                    - 2
        3. Показать вакансии по зарплате (по убыванию)    - 3
        4. Показать топ N вакансий                        - 4
        """)

        user_answer = int(input("Введите номер значения: "))
        display_vacancy_options(user_answer)

        restart = input("Хотите продолжить поиск? (Да/Нет): ")
        if restart.lower() != 'да':
            print("Спасибо за использование программы. До свидания!")
            break

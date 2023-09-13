class Vacancy:

    def __init__(self, title, salary_from, salary_to, experience, city, url):
        self.title = title
        self._salary_from = salary_from
        self._salary_to = salary_to
        self.experience = experience
        self.city = city
        self.url = url

    def __str__(self):
        return f"""Вакансия: {self.title}
Зарплата: {self._salary_from} до {self._salary_to} руб.
Опыт: {self.experience}
Город: {self.city}
Ссылка на вакансию: {self.url}"""

    def __ge__(self, other):
        self_salary = self._salary_from if self.salary_from is not None else 0
        return self_salary >= other

    @property
    def salary_from(self):
        return self._salary_from

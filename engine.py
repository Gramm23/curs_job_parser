from abc import ABC, abstractmethod
from class_error import ParsingError
import requests

secret_key_sj = 'v3.r.137787279.119015fa0f76cb13db4a4c08899279b5de21641a.7437ad55167a84b2c7ecc31b34bfed415c19a7a6'


class VacancyAPI(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def get_formatted_vacancies(self):
        pass


class HeadHunterAPI(VacancyAPI):

    def __init__(self, text):
        self.text = text
        self.vacancies = []

    def get_vacancies(self):
        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': self.text,
            'per_page': 50
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансий! Статус: {response.status_code}")
        self.vacancies.append(response.json()['items'])
        return self.vacancies

    def get_formatted_vacancies(self):
        formatted_vacancies = []
        for vacancy in self.vacancies[0]:
            formatted_vacancy = {
                "title": vacancy["name"],
                "salary_from": vacancy["salary"]["from"] if vacancy["salary"] else None,
                "salary_to": vacancy["salary"]["to"] if vacancy["salary"] else None,
                "experience": vacancy["experience"]["name"],
                "city": vacancy["area"]["name"],
                "url": vacancy["url"]
            }
            formatted_vacancies.append(formatted_vacancy)
        return formatted_vacancies


class SuperJobAPI(VacancyAPI):

    def __init__(self, text):
        self.text = text
        self.vacancies = []

    def get_vacancies(self):
        url = 'https://api.superjob.ru/2.0/vacancies'

        headers = {
            "X-Api-App-Id": secret_key_sj
        }
        params = {
            'keyword': self.text,
            'count': 50
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансий! Статус: {response.status_code}")
        self.vacancies.append(response.json()['objects'])
        return self.vacancies

    def get_formatted_vacancies(self):
        formatted_vacancies = []
        for vacancy in self.vacancies[0]:
            formatted_vacancy = {
                "title": vacancy["profession"],
                "salary_from": vacancy["payment_from"] if vacancy["payment_from"] else None,
                "salary_to": vacancy["payment_to"] if vacancy["payment_to"] else None,
                "experience": vacancy["experience"]["title"],
                "city": vacancy["town"]["title"],
                "url": vacancy["link"]
            }
            formatted_vacancies.append(formatted_vacancy)
        return formatted_vacancies




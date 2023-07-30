from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import base64

# Для начала определим настройки запуска
hostName = "localhost" # Адрес для доступа по сети
serverPort = 8080 # Порт для доступа по сети

class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def __get_html_from_git(self):
        '''
        Получает данные HTML-файла с удаленого репозитория
        :return: html-код
        '''

        url = 'https://raw.githubusercontent.com/KirillSimf2023/Django_HW_19_1/master/index.html'
        req = requests.get(url)
        if req.status_code == requests.codes.ok:
            ansver = req.text
        else:
            print('Content was not found.')
        return ansver

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        content = self.__get_html_from_git()
        self.send_response(200) # Отправка кода ответа
        self.send_header("Content-type", "text/html") # Отправка типа данных, который будет передаваться
        self.end_headers() # Завершение формирования заголовков ответа
        self.wfile.write(bytes(content, "utf-8")) # Тело ответа

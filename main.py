from http.server import HTTPServer
from server import hostName, serverPort, MyServer


def main():
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    server = HTTPServer((hostName, serverPort), MyServer)
    print(f'Сервер запущен на http://{hostName}:{serverPort}')

    try:
        # Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов
        server.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    server.server_close()
    print('Сервер остановлен')


if __name__ == "__main__":
    main()
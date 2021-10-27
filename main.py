import sys
import getpass
from Values import user_name, password
from mysql.connector import connect, Error

#Основной класс
class Mysqlproject():

    #Инициализация класса
    def __init__(self, *args):
        print("#" * 20)
        self.mainfunc()

    #Основная функция
    def mainfunc(self):
        choice = input("1.Создать нового пользователя\n2.Войти в профиль\n3.Выйти из программы\n"+"#"*20+"\n \nВведите цифру выбранной команды: ")
        list_choice = {
            "1": self.input_value,
            "2": self.user_enter,
            "3": self.user_quit,
        }
        try:
            return list_choice[choice]()
        except KeyError:
            print("Выбрана неправильная команда")
            return self.mainfunc()

    #Функция создания нового пользователя
    def input_value(self):
        new_username = input("Введите имя пользователя: ")
        new_passwd = getpass.getpass(prompt="Введите пароль: ")
        current_passwd = getpass.getpass(prompt="Подтвердите пароль: ")
        if new_passwd == current_passwd:
            try:
                with connect(host="127.0.0.1",
                             user=user_name,
                             password=password) as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(f"CREATE USER'{new_username}'@'127.0.0.1' IDENTIFIED BY '{new_passwd}';")
                        print(f"Пользователь {new_username} успешно создан!")
                return self.mainfunc()
            except Error as e:
                print(e)
                return self.mainfunc()
        else:
            print("Пароли не совпадают")
            return self.mainfunc()

    #Функция входа в профиль
    def user_enter(self):
        print("\n" + "#" * 20 + "\n")
        try:
            enter_username = input("Введите имя пользователя: ")
            enter_password = getpass.getpass(prompt="Введите пароль: ")
            with connect(host="127.0.0.1",
                         user=enter_username,
                         password=enter_password,
                         ) as connection:
                print("\n" + "#"*20+f"\nДобро пожаловать {enter_username}!\n")
                user_choice = input("Выберите номер команды:\n1.Просмотр таблицы в базе данных\n2.Редактирование базы данных\n3.Дополнительные функции")
                list_user_choice = {
                    #TO DO user_functions
                }


        except Error as e:
            print("\n",e)
            return self.mainfunc()

    #Функция выхода из приложения
    def user_quit(self):
        print("Выходим...")
        sys.exit()

if __name__ == "__main__":
    Mysqlproject()

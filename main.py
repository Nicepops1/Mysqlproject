import sys
import getpass
from Values import user_name, password
from mysql.connector import connect, Error


class Mysqlproject():

    def __init__(self, *args):
        print("#" * 20)
        self.mainfunc()

    def mainfunc(self):
        choice = input("1.Создать нового пользователя\n2.Войти\n3.Выйти\nВведите цифру выбранной команды: ")
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

    def user_enter(self):
        print("\n" + "#" * 20 + "\n")
        try:
            enter_username = input("Введите имя пользователя: ")
            enter_password = getpass.getpass(prompt="Введите пароль: ")
            with connect(host="127.0.0.1",
                         user=enter_username,
                         password=enter_password,
                         ) as connection:
                print("\n" + "#"*20+f"\nДобро пожаловать {enter_username}!")
                print("")


        except Error as e:
            print("\n",e)
            return self.mainfunc()

    def user_quit(self):
        print("Выходим...")
        sys.exit()

if __name__ == "__main__":
    Mysqlproject()

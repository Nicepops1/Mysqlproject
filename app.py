import pymysql, time
import admin_panel

class Main():
    def __init__(self):
        user_selection = str(input('Для входа в систему введите команду `войти`, для выхода - `выйти` -> '))
        if user_selection == 'войти':
            self.join_to_database()
        elif user_selection == 'выйти':
            print('Выходим...')
        else:
            print('Введена неверная команда')
            Main()

    def join_to_database(self):
        user_login = str(input('Введите имя пользователя: '))
        user_password = str(input('Введите пароль: '))

        if self.is_registered(user_login, user_password):
            connection = pymysql.connect(
                host='localhost',
                port=3306,
                user=user_login,
                password=user_password,
            )
            print('Производится вход в систему, пожалуйста подождите...')
            time.sleep(1)
            print('Вы успешно вошли в систему!')


        else:
            print('Вы не зарегистрированы в системе')
            should_create_new_user = str(input('Хотите ли вы создать нового пользователя? (Y/N) -> '))
            if should_create_new_user == 'Y':
                admin_panel.create_new_user(user_login, user_password)
            else:
                print('Перенаправляем вас на главную "страницу"...')
                time.sleep(.5)
                Main()

    def is_registered(self, user_login, user_password):
        try:
            connection = pymysql.connect(
                host='localhost',
                port=3306,
                user=user_login,
                password=user_password,
            )
            connection.close()
            return True
        except Exception as ex:
            return False

if __name__ == "__main__":
    Main()



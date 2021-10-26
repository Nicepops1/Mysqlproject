import pymysql, time
import config

def create_new_user(user_login, user_password):
    try:
        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user=config.user,
            password=config.password,
            database=config.db_name,
        )
        with connection.cursor() as cursor:
            create_new_user_query = f""" CREATE USER '{user_login}'@'localhost' IDENTIFIED BY '{user_password}'; """
            print(f'Создание пользователя {user_login}...')
            time.sleep(1)
            print('Создание прошло успешно!')
            cursor.execute(create_new_user_query)
            connection.commit()
    except Exception as ex:
        print('Произошла ошибка... (admin_panel)')
        print(ex)

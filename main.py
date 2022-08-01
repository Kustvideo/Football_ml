# Заккоментировать ctrl k ctrl c Раскомментировать ctrl k ctrl u

import psycopg2
from config import host, user, password, db_name


try:
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    
    )

    connection.autocommit = True
    # Запрос на соединение и проверку версии

    with connection.cursor() as cursor:
        cursor.execute(
            "select version();"
        )
        print(f"Server version: {cursor.fetchone()}")
    
    # Запрос на создание таблицы
    
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #             id serial PRIMARY KEY,
    #             first_name varchar(50) NOT NULL,
    #             nick_name varchar(50) NOT NULL)"""
    #     )
    #     print("Table created")
    

    # Запрос на добавление

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """INSERT INTO users(              
    #             first_name,
    #             nick_name)
    #             VALUES ('Sasha', 'Boss')"""
    #     )
    #     print("[info] Table inserted")

    # Запрос на select 

    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT id, nick_name FROM users              
                WHERE first_name = 'Sasha';
                """
        )
        print(cursor.fetchone())


except Exception as _ex:
    print('Err', _ex)
finally:
    if connection:
        connection.close()
        print('[INFO] cool')

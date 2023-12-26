import pymysql.cursors
import random

conn = pymysql.connect(
    host="db",
    user="root",
    password="password",
    db="dev",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)


def get_users():
    with conn.cursor() as cursor:
        sql = "SELECT * FROM `Users`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def get_user_first_data():
    with conn.cursor() as cursor:
        sql = "SELECT * FROM `Users` ORDER BY `id` ASC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        logger("FIRST DATA")
        print(result)

def get_user_by_id():
    with conn.cursor() as cursor:
        sql = "SELECT * FROM `Users` ORDER BY `id` DESC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        logger("LAST DATA")
        print(result)

def get_user_count():
    with conn.cursor() as cursor:
        sql = "SELECT COUNT(*) FROM `Users`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)

def get_all_user_ids():
    with conn.cursor() as cursor:
        sql = "SELECT `id` FROM `Users`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)

def get_first_user_id():
    with conn.cursor() as cursor:
        sql = "SELECT `id` FROM `Users` ORDER BY `id` ASC LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)

def insert_user():
    with conn.cursor() as cursor:
        sql = "INSERT INTO `Users` (`Name`, `Age`, `Male`) VALUES ('Python-Tester', 999, True)"
        cursor.execute(sql)
        conn.commit()
        logger("INSERT")
        get_users()


def update_user():
    with conn.cursor() as cursor:
        rand = random.randint(0, 99)
        sql = f"UPDATE `Users` SET `Name`='大車輪', `Age`={rand}, `Male`=False ORDER BY `id` ASC LIMIT 1"
        cursor.execute(sql)
        conn.commit()
        logger("UPDATE")
        get_users()


def delete_user():
    with conn.cursor() as cursor:
        sql = "DELETE FROM `Users` ORDER BY `id` ASC LIMIT 1"
        cursor.execute(sql)
        conn.commit()
        logger("DELETE")
        get_users()


def logger(message: str):
    print(message)


get_users()
get_user_first_data()
get_user_by_id()

get_user_count()
get_all_user_ids()
get_first_user_id()

insert_user()
update_user()
delete_user()


conn.close()
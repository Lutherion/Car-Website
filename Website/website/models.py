# write all your SQL queries in this file.
from datetime import datetime
from psycopg2 import sql
import psycopg2
#from website import conn

db = "dbname='website' user='website' host='127.0.0.1' password = '1235'"
conn = psycopg2.connect(db)

def select_Cars():
    cur = conn.cursor()
    sql = """
    SELECT * FROM Cars
    """
    cur.execute(sql)
    cars = [row for row in cur.fetchall()]
    cur.close()
    return cars

def select_user_id(username, password):
    cur = conn.cursor()
    sql = """
    SELECT c_id FROM Users WHERE c_name = %s AND c_password = %s
    """
    cur.execute(sql, (username, password))
    cars = [row for row in cur.fetchall()]
    cur.close()
    return cars

def select_favourites(user_id):
    print(user_id)
    cur = conn.cursor()
    sql = f"""
    SELECT C.* FROM Cars C, favbrand F where F.c_id = {user_id} and C.cars_id = F.cars_id
    """
    cur.execute(sql)
    cars = [row for row in cur.fetchall()]
    cur.close()
    return cars
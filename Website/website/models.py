from datetime import datetime
import psycopg2

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

def add_car(cars, model, german, netherlands, unitedKingdom, battery, acceleration, topSpeed, range, efficiency, fastCharge, towing, seats):
    l = len(cars)
    cur = conn.cursor()
    sql = f"""
    INSERT INTO cars(cars_id, name, available_since, german_price, netherlands_price, unitedkingdom_price, battery, acceleration, top_speed, range, efficiency, fast_charge, towing, seats)
    VALUES ({l}, '{model}', '{datetime.now().date()}', {german}, {netherlands}, {unitedKingdom}, {battery}, {acceleration}, {topSpeed}, {range}, {efficiency}, {fastCharge}, {towing}, {seats}); 
    """
    print(sql)
    cur.execute(sql)
    conn.commit()
    cur.close()

    return(1)
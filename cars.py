from datetime import datetime

from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from dbconn import DbConn


from dbconn import DbConn
from auth_schemas import UserSignUpSchema, UserLoginSchema
from security import hash_password, verify_password
from cars_schemas import CarsCreateSchema
# from buy_courses_schemas import BuyCoursesSchemas

cars_router = APIRouter(tags=['Cars Create'])


# @_CREATE:

@cars_router.post("/cars")
def add_cars(data: CarsCreateSchema):
    dbconn = DbConn()

    dbconn.cursor.execute("""INSERT INTO cars (name, duration, price) VALUES (%s, %s, %s)""",
                          (data.name, data.duration, data.price))

    dbconn.conn.commit()

    return "OK"


# @_GET:
cars_router1 = APIRouter(tags=['Cars Get'])

@cars_router1.get("/{cars_id}")
def get_curs_by_id(cars_id, user_id):
    dbconn = DbConn()
    # TODO:
    dbconn.cursor.execute("""SELECT * FROM bayed_courses""")
    all_buyed_courses = dbconn.cursor.fetchall()

    for c in all_buyed_courses:
        print(c)

    return

    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE id=%s""",
                          (id,))

    cars = dbconn.cursor.fetchone()

    return cars


@cars_router1.get("/cars_name")
def get_cars_by_name(name):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE name=%s""",
                          (name,))

    cars = dbconn.cursor.fetchall()

    return cars


@cars_router1.get("/cars_duration")
def get_cars_by_duration(duration):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE duration=%s""",
                          (duration,))

    cars = dbconn.cursor.fetchall()

    return cars


@cars_router1.get("/cars_price")
def get_cars_by_price(price):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE price=%s""",
                          (price,))

    cars = dbconn.cursor.fetchall()

    return cars


# @_UPDATE:
cars_router2 = APIRouter(tags=['Cars Update'])

@cars_router2.put("/cars_id")
def update_cars_by_id(data: CarsCreateSchema, id: int):
    dbconn = DbConn()

    dbconn.cursor.execute("""UPDATE cars SET name=%s, duration=%s, price=%s WHERE id=%s""",
                          (data.name, data.duration, data.price, id))

    dbconn.conn.commit()

    return "OK"


# DELETE:
cars_router3 = APIRouter(tags=['Cars Delete'])

@cars_router3.delete("/cars_id")
def delite_cars_by_id(id):
    dbconn = DbConn()

    dbconn.cursor.execute("""DELETE FROM cars WHERE id=%s""",
                          (id,))

    dbconn.conn.commit()

    return "OK"

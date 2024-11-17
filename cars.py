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

    dbconn.cursor.execute("""INSERT INTO cars (tipe, brand, model, year, mileage, color, price,
            engine, engine_capacity, gearbox, drive, steering_wheel, region, description)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                          (data.tipe, data.model, data.year, data.mileage, data.color, data.price,
                           data. engine, data.engine_capacity, data.gearbox, data.drive,
                           data.steering_wheel, data.region, data.duration))

    dbconn.conn.commit()

    return "OK"


# @_GET:
cars_router1 = APIRouter(tags=['Cars Get'])

@cars_router1.get("/{id}")
def get_cars_by_id(id):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE id=%s""",
                          (id,))

    cars = dbconn.cursor.fetchone()

    return cars


@cars_router1.get("/{tipe}")
def get_cars_by_tipe(tipe):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE tipe=%s""",
                          (tipe,))

    cars = dbconn.cursor.fetchall()

    return cars


@cars_router1.get("/{brand}")
def get_cars_by_brand(brand):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE brand=%s""",
                          (brand,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/{year}")
def get_cars_by_year(year):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE year=%s""",
                          (year,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/{mileage}")
def get_cars_by_mileage(mileage):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE mileage=%s""",
                          (mileage,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/{color}")
def get_cars_by_color(color):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE color=%s""",
                          (color,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/{price}")
def get_cars_by_price(price):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE price=%s""",
                          (price,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/{engine}")
def get_cars_by_engine(engine):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE engine=%s""",
                          (engine,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/{engine_capacity}")
def get_cars_by_engine_capacity(engine_capacity):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE engine_capacity=%s""",
                          (engine_capacity,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/{gearbox}")
def get_cars_by_gearbox(gearbox):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE gearbox=%s""",
                          (gearbox,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/{drive}")
def get_cars_by_drive(drive):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE drive=%s""",
                          (drive,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/{steering_wheel}")
def get_cars_by_steering_wheel(steering_wheel):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE steering_wheel=%s""",
                          (steering_wheel,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/{region}")
def get_cars_by_region(region):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE region=%s""",
                          (region,))

    cars = dbconn.cursor.fetchall()

    return cars

@cars_router1.get("/{description}")
def get_cars_by_description(description):
    dbconn = DbConn()

    dbconn.cursor.execute("""SELECT * FROM cars WHERE description=%s""",
                          (description,))

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
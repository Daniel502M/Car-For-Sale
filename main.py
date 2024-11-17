from fastapi import FastAPI
import uvicorn
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app = FastAPI()


@app.get('/')
def main():
    return "Ok"




if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
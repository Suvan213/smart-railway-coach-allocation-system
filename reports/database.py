import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="suvan213",
        database="railway_coach_db"
    )
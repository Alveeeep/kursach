import psycopg2

conn = psycopg2.connect(
    dbname="kursovaya",
    user="alvir",
    password="MiNeR4321",
    host="localhost"
)
cur = conn.cursor()

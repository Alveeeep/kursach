import psycopg2

conn = psycopg2.connect(
    dbname="kursovaya",
    user="alvir",
    password="MiNeR4321",
    host="127.0.0.1",
    port="5445"
)
cur = conn.cursor()

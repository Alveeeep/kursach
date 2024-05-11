import psycopg2
from db import cur, conn
from datetime import date


def get_client_info(client_id: int):
    cur.execute("SELECT * FROM Clients WHERE id_client=%s", (client_id,))
    data = cur.fetchone()
    return data


def create_purchase(client_id: int, product_id: int, store_id: int, count: int):
    cur.execute("INSERT INTO Purchases (id_client, id_store, purchase_date) VALUES (%s, %s, %s)",
                (client_id, store_id, date.today().isoformat()))
    conn.commit()
    cur.execute("SELECT id_purchase FROM Purchases ORDER BY id_purchase DESC LIMIT 1")
    p_id = cur.fetchone()["id_purchase"]
    cur.execute("INSERT INTO Purchases_payments ()")

import psycopg2
from db import cur, conn
from datetime import date


def get_client_info(client_id: int):
    cur.execute(f"SELECT * FROM clients WHERE id_client={client_id}")
    data = cur.fetchone()
    return data


def edit_client_info(client_id: int, email, phone, firstname, lastname):
    cur.execute(
        f"UPDATE Clients SET email={email},phone={phone},firstname={firstname},lastname={lastname} WHERE id_client={client_id}")
    conn.commit()
    conn.close()


def get_product_info(product_id: int):
    cur.execute(f"SELECT * FROM Products WHERE id_product={product_id}")
    data = cur.fetchone()
    return data


def edit_product_info(product_id: int, name, id_manufacture, id_category, price):
    cur.execute(
        f"UPDATE Products SET name={name},id_manufacture={id_manufacture},id_category={id_category},price={price} WHERE id_product={product_id}")
    conn.commit()
    conn.close()


def create_purchase(client_id: int, product_id: int, store_id: int, count: int):
    cur.execute(
        f"INSERT INTO Purchases (id_client, id_store, purchase_date) VALUES ({client_id}, {store_id}, {date.today().isoformat()})")
    conn.commit()
    cur.execute("SELECT id_purchase FROM Purchases ORDER BY id_purchase DESC LIMIT 1")
    p_id = cur.fetchone()[0]
    price = get_product_info(product_id)[4]
    cur.execute(
        f"INSERT INTO Purchases_payments (id_purchase, id_product, count, price) VALUES ({p_id}, {product_id}, {count}, {price})",
        (p_id, product_id, count, price))
    conn.commit()
    conn.close()


def get_deliveries_by_product(product_id: int):
    cur.execute(f"SELECT * FROM Deliveries WHERE id_product={product_id}")
    data = cur.fetchall()
    return data


def get_product_count_in_store(product_id: int, store_id: int):
    cur.execute(f"SELECT SUM(count) FROM Deliveries WHERE id_product={product_id} and id_store={store_id}")
    count_deliveries = cur.fetchone()[0]
    req1 = f"SELECT id_purchase FROM Purchase WHERE id_store={store_id}"
    cur.execute(f"SELECT SUM(count) FROM Purchases_payments WHERE id_purchase IN ({req1}) and id_product={product_id}")
    count_purchases = cur.fetchone()[0]
    if count_deliveries - count_purchases > 0:
        return count_deliveries - count_purchases
    return 0


def get_products_in_store(store_id: int):
    cur.execute(
        f"SELECT id_product, SUM(count) as total_count FROM Deliveries WHERE id_store={store_id} GROUP BY id_product")
    data = cur.fetchall()
    return data


def add_product(name: str, id_manufacture: int, id_category: int, price: int):
    cur.execute(
        f"INSERT INTO Products (name, id_manufacture, id_category, price) VALUES ({name}, {id_manufacture}, {id_category}, {price})")
    conn.commit()
    conn.close()


def delete_product(product_id: int):
    cur.execute(f"DELETE FROM Products WHERE id_product={product_id}")
    conn.commit()
    conn.close()


def add_delivery(product_id: int, store_id: int, count: int):
    cur.execute(
        f"INSERT INTO Deliveries (id_product, id_store, delivery_date, count) VALUES ({product_id},{store_id},{date.today().isoformat()},{count})")
    conn.commit()
    conn.close()


def add_manufacture(name: str):
    cur.execute(f"INSERT INTO Manufacturers (name) VALUES ({name})")
    conn.commit()
    conn.close()


def delete_manufacture(manufacture_id: int):
    cur.execute(f"DELETE FROM Manufacturers WHERE id_manufacture={manufacture_id}")
    conn.commit()
    conn.close()


def add_category(name: str):
    cur.execute(f"INSERT INTO Categories (name) VALUES ({name})")
    conn.commit()
    conn.close()


def delete_category(category_id: int):
    cur.execute(f"DELETE FROM Categories WHERE id_category={category_id}")
    conn.commit()
    conn.close()


def get_categories():
    cur.execute("SELECT * FROM Categories")
    data = cur.fetchall()
    return data


def get_products_by_category(category_id: int):
    cur.execute(f"SELECT * FROM Products WHERE id_category={category_id}")
    data = cur.fetchall()
    return data


def get_clients():
    cur.execute("SELECT * FROM clients")
    data = cur.fetchall()
    return data


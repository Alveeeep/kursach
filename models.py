import psycopg2
from db import cur, conn
from datetime import date


def get_client_info(client_id):
    cur.execute(f"SELECT * FROM clients WHERE id_client={client_id}")
    data = cur.fetchone()
    return data


def edit_client_info(client_id, email, phone, firstname, lastname):
    cur.execute(
        f"UPDATE clients SET email = %s,phone=%s,firstname=%s,lastname=%s WHERE id_client={client_id}",
        [email, phone, firstname, lastname])
    conn.commit()


def get_product_info(product_id):
    cur.execute(f"SELECT * FROM products WHERE id_product={product_id}")
    data = cur.fetchone()
    return data


def edit_product_info(product_id, name, id_manufacture, id_category, price):
    cur.execute(
        f"UPDATE products SET name='{name}',id_manufacture='{id_manufacture}',id_category='{id_category}',price='{price}' WHERE id_product={product_id}")
    conn.commit()


def create_purchase(client_id, product_id, store_id, count):
    cur.execute(
        f"INSERT INTO purchases (id_client, id_store, purchase_date) VALUES ('{client_id}', '{store_id}', '{date.today().isoformat()}')")
    conn.commit()
    cur.execute("SELECT id_purchase FROM Purchases ORDER BY id_purchase DESC LIMIT 1")
    p_id = cur.fetchone()[0]
    price = get_product_info(product_id)[4]
    cur.execute(
        f"INSERT INTO purchases_payments (id_purchase, id_product, count, price) VALUES ('{p_id}', '{product_id}', '{count}', '{price}')",
        (p_id, product_id, count, price))
    conn.commit()


def get_deliveries_by_product(product_id):
    cur.execute(f"SELECT * FROM deliveries WHERE id_product={product_id}")
    data = cur.fetchall()
    return data


def get_product_count_in_store(product_id, store_id):
    cur.execute(f"SELECT SUM(count) FROM deliveries WHERE id_product={product_id} and id_store={store_id}")
    count_deliveries = cur.fetchone()[0]
    req1 = f"SELECT id_purchase FROM purchases WHERE id_store={store_id}"
    cur.execute(f"SELECT SUM(count) FROM purchases_payments WHERE id_purchase IN ({req1}) and id_product={product_id}")
    count_purchases = cur.fetchone()[0]
    if count_deliveries - count_purchases > 0:
        return count_deliveries - count_purchases
    return 0


def get_products_in_store(store_id):
    cur.execute(
        f"SELECT id_product, SUM(count) as total_count FROM deliveries WHERE id_store={store_id} GROUP BY id_product")
    data = cur.fetchall()
    return data


def add_product(name, id_manufacture, id_category, price):
    cur.execute(
        f"INSERT INTO products (name, id_manufacture, id_category, price) VALUES ('{name}', '{id_manufacture}', '{id_category}', '{price}')")
    conn.commit()


def delete_product(product_id):
    cur.execute(f"DELETE FROM products WHERE id_product={product_id}")
    conn.commit()


def add_delivery(product_id, store_id, delivery_date, count):
    cur.execute(
        f"INSERT INTO deliveries (id_product, id_store, delivery_date, count) VALUES ('{product_id}','{store_id}','{delivery_date}','{count}')")
    conn.commit()


def add_manufacture(name):
    cur.execute(f"INSERT INTO manufacturers (name) VALUES ('{name}')")
    conn.commit()


def delete_manufacture(manufacture_id):
    cur.execute(f"DELETE FROM manufacturers WHERE id_manufacture={manufacture_id}")
    conn.commit()


def add_category(name):
    cur.execute(f"INSERT INTO categories (name) VALUES ('{name}')")
    conn.commit()


def delete_category(category_id):
    cur.execute(f"DELETE FROM categories WHERE id_category={category_id}")
    conn.commit()


def get_categories():
    cur.execute("SELECT * FROM categories")
    data = cur.fetchall()
    return data


def get_products_by_category(category_id):
    cur.execute(f"SELECT * FROM products WHERE id_category={category_id}")
    data = cur.fetchall()
    return data


def get_clients():
    cur.execute("SELECT * FROM clients")
    data = cur.fetchall()
    return data


def get_products():
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    return data


def get_category_name_by_id(category_id):
    cur.execute(f"SELECT name From categories WHERE id_category={category_id}")
    data = cur.fetchone()
    return data


def get_manufacture_name_by_id(manufacture_id):
    cur.execute(f"SELECT name From manufacturers WHERE id_manufacture={manufacture_id}")
    data = cur.fetchone()
    return data


def get_store_info_by_id(store_id):
    cur.execute(f"SELECT * FROM stores WHERE id_store={store_id}")
    data = cur.fetchone()
    return data


def get_deliveries_by_store(store_id):
    cur.execute(f"SELECT * FROM deliveries WHERE id_store={store_id}")
    data = cur.fetchall()
    return data

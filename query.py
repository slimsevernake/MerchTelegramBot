create_database = dict(customer=(
    """CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    address VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(255),
    username VARCHAR(255),
    chat_id INT UNIQUE)"""
), category=(
    """CREATE TABLE category (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(255))"""
), product=(
    """CREATE TABLE product (
    product_id SERIAL PRIMARY KEY,
    category_id INT,
    name VARCHAR(255),
    description TEXT,
    price INT,
    FOREIGN KEY (category_id) REFERENCES category(category_id))"""
), product_photo=(
    """CREATE TABLE product_photo (
    id SERIAL PRIMARY KEY,
    url TEXT,
    product_id INT,
    FOREIGN KEY (product_id) REFERENCES product(product_id))"""
), cart=(
    """CREATE TABLE cart (
    cart_id SERIAL PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id))"""
), cart_product=(
    """CREATE TABLE cart_product (
    cart_id INT,
    product_id INT,
    FOREIGN KEY(product_id) REFERENCES product(product_id),
    FOREIGN KEY(cart_id) REFERENCES cart(cart_id ))"""
))
query_register = dict(insert_register_data=(
    """insert into customer (first_name, last_name, address,
                 email, phone, username, chat_id) 
    values (%s, %s, %s, %s, %s, %s, %s) """
), update_register_data=(
    """update %s set %s where chat_id = %s"""
), select_register_data=(
    """select * from customer where chat_id = """
), delete_register_data=(
    """insert into customer (first_name, last_name, city, adds, 
    email, phone, chat_id) 
    values (%s, %s, %s, %s, %s, %s, %s) """
))
interface_query = dict(category=(
    """SELECT * FROM category"""
), product=(
    """SELECT category.category_name, product.product_id, product.name, 
    product.description, product.price, product_photo.url FROM category LEFT 
    JOIN product ON category.category_id=product.category_id LEFT JOIN 
    product_photo ON product.product_id = product_photo.product_id WHERE 
    category.category_id = """
), display_product_cart=(
    """SELECT product.product_id, product.name, product.description, 
    product.price, product_photo.url FROM customer LEFT JOIN cart ON 
    customer.customer_id = cart.customer_id LEFT JOIN cart_product ON 
    cart_product.cart_id = cart.cart_id LEFT JOIN product ON 
    product.product_id = cart_product.product_id LEFT JOIN product_photo ON 
    product.product_id = product_photo.product_id WHERE customer.chat_id = """
), add_product_cart=(
    """INSERT INTO cart_product (cart_id, product_id) VALUES (%s, %s)"""
), delete_product_cart=(
    """DELETE FROM cart_product WHERE cart_product.cart_id = (SELECT cart_id 
    FROM cart WHERE cart.customer_id=(SELECT customer_id FROM customer WHERE 
    customer.chat_id = )) AND cart_product.product_id = """
), cart_id_info=(
    """SELECT cart.cart_id FROM customer LEFT JOIN cart ON 
    customer.customer_id = cart.customer_id WHERE customer.chat_id = """
))
check_database = dict(check=(
    """SELECT * FROM pg_database WHERE datname='merch_telegram_bot_db'"""
))

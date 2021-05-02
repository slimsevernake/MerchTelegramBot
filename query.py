default_query = {
    'customer': (
        'CREATE TABLE customer ('
        'id SERIAL PRIMARY KEY,'
        'first_name VARCHAR(255),'
        'last_name VARCHAR(255),'
        'adds VARCHAR(255),'
        'email VARCHAR(255),'
        'phone VARCHAR(255),'
        'chat_id INT UNIQUE)'
    ),
    'category': (
        'CREATE TABLE category ('
        'id SERIAL PRIMARY KEY,'
        'category_name VARCHAR(255))'
    ),
    'product': (
        'CREATE TABLE product ('
        'id SERIAL PRIMARY KEY,'
        'category_id INT,'
        'name VARCHAR(255),'
        'description TEXT,'
        'price INT,'
        'FOREIGN KEY (category_id) REFERENCES category(id))'
    ),
    'product_photo': (
        'CREATE TABLE product_photo ('
        'id SERIAL PRIMARY KEY,'
        'url VARCHAR(255),'
        'product_id INT,'
        'FOREIGN KEY (product_id) REFERENCES product(id))'
    ),
    'cart': (
        'CREATE TABLE cart ('
        'id SERIAL PRIMARY KEY,'
        'customer_id INT,'
        'FOREIGN KEY(customer_id) REFERENCES customer(id))'
    ),
    'cart_product': (
        'CREATE TABLE cart_product ('
        'cart_id INT,'
        'product_id INT,'
        'FOREIGN KEY(product_id) REFERENCES product(id),'
        'FOREIGN KEY(cart_id) REFERENCES cart(id))'
    )
}

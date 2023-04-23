__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

import models
from models import db
from test_data import tag_data, user_data, product_data


def test():
    output = db.get_columns('tag')
    print(output)
    # query = models.Tag.select()
    # print(query)
    # for i in query:
    #     print(i.name_tag)


def search(term):
    ...


def list_user_products(user_id):
    ...


def list_products_per_tag(tag_id):
    ...


def add_product_to_catalog(user_id, product):
    ...


def update_stock(product_id, new_quantity):
    ...


def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(product_id):
    ...


def populate_test_database():
    tag_data()
    user_data()
    product_data()


if __name__ == "__main__":
    db.connect()
    db.create_tables([models.Tag, models.Product, models.User,
                     models.Transaction])  # , safe=True
    populate_test_database()


# python main.py
# sqlite3 betsy.db
# .headers ON
# .mode column
# SELECT * FROM tag;
# SELECT * FROM product;
# SELECT * FROM user;

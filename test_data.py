import models


def tag_data():
    data_source = [
        {'name_tag': 'Tafel', 'segment': 'Meubels'},
        {'name_tag': 'Stoel', 'segment': 'Meubels'},
        {'name_tag': 'Kast', 'segment': 'Meubels'},
        {'name_tag': 'Bank', 'segment': 'Meubels'},
        {'name_tag': 'TV', 'segment': 'Elektronika'}
    ]

    # INSERT multiple rows
    models.Tag.insert_many(data_source).execute()


def user_data():
    data_source = [
        {'user_name': 'flipflop', 'email': 'test@bla.nl', 'phonenumber': 656320255,
            'street': "kerklaan", 'street_number': 80, 'postcode': '3306BM', 'place': 'Rotterdam'},
        {'user_name': 'boerenkool', 'email': 'test@bla.nl', 'phonenumber': 656320255,
            'street': "bospad", 'street_number': 204, 'postcode': '1245QW', 'place': 'Arnhem'}
    ]

    # INSERT multiple rows
    models.User.insert_many(data_source).execute()


def product_data():
    data_source = [
        {'product_name': 'Ronde tafel',
            'description': 'Een mooie ronde tafel', 'price_unit': 110, 'quantity_in_stock': 2, 'user_name_id': 1, 'name_tag': 'Tafel'},
        {'product_name': 'Zwarte stoel',
            'description': 'Zarte stoel voor dikke mensen', 'price_unit': 65, 'quantity_in_stock': 3, 'user_name_id': 1, 'name_tag': 'Stoel'},
        {'product_name': 'Stoel op poten',
            'description': 'Deze stoel staat op poten', 'price_unit': 74, 'quantity_in_stock': 1, 'user_name_id': 1, 'name_tag': 'Stoel'},
        {'product_name': 'Bank voor 3 personen',
            'description': 'Een bank voor het hele gezin', 'price_unit': 455, 'quantity_in_stock': 1, 'user_name_id': 1, 'name_tag': 'Bank'},
        {'product_name': 'Houten kast',
            'description': 'Een eiken houten kast van 220 cm hoog', 'price_unit': 250, 'quantity_in_stock': 2, 'user_name_id': 1, 'name_tag': 'Kast'},
        {'product_name': 'Samsung TV',
            'description': 'Nieuw Samsung tv voor aan de muur 56inch', 'price_unit': 889, 'quantity_in_stock': 3, 'user_name_id': 2, 'name_tag': 'TV'}
    ]

    # INSERT multiple rows
    models.Product.insert_many(data_source).execute()

# Models go here
import peewee
import datetime

db = peewee.SqliteDatabase("betsy.db")


class Tag(peewee.Model):
    name_tag = peewee.CharField()
    segment = peewee.CharField()

    class Meta:
        database = db


class User(peewee.Model):
    user_name = peewee.CharField(unique=True)
    email = peewee.CharField()  # checken op type juist!
    phonenumber = peewee.IntegerField()  # checken op type juist!
    street = peewee.CharField()
    street_number = peewee.IntegerField()
    postcode = peewee.CharField()  # checken op type juist!
    place = peewee.CharField()
    # own_products = peewee.ManyToManyField(Product)  # ook many to many?!

    class Meta:
        database = db


class Product(peewee.Model):
    product_name = peewee.CharField()
    description = peewee.TextField()
    price_unit = peewee.DecimalField(rounding=2)
    quantity_in_stock = peewee.IntegerField()
    user_name_id = peewee.ForeignKeyField(User)
    name_tag = peewee.ForeignKeyField(Tag)

    class Meta:
        database = db


class Transaction(peewee.Model):
    transaction_date = peewee.DateTimeField(default=datetime.datetime.now)
    user_buy = peewee.ForeignKeyField(User)
    user_sell = peewee.ForeignKeyField(User)
    purchased_product = peewee.ForeignKeyField(Product)
    quantity = peewee.IntegerField()

    class Meta:
        database = db


# OwnProducts = User.own_products.get_through_model()

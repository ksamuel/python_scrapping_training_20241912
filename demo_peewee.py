import peewee as pw

db = pw.SqliteDatabase("ecommerce.sqlite")


class Product(pw.Model):
    name = pw.CharField()
    price = pw.FloatField()

    class Meta:
        database = db


db.connect()
db.create_tables([Product])

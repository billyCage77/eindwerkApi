from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Product(db.Document):
    name = db.StringField(required=True, unique=True)
    price = db.FloatField(db.StringField(), required=True)
    quantity = db.IntField(db.StringField(), required=True)
    barcode = db.IntField(db.StringField(), required=True)
    added_by = db.ReferenceField('User')

class Supplier(db.Document):
    name = db.StringField(required=True, unique=True) 
    number =  db.IntField(required=True, unique=True)
    adress =  db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    products = db.ListField(db.ReferenceField('Product', reverse_delete_rule=db.PULL))

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

User.register_delete_rule(Product, 'added_by', db.CASCADE)
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(20),nullable=False)
    address= db.Column(db.String(80),nullable=False)
    password=db.Column(db.String(80),nullable=False)
    image = db.Column(db.String(80),nullable=False,default='default.jpd')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image}','{self.address}')"

class Admin(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(20),nullable=False)
    address= db.Column(db.String(80),nullable=False)
    password=db.Column(db.String(80),nullable=False)
    image = db.Column(db.String(80),nullable=False,default='default.jpd')

    def __repr__(self):
        return f"Admin('{self.username}', '{self.email}', '{self.image}','{self.address}')"
class Retailer(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(20),nullable=False)
    address= db.Column(db.String(80),nullable=False)
    password=db.Column(db.String(80),nullable=False)
    image = db.Column(db.String(80),nullable=False,default='default.jpd')

    def __repr__(self):
        return f"Retailer('{self.username}', '{self.email}', '{self.image}','{self.address}')"

class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(70),nullable=False)
    catagory= db.Column(db.String(30),nullable=False)
    brnad = db.Column(db.String(30))
    retailer_id =db.Column(db.Integer,db.ForeignKey(Retailer.id),nullable=False)
    price = db.Column(db.Float,nullable=False)
    previous_price= db.Column(db.Float,nullable=True)
    description = db.Column(db.Text ,nullable =True)
    others = db.Column(db.Text,nullable=True)

    def __repr__(self):
        return f"Product('{self.id}', '{self.name}', '{self.catagory}','{self.brand}','{self.retailer_id}','{self.price}','{self.previous_price}','{self.description}','{self.others}')"








if __name__ == "__main__":
    app.run(port=4000,debug=True)
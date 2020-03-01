from flask import Flask, render_template, url_for, flash, redirect
from myapp import app
from myapp.model import User,Product
from flask import jsonify
from myapp.schema import ProductSchema



Productschemas = ProductSchema(many= True)
Productschema = ProductSchema()
@app.route('/',methods =['GET'])
def home():
    data = Product.query.all()
    result = Productschemas.dump(data)
    return {'products':result}

@app.route('/product/<int:id>',methods = ['GET'])
def get_product(id):
    data= Product.query.get(id)
    result = Productschema.dump(data)
    return {'product':result}

@app.route('/brands/<brandname>')
def brandname(brandname):
    data = Product.query.filter_by(brnad=brandname)
    result = Productschemas.dump(data)
    return {brandname: result}
    

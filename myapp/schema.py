from marshmallow import Schema, fields, ValidationError, pre_load

class UserSchema(Schema):
    id = fields.Int()
    username=fields.Str()
    email = fields.Str()
    address = fields.Str()
    image = fields.Str()

class ProductSchema(Schema):
    id = fields.Int()
    name= fields.Str()
    catagory= fields.Str()
    brnad = fields.Str()
    retailer_id =fields.Int()
    price = fields.Str()
    previous_price= fields.Str()
    description = fields.Str()
    others = fields.Str()
    
    
    

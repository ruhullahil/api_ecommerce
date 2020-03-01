from myapp import db

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
        return f"Product('{self.id}', '{self.name}', '{self.catagory}','{self.brnad}',{self.retailer_id},{self.price},{self.previous_price},'{self.description}','{self.others}')"


class Sellsproduct(db.Model):
    sells_id = db.Column(db.Integer,primary_key = True)
    product_id = db.Column(db.Integer,db.ForeignKey(Product.id),nullable = False)
    conut = db.Column(db.Integer,nullable= False)

    def __repr__(self):
        return f"Sellsproduct('{self.product_id}','{self.conut}')"



class Stokesproduct(db.Model):
    stok_id = db.Column(db.Integer,primary_key = True)
    product_id = db.Column(db.Integer,db.ForeignKey(Product.id),nullable = False)
    conut = db.Column(db.Integer,nullable= False)

    def __repr__(self):
        return f"Stokesproduct('{self.product_id}','{self.conut}')"



class Topsellsproduct(db.Model):
    product_id = db.Column(db.Integer,db.ForeignKey(Product.id),primary_key = True)

    def __repr__(self):
        return f"Topsellsproduct('{self.product_id}')"


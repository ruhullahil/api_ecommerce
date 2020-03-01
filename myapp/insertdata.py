from myapp import db
from myapp.model import User,Retailer,Product


user1 = User(username='ruhullahil',email='ruhullahilt@gmail.com',address='mirpur-2',password='this is test')
user2= User(username='kabir',email='ruhullahilt@gmail.com',address='mirpur-2',password='this is test')
retailer1 = Retailer(username='ruhullahil',email='ruhullahilt@gmail.com',address='mirpur-2',password='this is test')

product1 =Product(name='a50s',catagory='mobile',brnad='samsung',retailer_id=3,price=25000,previous_price=26500,description='none')
product2 =Product(name='a50',catagory='mobile',brnad='samsung',retailer_id=3,price=25000,previous_price=26500,description='none')

db.session.add(user1)
db.session.add(user2)
db.session.add(retailer1)
db.session.add(product1)
db.session.add(product2)
db.session.commit()
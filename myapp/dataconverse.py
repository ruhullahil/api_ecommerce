class jesonProduct():
    def __init__(self,obj):
        self.id= obj.id
        self.name = obj.name
        self.catagory= obj.catagory
        self.brand = obj.brnad
        self.retailer_id= obj.retailer_id
        self.price = obj.price
        self.pervious_price = obj.previous_price
        self.description= obj.description
        self.others= obj.others
    def ret_jesonProduct(self):
        dic={}
        dic['id']=self.id
        dic['name']= self.name
        dic['catagory']=self.catagory
        dic['brand'] = self.brand
        dic['price']=self.price
        dic['pervious_price'] = self.pervious_price
        dic['description'] = self.description
        dic['others']= self.others
    

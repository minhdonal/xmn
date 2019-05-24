from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225))
    img_url = db.Column(db.String(200))
    description = db.Column(db.String(225))
    title = db.Column(db.String(200))
    product_status_id = db.Column(db.Integer)
    regular_price = db.Column(db.Float)
    discount_price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    taxable = db.Column(db.Boolean)

    def __init__(self, name, img_url, description,
    title, product_status_id, regular_price, discount_price,
    quantity, taxable):
        self.name = name
        self.img_url = img_url
        self.description = description
        self.title = title
        self.product_status_id = product_status_id
        self.regular_price = regular_price
        self.discount_price = discount_price
        self.quantity = quantity
        self.taxable


    def __repr__(self):
        if product_status_id != 1:
            return False
        
        return """
            'id': {}, 
            'name': {},
            'title': {},
            'description': {},
            'img_url': {},
            'regular_price': {},
            'quantity': {}
        """.format(
            self.id, self.name, self.title, 
            self.description, self.img_url, 
            self.regular_price, self.quantity)

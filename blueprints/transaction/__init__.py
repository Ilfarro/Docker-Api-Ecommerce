from flask_restful import fields
from blueprints import db

class Transaction(db.Model):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    total_quantity = db.Column(db.Integer)
    total_harga = db.Column(db.Integer)
    payment_method = db.Column(db.String(200))
    payment_status = db.Column(db.String(200))
    created_at = db.Column(db.String(200))
    updated_at = db.Column(db.String(200))
    
    response_field = {
        'id': fields.Integer,
        'user_id': fields.Integer,
        'total_quantity': fields.Integer,
        'total_harga': fields.Integer,
        'payment_method': fields.String,
        'payment_status': fields.String,
        'created_at': fields.String,
        'updated_at': fields.String
    }

    def __init__(self, id, user_id, total_quantity, total_harga, payment_method, payment_status, created_at, updated_at):
        self.id = id
        self.user_id = user_id
        self.total_quantity = total_quantity
        self.total_harga = total_harga
        self.payment_method = payment_method
        self.payment_status = payment_status
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f'<Transaction {self.id}>'

db.create_all()
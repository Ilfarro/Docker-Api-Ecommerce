from flask_restful import fields
from blueprints import db

class Package(db.Model):
    __tablename__ = 'package'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(200))
    jumlah_iklan = db.Column(db.Integer)
    jumlah_iklan_premium = db.Column(db.Integer)
    harga = db.Column(db.Integer)

    response_field = {
        'id': fields.Integer,
        'nama': fields.String,
        'jumlah_iklan': fields.Integer,
        'jumlah_iklan_premium': fields.Integer,
        'harga': fields.Integer
    }

    def __init__(self, id, nama, jumlah_iklan, jumlah_iklan_premium, harga):
        self.id = id
        self.nama = nama
        self.jumlah_iklan = jumlah_iklan
        self.jumlah_iklan_premium = jumlah_iklan_premium
        self.harga = harga

    def __repr__(self):
        return f'<Package {self.id}>'

db.create_all()
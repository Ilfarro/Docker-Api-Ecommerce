from flask_restful import fields
from blueprints import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    phone = db.Column(db.String(200))
    jumlah_iklan = db.Column(db.Integer)
    jumlah_iklan_premium = db.Column(db.Integer)
    url_foto = db.Column(db.String(200))
    status = db.Column(db.String(200))

    response_field = {
        'id': fields.Integer,
        'username': fields.String,
        'password': fields.String,
        'first_name': fields.String,
        'last_name': fields.String,
        'email': fields.String,
        'phone': fields.String,
        'jumlah_iklan': fields.Integer,
        'jumlah_iklan_premium': fields.Integer,
        'url_foto': fields.String,
        'status': fields.String
    }

    def __init__(self, id, username, password, first_name, last_name, email, phone, jumlah_iklan, jumlah_iklan_premium, url_foto, status):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.jumlah_iklan = jumlah_iklan
        self.jumlah_iklan_premium = jumlah_iklan_premium
        self.url_foto = url_foto
        self.status = status

    def __repr__(self):
        return f'<Users {self.id}>'

db.create_all()
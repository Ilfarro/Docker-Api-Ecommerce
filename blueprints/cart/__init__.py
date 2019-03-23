from flask import Blueprint, Flask
import json
from flask_restful import Resource, Api, reqparse, marshal
from . import *
from flask_restful import fields
from blueprints import db

class Cart(db.Model):
    __tablename__ = 'cart'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    package_id = db.Column(db.Integer)
    transaction_id = db.Column(db.Integer)
    nama_package = db.Column(db.String(200))
    quantity = db.Column(db.Integer)
    harga = db.Column(db.Integer)
    created_at = db.Column(db.String(200))
    updated_at = db.Column(db.String(200))

    response_field = {
        'id': fields.Integer,
        'user_id': fields.Integer,
        'package_id': fields.Integer,
        'transaction_id': fields.Integer,
        'nama_package': fields.String,
        'quantity': fields.Integer,
        'harga': fields.Integer,
        'created_at': fields.String,
        'updated_at': fields.String
    }

    def __init__(self, id, user_id, package_id, transaction_id, nama_package, quantity, harga, created_at, updated_at):
        self.id = id
        self.user_id = user_id
        self.package_id = package_id
        self.transaction_id = transaction_id
        self.nama_package = nama_package
        self.quantity = quantity
        self.harga = harga
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f'<Cart {self.id}>'

db.create_all()
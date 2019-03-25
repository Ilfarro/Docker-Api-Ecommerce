import json
from flask_restful import Resource, Api, reqparse, marshal
from flask import Blueprint, Flask
from . import *
from blueprints.users import *
from blueprints.package import *
from blueprints import db
from datetime import date, datetime

from flask_jwt_extended import jwt_required, get_jwt_claims

bp_cart = Blueprint('cart', __name__)
api = Api(bp_cart)

class CartResource(Resource):

    @jwt_required
    def get(self,id=None):
        if id is None:
            user_id = get_jwt_claims()['id']
            parser = reqparse.RequestParser()
            parser.add_argument('p',type=int, location='args', default=1)
            parser.add_argument('rp',type=int, location='args', default=100)
            parser.add_argument('id',type=int, location='args')
            parser.add_argument('nama_package', location='args')
            args = parser.parse_args()
            
            offset = (args['p'] * args['rp']) - args['rp']

            qry = Cart.query.filter_by(user_id=user_id).filter_by(transaction_id=0)

            if args['id'] is not None:
                qry = qry.filter_by(id=args['id'])
            if args['nama_package'] is not None:
                qry = qry.filter(Cart.nama_package.like("%"+args['nama_package']+"%"))

            rows = []
            for row in qry.limit(args['rp']).offset(offset).all():
                rows.append(marshal(row, Cart.response_field))
            return {'status': 'Success', 'halaman': args['p'], 'data': rows}, 200, { 'Content-Type': 'application/json' }

        else :
            user_id = get_jwt_claims()['id']
            qry = Cart.query.filter_by(user_id=user_id).filter_by(id=id).first()
            if qry is not None:
                return {'status': 'Success', 'data': marshal(qry, Cart.response_field)}, 200, { 'Content-Type': 'application/json' }
            return {'status': 'NOT_FOUND','message':'item not found'},404, { 'Content-Type': 'application/json' }
    
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('package_id', location='json')
        args = parser.parse_args()

        qry = Package.query.get(args['package_id'])
        if qry is None:
            return {'status': 'Failed', 'message': 'Invalid item id'}, 404, {'Content-Type': 'application/json'}

        user_id = get_jwt_claims()['id']
        transaction_id = 0
        nama_package = marshal(qry, Package.response_field)['nama']
        created_at = datetime.now()
        updated_at = datetime.now()
        quantity = 1
        harga = marshal(qry, Package.response_field)['harga']

        cart = Cart(None, user_id, args['package_id'], transaction_id, nama_package, quantity, harga, created_at, updated_at)
        db.session.add(cart)
        db.session.commit()

        if cart is not None:
            return {'status': 'Success', 'data': marshal(cart, Cart.response_field)}, 200, { 'Content-Type': 'application/json' }
        return {'status': 'Failed', 'message': 'Failed to add cart'}, 404, {'Content-Type': 'application/json'}
        
    @jwt_required
    def delete(self,id):
        user_id = get_jwt_claims()['id']
        qry = Cart.query.filter_by(user_id=user_id).filter_by(id=id).first()
        if qry is not None:
            db.session.delete(qry)
            db.session.commit()
            return {'status': "Success", 'message': 'Cart deleted'}, 200, {'Content-Type': 'application/json'}
        return {'status': 'Not Found','message':'Cart not found'},404, { 'Content-Type': 'application/json' }

api.add_resource(CartResource, '/cart', '/cart/<int:id>')
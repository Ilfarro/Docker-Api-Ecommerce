import json
from flask_restful import Resource, Api, reqparse, marshal
from flask import Blueprint, Flask
from . import *
from blueprints.users import *
from blueprints.cart import *
from blueprints.package import *
from blueprints import db
from datetime import date, datetime

from flask_jwt_extended import jwt_required, get_jwt_claims

bp_transaction = Blueprint('transaction', __name__)
api = Api(bp_transaction)

class TransactionResource(Resource):

    @jwt_required
    def get(self,id=None):
        if id is None:
            user_id = get_jwt_claims()['id']
            parser = reqparse.RequestParser()
            parser.add_argument('p',type=int, location='args', default=1)
            parser.add_argument('rp',type=int, location='args', default=100)
            parser.add_argument('id',type=int, location='args')
            parser.add_argument('payment_method', location='args')
            parser.add_argument('payment_status', location='args')
            args = parser.parse_args()
            
            offset = (args['p'] * args['rp']) - args['rp']

            qry = Transaction.query.filter_by(user_id=user_id)

            if args['id'] is not None:
                qry = qry.filter_by(id=args['id'])
            if args['payment_method'] is not None:
                qry = qry.filter(Transaction.payment_method.like("%"+args['payment_method']+"%"))
            if args['payment_status'] is not None:
                qry = qry.filter(Transaction.payment_status.like("%"+args['payment_status']+"%"))

            rows = []
            for row in qry.limit(args['rp']).offset(offset).all():
                rows.append(marshal(row, Transaction.response_field))
            return {'status': 'Success', 'halaman': args['p'], 'data': rows}, 200, { 'Content-Type': 'application/json' }

        else :
            user_id = get_jwt_claims()['id']
            qry = Transaction.query.filter_by(user_id=user_id).filter_by(id=id).first()
            if qry is not None:
                return {'status': 'Success', 'data': marshal(qry, Transaction.response_field)}, 200, { 'Content-Type': 'application/json' }
            return {'status': 'NOT_FOUND','message':'Transaction not found'},404, { 'Content-Type': 'application/json' }
    
    @jwt_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('payment_method', location='json')
        args = parser.parse_args()

        user_id = get_jwt_claims()['id']
        created_at = datetime.now()
        updated_at = datetime.now()

        cart_qry = Cart.query.filter_by(user_id = user_id).filter_by(transaction_id = 0)
        if cart_qry is None:
            return {'status': 'Failed', 'message': 'Invalid cart'}, 404, {'Content-Type': 'application/json'}

        payment_status = 'paid'
        total_quantity = 0
        total_harga = 0
        for element in cart_qry.all():
            temp = marshal(element, Cart.response_field)
            total_quantity += temp['quantity']
            total_harga += temp['harga']

        transaction_qry = Transaction(None, user_id, total_quantity, total_harga, args['payment_method'], payment_status, created_at, updated_at)
        db.session.add(transaction_qry)
        db.session.commit()

        for element in cart_qry.all():
            element.transaction_id = transaction_qry.id
        db.session.commit()

        if transaction_qry is not None:
            return {'status': 'Success', 'data': marshal(transaction_qry, Transaction.response_field)}, 200, { 'Content-Type': 'application/json' }
        return {'status': 'Failed', 'message': 'Failed to add cart'}, 404, {'Content-Type': 'application/json'}
        
    @jwt_required
    def delete(self,id):
        user_id = get_jwt_claims()['id']
        qry = Transaction.query.filter_by(user_id=user_id).filter_by(id=id).first()
        if qry is not None:
            db.session.delete(qry)
            db.session.commit()
            return {'status': "Success", 'message': 'Transaction deleted'}, 200, {'Content-Type': 'application/json'}
        return {'status': 'Not Found','message':'Transaction not found'},404, { 'Content-Type': 'application/json' }

api.add_resource(TransactionResource, '/transaction', '/transaction/<int:id>')
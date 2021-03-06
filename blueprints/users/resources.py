import json
from flask_restful import Resource, Api, reqparse, marshal
from flask import Blueprint, Flask
from . import *
from blueprints.cart import *
from blueprints import db
from datetime import date, datetime

from flask_jwt_extended import jwt_required, get_jwt_claims

bp_users = Blueprint('users', __name__)
api = Api(bp_users)

class UsersRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='json', required=True)
        parser.add_argument('password', location='json', required=True)
        parser.add_argument('first_name', location='json', required=True)
        parser.add_argument('last_name', location='json', required=True)
        parser.add_argument('email', location='json', required=True)
        parser.add_argument('phone', location='json', required=True)
        parser.add_argument('jumlah_iklan', location='json', default=0)
        parser.add_argument('jumlah_iklan_premium', location='json', default=0)
        parser.add_argument('url_foto', location='json', default='http://dismagazine.com/uploads/2011/08/notw_silhouette-1.jpg')
        parser.add_argument('status', location='json', default='user')
        args = parser.parse_args()

        users = Users(None, args['username'], args['password'], args['first_name'], args['last_name'], args['email'], args['phone'], args['jumlah_iklan'], args['jumlah_iklan_premium'], args['url_foto'], args['status'])
        db.session.add(users)
        db.session.commit()

        if users is not None:
            return {'status': 'Success', 'message': 'User added', 'data': marshal(users, Users.response_field)}, 200, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}
        return {'status': 'Failed', 'message': 'Please fill the field'}, 404, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

class UsersMe(Resource):
    @jwt_required
    def get(self):
        qry = Users.query.get(get_jwt_claims()['id'])
        if qry is not None:
            return {'status': 'Success', 'data': marshal(qry, Users.response_field)}, 200, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}
        return {'status': 'Not Found', 'message': 'User not found'}, 404, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

    @jwt_required
    def patch(self, id):
        qry = Users.query.get(id)
        
        parser = reqparse.RequestParser()
        parser.add_argument('username', location='json')
        parser.add_argument('password', location='json')
        parser.add_argument('first_name', location='json')
        parser.add_argument('last_name', location='json')
        parser.add_argument('email', location='json')
        parser.add_argument('phone', location='json')
        parser.add_argument('jumlah_iklan', location='json')
        parser.add_argument('jumlah_iklan_premium', location='json')
        parser.add_argument('url_foto', location='json')
        parser.add_argument('status', location='json')
        args = parser.parse_args()

        user_qry = Users.query.get(get_jwt_claims()['id'])

        if args['password'] is not None:
            qry.password = args['password']
        if args['first_name'] is not None:
            qry.first_name = args['first_name']
        if args['last_name'] is not None:
            qry.last_name = args['last_name']
        if args['email'] is not None:
            qry.email = args['email']
        if args['phone'] is not None:
            qry.phone = args['phone']
        if args['jumlah_iklan'] is not None:
            qry.jumlah_iklan = args['jumlah_iklan']
        if args['jumlah_iklan_premium'] is not None:
            qry.jumlah_iklan_premium = args['jumlah_iklan_premium']
        if args['url_foto'] is not None:
            qry.url_foto = args['url_foto']
        if args['status'] is not None:
            qry.status = args['status']

        db.session.commit()
        if qry is not None:
            return {'status': 'Success', 'data': marshal(qry, Users.response_field)}, 200, {'Content-Type': 'application/json'}
        return {'status': 'Not Found', 'message': 'User not found'}, 404, {'Content-Type': 'application/json'}

    @jwt_required
    def delete(self, id):
        qry = Users.query.get(id)
        if qry is not None:
            db.session.delete(qry)
            db.session.commit()
            return {'status': "Success", 'message': 'User deleted'}, 200, {'Content-Type': 'application/json'}

        return {'status': 'Not Found', 'message': 'User not found'}, 404, {'Content-Type': 'application/json'}

api.add_resource(UsersRegister, '/register')
api.add_resource(UsersMe, '/me', '/me/<int:id>')
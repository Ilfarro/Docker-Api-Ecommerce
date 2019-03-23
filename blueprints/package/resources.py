import json
from flask_restful import Resource, Api, reqparse, marshal
from flask import Blueprint, Flask
from . import *
from blueprints.users import *
from blueprints import db

from flask_jwt_extended import jwt_required, get_jwt_claims

bp_package = Blueprint('package', __name__)
api = Api(bp_package)
class PackageResource(Resource):
    @jwt_required
    def get(self, id=None):
        if id is None:
            parser = reqparse.RequestParser()
            parser.add_argument('p', type=int, location='args', default=1)
            parser.add_argument('rp', type=int, location='args', default=100)
            args = parser.parse_args()

            offset = (args['p'] * args['rp']) - args['rp']  

            qry = Package.query
            rows = []
            for row in qry.limit(args['rp']).offset(offset).all():
                rows.append(marshal(row, Package.response_field))
            return {'status': 'Success', 'halaman': args['p'], 'data': rows}, 200, {'Content-Type': 'application/json'}

        else:
            qry = Package.query.get(id)
            if qry is not None:
                return marshal(qry, Package.response_field), 200, {'Content-Type': 'application/json'}
            return {'status': 'Not Found', 'message': 'Package not found'}, 404, {'Content-Type': 'application/json'}

    @jwt_required
    def post(self):
        status = get_jwt_claims()['status']
        if status != "admin":
            return {'message':'Only Admin can post new Package'}, 404, { 'Content-Type': 'application/json' }
        parser = reqparse.RequestParser()
        parser.add_argument('nama', location='json', required=True)
        parser.add_argument('jumlah_iklan', location='json', required=True)
        parser.add_argument('jumlah_iklan_premium', location='json', required=True)
        parser.add_argument('harga', location='json', required=True)
        args = parser.parse_args()

        package = Package(None, args['nama'], args['jumlah_iklan'], args['jumlah_iklan_premium'], args['harga'])
        db.session.add(package)
        db.session.commit()

        if package is not None:
            return {'status': 'Success', 'data': marshal(package, Package.response_field)}, 200, {'Content-Type': 'application/json'}
        return {'status': 'Failed', 'message': 'Failed to add Package'}, 404, {'Content-Type': 'application/json'}
        
    @jwt_required
    def patch(self, id):
        status = get_jwt_claims()['status']
        if status != "admin":
            return {'message':'Only Admin can edit Package'}, 404, { 'Content-Type': 'application/json' }

        qry = Package.query.get(id)
        
        parser = reqparse.RequestParser()
        parser.add_argument('nama', location='json')
        parser.add_argument('jumlah_iklan', location='json')
        parser.add_argument('jumlah_iklan_premium', location='json')
        parser.add_argument('harga', location='json')
        args = parser.parse_args()

        if args['nama'] is not None:
            qry.nama = args['nama']
        if args['jumlah_iklan'] is not None:
            qry.jumlah_iklan = args['jumlah_iklan']
        if args['jumlah_iklan_premium'] is not None:
            qry.jumlah_iklan_premium = args['jumlah_iklan_premium']
        if args['harga'] is not None:
            qry.harga = args['harga']

        db.session.commit()

        if qry is not None:
            return {'status': 'Success', 'data': marshal(qry, Package.response_field)}, 200, {'Content-Type': 'application/json'}
        return {'status': 'Not Found', 'message': 'Package not found'}, 404, {'Content-Type': 'application/json'}

    @jwt_required
    def delete(self, id):
        status = get_jwt_claims()['status']
        if status != "admin":
            return {'message':'Only Admin can delete Package'}, 404, { 'Content-Type': 'application/json' }
        qry = Package.query.get(id)
        if qry is not None:
            db.session.delete(qry)
            db.session.commit()
            return {'status': "Success", 'message': 'Package deleted'}, 200, {'Content-Type': 'application/json'}
        return {'status': 'Not Found', 'message': 'Package not found'}, 404, {'Content-Type': 'application/json'}

api.add_resource(PackageResource, '/package', '/package/<int:id>')
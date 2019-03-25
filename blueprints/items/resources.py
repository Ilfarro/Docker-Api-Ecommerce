import json
from flask_restful import Resource, Api, reqparse, marshal
from flask import Blueprint, Flask
from . import *
from blueprints.users import *
from blueprints import db

from flask_jwt_extended import jwt_required, get_jwt_claims

bp_items = Blueprint('items', __name__)
api = Api(bp_items)
class ItemsAuthenticated(Resource):
    @jwt_required
    def get(self, id=None):
        if id is None:
            parser = reqparse.RequestParser()
            parser.add_argument('p', type=int, location='args', default=1)
            parser.add_argument('rp', type=int, location='args', default=100)
            parser.add_argument('search', location='args')
            parser.add_argument('status_item', location='args')
            parser.add_argument('post_by', location='args')
            args = parser.parse_args()

            offset = (args['p'] * args['rp']) - args['rp']  

            qry = Items.query

            if args['search'] is not None:
                qry = qry.filter(Items.kategori.like("%"+args['search']+"%"))
                if qry.first() is None:
                    qry = Items.query.filter(Items.nama.like("%"+args['search']+"%"))
                    if qry.first() is None:
                        qry = Items.query.filter(Items.deskripsi.like("%"+args['search']+"%"))
                        if qry.first() is None:
                            qry = Items.query.filter(Items.lokasi.like("%"+args['search']+"%"))
                            if qry.first() is None:
                                return {'status': 'Not Found', 'message': 'Item not found'}, 404, {'Content-Type': 'application/json'}

            if args['status_item'] is not None:
                qry = qry.filter(Items.status_item.like("%"+args['status_item']+"%"))

            if args['post_by'] is not None:
                qry = qry.filter(Items.post_by.like("%"+args['post_by']+"%"))
            
            rows = []
            for row in qry.limit(args['rp']).offset(offset).all():
                rows.append(marshal(row, Items.response_field))
            return {'status': 'Success', 'halaman': args['p'], 'data': rows}, 200, {'Content-Type': 'application/json'}

        else:
            qry = Items.query.get(id)
            if qry is not None:
                return marshal(qry, Items.response_field), 200, {'Content-Type': 'application/json'}
            return {'status': 'Not Found', 'message': 'Item not found'}, 404, {'Content-Type': 'application/json'}

    @jwt_required
    def post(self):
        users_id = get_jwt_claims()["id"]
        parser = reqparse.RequestParser()
        parser.add_argument('kategori', location='json', required=True)
        parser.add_argument('nama', location='json', required=True)
        parser.add_argument('deskripsi', location='json', required=True)
        parser.add_argument('harga', location='json', required=True)
        parser.add_argument('lokasi', location='json', required=True)
        parser.add_argument('url_foto', location='json', required=True)
        args = parser.parse_args()

        status_item = 'regular'

        user_qry = Users.query.get(get_jwt_claims()['id'])

        if status_item == "regular" and user_qry.jumlah_iklan > 0:
            user_qry.jumlah_iklan -= 1
        elif status_item == "premium" and user_qry.jumlah_iklan_premium > 0:
            user_qry.jumlah_iklan_premium -= 1
        else:
            return {'status': 'Failed', 'message': 'Failed to add item'}, 404, {'Content-Type': 'application/json'}

        items = Items(None, args['kategori'], args['nama'], args['deskripsi'], args['harga'], args['lokasi'], args['url_foto'], status_item, users_id)
        db.session.add(items)
        db.session.commit()

        if items is not None:
            return {'status': 'Success', 'data': marshal(items, Items.response_field)}, 200, {'Content-Type': 'application/json'}
        return {'status': 'Failed', 'message': 'Failed to add item'}, 404, {'Content-Type': 'application/json'}
        
    @jwt_required
    def patch(self, id):
        users_id = get_jwt_claims()["id"]
        qry = Items.query.get(id)
        
        parser = reqparse.RequestParser()
        parser.add_argument('kategori', location='json')
        parser.add_argument('nama', location='json')
        parser.add_argument('deskripsi', location='json')
        parser.add_argument('harga', location='json')
        parser.add_argument('lokasi', location='json')
        parser.add_argument('url_foto', location='json')
        parser.add_argument('status_item', location='json')
        args = parser.parse_args()

        user_qry = Users.query.get(get_jwt_claims()['id'])

        if args['kategori'] is not None:
            qry.kategori = args['kategori']
        if args['nama'] is not None:
            qry.nama = args['nama']
        if args['deskripsi'] is not None:
            qry.deskripsi = args['deskripsi']
        if args['harga'] is not None:
            qry.harga = args['harga']
        if args['lokasi'] is not None:
            qry.lokasi = args['lokasi']
        if args['url_foto'] is not None:
            qry.url_foto = args['url_foto']
        if args['status_item'] is not None:
            qry.status_item = args['status_item']
            if args['status_item'] == "premium" and user_qry.jumlah_iklan_premium > 0:
                user_qry.jumlah_iklan_premium -= 1
            else:
                return {'status': 'Failed', 'message': 'Failed to edit item'}, 404, {'Content-Type': 'application/json'}

        db.session.commit()
        if qry is not None:
            return {'status': 'Success', 'data': marshal(qry, Items.response_field)}, 200, {'Content-Type': 'application/json'}
        return {'status': 'Not Found', 'message': 'Item not found'}, 404, {'Content-Type': 'application/json'}

    @jwt_required
    def delete(self, id):
        users_id = get_jwt_claims()["id"]
        qry = Items.query.get(id)
        if qry is not None:
            db.session.delete(qry)
            db.session.commit()
            return {'status': "Success", 'message': 'Item deleted'}, 200, {'Content-Type': 'application/json'}

        return {'status': 'Not Found', 'message': 'Item not found'}, 404, {'Content-Type': 'application/json'}
        
class ItemsPublic(Resource):
    def get(self, id=None):
        if id is None:
            parser = reqparse.RequestParser()
            parser.add_argument('p', type=int, location='args', default=1)
            parser.add_argument('rp', type=int, location='args', default=100)
            parser.add_argument('search', location='args')
            parser.add_argument('status_item', location='args')
            parser.add_argument('kategori', location='args')
            args = parser.parse_args()

            offset = (args['p'] * args['rp']) - args['rp']  
            
            qry = Items.query

            if args['search'] is not None:
                qry = qry.filter(Items.kategori.like("%"+args['search']+"%"))
                if qry.first() is None:
                    qry = Items.query.filter(Items.nama.like("%"+args['search']+"%"))
                    if qry.first() is None:
                        qry = Items.query.filter(Items.deskripsi.like("%"+args['search']+"%"))
                        if qry.first() is None:
                            qry = Items.query.filter(Items.lokasi.like("%"+args['search']+"%"))
                            if qry.first() is None:
                                return {'status': 'Not Found', 'message': 'Item not found'}, 404, {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}

            if args['status_item'] is not None:
                qry = qry.filter(Items.status_item.like("%"+args['status_item']+"%"))

            if args['kategori'] is not None:
                qry = qry.filter(Items.kategori.like("%"+args['kategori']+"%"))

            rows = []
            for row in qry.limit(args['rp']).offset(offset).all():
                rows.append(marshal(row, Items.response_field))
            return {'status': 'Success', 'halaman': args['p'], 'data': rows}, 200, {'Content-Type': 'application/json'}

        else:
            qry = Items.query.get(id)
            if qry is not None:
                return marshal(qry, Items.response_field), 200, {'Content-Type': 'application/json'}
            return {'status': 'Not Found', 'message': 'Item not found'}, 404, {'Content-Type': 'application/json'}

api.add_resource(ItemsAuthenticated, '/users/items', '/users/items/<int:id>')
api.add_resource(ItemsPublic, '/public/items', '/public/items/<int:id>')
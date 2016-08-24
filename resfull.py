#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, make_response
from flask_restful import fields, marshal, Api, Resource
from flask.ext.restful import reqparse

app = Flask(__name__)
api = Api(app)

class QueryAPI(Resource):
	"""docstring for QueryAPI"""
	def __init__(self):
		self.reqparse = reqparse.RequestParser()
		self.reqparse.add_argument('cust_id', type=int, required=True, location='args')
		self.reqparse.add_argument('ip', type=str, required=True, location='args')
		super(QueryAPI, self).__init__()

	def get(self):
		args = self.reqparse.parse_args()
		print args['cust_id']
		print args['ip']

		return {'msg':'ok'}, 200


api.add_resource(QueryAPI, '/query')

if __name__ == '__main__':
	app.run(debug=True)	
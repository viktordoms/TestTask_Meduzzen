from app import db
from models.models import *
from src.validates.validation import validate

from flask import request, jsonify
from flask_restful import Resource
from serializers.serializer import user_schema
from werkzeug.security import generate_password_hash


class UserView(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id)
        res = user_schema.dump(user)
        if res:
            return jsonify(res)
        else:
            return {"response": 'User not found'}, 404

    def delete(self, id):
        user = User.query.get(id)
        try:
            db.session.delete(user)
            db.session.commit()
            return {"response": 'User delete'}, 200
        except:
            return {"response": 'User not found'}, 404

    def patch(self, id):
        user = User.query.get(id)
        if user:
            data = {
                'id': id,
                "username": request.json.get('username', user.username),
                "email": request.json.get('email', user.email),
                "password": request.json.get('password', user.password),
                "password2": request.json.get('password2', user.password)
            }
            response_validator = validate(data)
            if response_validator:
                return response_validator
            else:
                user.email = request.json.get('email', user.email)
                user.username = request.json.get('username', user.username)
                user.password = generate_password_hash(request.json.get('password', user.password))

                try:
                    db.session.commit()
                    return {'response': 'Update successful'}, 200
                except:
                    return {'response': 'Error update'}, 400
        else:
            return {'response': 'User not found'}, 404

    def put(self, id):
        user = User.query.get(id)
        if user:
            try:
                data = {
                    'id': id,
                    "username": request.json['username'],
                    "email": request.json['email'],
                    "password": request.json['password'],
                    "password2": request.json['password2']
                }
            except KeyError:
                return {'response': 'You must enter and update all parameter'}, 400

            response_validator = validate(data)
            if response_validator:
                return response_validator
            else:
                user.email = request.json['email']
                user.username = request.json['username']
                user.password = generate_password_hash(request.json['password'])
                try:
                    db.session.commit()
                    return {'response': 'Update successful'}, 200
                except:
                    return {'response': 'Update error'}, 400
        else:
            return {'response': 'User not found'}, 404


class AddUsersView(Resource):
    def post(self):
        try:
            id = request.form.get('id')
            register_date = request.form.get('register_date')
            username = request.json['username']
            email = request.json['email']
            password = request.json['password']
            password2 = request.json['password2']
        except KeyError:
            return {"response": "Enter all dates"}, 400

        data = {
            "id": id,
            "username": username,
            "email": email,
            "password": password,
            "password2": password2
        }

        response_validator = validate(data)

        if response_validator:
            return response_validator
        else:
            has_password = generate_password_hash(password)
            use = User(
                id=id,
                username=username,
                register_date=register_date,
                email=email,
                password=has_password
            )
            try:
                db.session.add(use)
                db.session.commit()
                return {'response': 'User add to database'}, 201
            except:
                return {'response': 'Error add to database'}, 400


class UsersView(Resource):
    def get(self):
        data = User.query.all()
        responce_database = user_schema.dump(data)
        if responce_database:
            return jsonify(responce_database)
        else:
            return {"response": 'Database is empty'}, 404

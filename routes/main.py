from app import db
from models.models import *
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
            if request.json.get("email", False):
                if not isinstance(request.json['email'], str):
                    return {"response": 'Email must be string. Enter correct email.'}, 400
                else:
                    if User.query.filter(User.email == request.json['email']).first():
                        return {"response": 'User with this email is already exist'}, 400
                    else:
                        if len(request.json['email']) >= 5:
                            user.email = request.json['email']
                        else:
                            return {"response": 'Email should be longer than 5 characters'}, 400

            if request.json.get('username', False):
                if not isinstance(request.json['username'], str):
                    return {"response": 'Username must be string. Enter correct username.'}, 400
                else:
                    if User.query.filter(User.username == request.json['username']).first():
                        return {"response": 'User with this username is already exist'}, 400
                    else:
                        if len(request.json['username']) >= 4:
                            user.username = request.json['username']
                        else:
                            return {"response": 'Username should be longer than 4 characters'}, 400
            if request.json.get('password', False):
                if len(request.json['password']) >= 8:
                    user.password = generate_password_hash(request.json['password'])
                else:
                    return {"response": 'Password should be longer than 8 characters'}, 400
        else:
            return {"response": 'User not found'}, 404
        try:
            db.session.commit()
            return {"response": 'Update successful'}, 200
        except:
            return {"response": 'Update error'}, 400

    def put(self, id):
        user = User.query.get(id)
        try:
            if user:
                if not isinstance(request.json['email'], str):
                    return {"response": 'Email must be string. Enter correct email.'}, 400
                elif not isinstance(request.json['username'], str):
                    return {"response": 'Username must be string. Enter correct username.'}, 400
                else:
                    if User.query.filter(User.email == request.json['email']).first():
                        return {"response": 'User with this email is already exist'}, 400
                    if User.query.filter(User.username == request.json['username']).first():
                        return {"response": 'User with this username is already exist'}, 400
                    else:
                        if len(request.json['email']) >= 5:
                            user.email = request.json['email']
                        else:
                            return {"response": 'Email should be longer than 5 characters'}, 400

                        if len(request.json['username']) >= 4:
                             user.username = request.json['username']
                        else:
                            return {"response": 'Username should be longer than 5 characters'}, 400

                        if len(request.json['password']) >= 8:
                            user.password = generate_password_hash(request.json['password'])
                        else:
                            return {"response": 'Password should be longer than 8 characters'}, 400

            else:
                return {'response': 'User not found'}, 404
        except KeyError:
            return {'response': 'You must enter and update all parameter'}, 400

        try:
            db.session.commit()
            return {'request': 'Update successful'}, 200
        except:
            return {'request': 'Update error'}, 400


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

        if not isinstance(email, str):
            return {'response': 'Email must be string. Enter correct email.'}, 400
        if not isinstance(username, str):
            return {'response': 'Username must be string. Enter correct username.'}, 400

        if User.query.filter(User.email == email).first():
            return {'response': 'User with this email is already exist'}, 400
        if User.query.filter(User.username == username).first():
            return {'response': 'User with this username is already exist'}, 400
        if len(email) <= 5:
            return {'response': 'Email should be longer than 5 characters'}, 400
        if len(username) <= 4:
            return {'response': 'Username should be longer than 4 characters'}, 400
        if len(password) <= 8:
            return {'response': 'Password should be longer than 8 characters'}, 400
        if password != password2:
            return {'response': 'Password is not curable'}, 400

        else:
            has_password = generate_password_hash(password)
            user = User(
                id=id,
                username=username,
                register_date=register_date,
                email=email,
                password=has_password
            )
            try:
                db.session.add(user)
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

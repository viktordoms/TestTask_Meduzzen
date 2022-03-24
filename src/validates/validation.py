from models.models import *
from sqlalchemy import and_


def validator(data, param, object_filter, len_param, object_id):
    if not isinstance(data[param], str):
        return {'response': f'{param} must be string. Enter correct {param}].'}, 400
    if User.query.filter(and_(object_filter == data[param], object_id != data['id'])).first():
        return {'response': f'User with this {param} is already exist'}, 400
    if len(data[param]) <= len_param:
        return {'response': f'{param} should be longer than {len_param} characters'}, 400


def validator_password(data, password, password2, len_param):
    if not isinstance(data[password], str):
        return {'response': f'{password} must be string. Enter correct {password}.'}, 400
    if not isinstance(data[password2], str):
        return {'response': f'{password2} must be string. Enter correct {password2}.'}, 400
    if len(data[password]) <= len_param:
        return {'response': f'{password} should be longer than {len_param} characters'}, 400
    if data[password] != data[password2]:
        return {'response': f'{password} is not curable'}, 400


def validate(data):

   valid_email = validator(data=data, param='email', object_filter=User.email, object_id=User.id, len_param=5)
   valid_username = validator(data=data, param='username', object_filter=User.username, object_id=User.id, len_param=4)
   valid_password = validator_password(data=data, password='password', password2='password2', len_param=8)

   if valid_email:
       return valid_email
   elif valid_username:
       return valid_username
   elif valid_password:
       return valid_password
   else:
       return False



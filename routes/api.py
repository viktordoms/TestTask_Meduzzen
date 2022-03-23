from app import *
from .main import *


api.add_resource(AddUsersView, '/user')
api.add_resource(UsersView, '/user_list')
api.add_resource(UserView, '/user/<int:id>')

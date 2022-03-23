from app import marshmallow


class UserSchema(marshmallow.Schema):
    class Meta:

        fields = ['id', 'username', 'email', 'password', 'register_date']


user_schema = UserSchema(many=True)

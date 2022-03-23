USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "email": {"type": "string"},
        "password": {"type": "string"},
        "username": {"type": "string"},
        "register_date": {"type": "string"}
    },
    "required": ['id', 'email', 'username', 'password', 'register_date']
}

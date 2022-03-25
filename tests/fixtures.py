data_create_user = [
    ('user1@user', 'user1', '1234567890', '1234567890', 'User add to database', 201),
    ('user1@user', 'user1', '1234567890', '1234567890', 'User with this email is already exist', 400),
    ('user20@user', 'user1', '1234567890', '1234567890', 'User with this username is already exist', 400),
    ('user', 'user2', '1234567890', '1234567890', 'email should be longer than 5 characters', 400),
    ('user20@user', 'use', '1234567890', '1234567890', 'username should be longer than 4 characters', 400),
    ('user20@user', 'user20', '1234567', '1234567', 'password should be longer than 8 characters', 400),
    ('user20@user', 'user20', '1234567890', '1234567', 'password is not curable', 400),
    (12425435, 'user20', '1234567890', '1234567890', 'email must be string. Enter correct email.', 400),
    ('user20@user', 1241352, '1234567890', '1234567', 'username must be string. Enter correct username.', 400),
    ('user20@user', 'user20', 1234567890, '1234567', 'password must be string. Enter correct password.', 400),
    ('user20@user', 'user20', '1234567890', 1243545435, 'password2 must be string. Enter correct password2.', 400),
    ('user2@user', 'user2', '1234567890', '1234567890', 'User add to database', 201)]

data_put_user = [
    ('user1@user', 'user1', '1234567890', '1234567890', 'User with this email is already exist', 400),
    ('user3@user', 'user1', '1234567890', '1234567890', 'User with this username is already exist', 400),
    ('user', 'user1', '1234567890', '1234567890', 'email should be longer than 5 characters', 400),
    ('user3@user', 'use', '1234567890', '1234567890', 'username should be longer than 4 characters', 400),
    ('user3@user', 'user3', '1234567', '1234567', 'password should be longer than 8 characters', 400),
    ('user3@user', 'user3', '1234567890', '1234567', 'password is not curable', 400),
    (12425435, 'user3', '1234567890', '1234567890', 'email must be string. Enter correct email.', 400),
    ('user3@user', 1241352, '1234567890', '1234567', 'username must be string. Enter correct username.', 400),
    ('user3@user', 'user3', 1234567890, '1234567', 'password must be string. Enter correct password.', 400),
    ('user3@user', 'user3', '1234567890', 1243545435, 'password2 must be string. Enter correct password2.', 400),
    ('user3@user', 'user3', '1234567890', '1234567890', 'Update successful', 200)]

data_patch_user = [
    ('user1@user', 'user1', '1234567890', '1234567890', 'User with this email is already exist', 400),
    ('user21@user', 'user1', '1234567890', '1234567890', 'User with this username is already exist', 400),
    ('user', 'user21', '1234567890', '1234567890', 'email should be longer than 5 characters', 400),
    ('user21@user', 'use', '1234567890', '1234567890', 'username should be longer than 4 characters', 400),
    ('user21@user', 'user21', '1234567', '1234567', 'password should be longer than 8 characters', 400),
    ('user21@user', 'user21', '1234567890', '1234567', 'password is not curable', 400),
    (12425435, 'user21', '1234567890', '1234567890', 'email must be string. Enter correct email.', 400),
    ('user21@user', 1241352, '1234567890', '1234567', 'username must be string. Enter correct username.', 400),
    ('user21@user', 'user21', 1234567890, '1234567', 'password must be string. Enter correct password.', 400),
    ('user21@user', 'user21', '1234567890', 1243545435, 'password2 must be string. Enter correct password2.', 400),
    ('user21@user', 'user21', '1234567890', '1234567890', 'Update successful', 200)]

data_delete_user = [
    (2, 'User delete', 200),
    (10, 'User not found', 404)]

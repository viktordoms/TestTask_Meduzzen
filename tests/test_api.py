import requests
from jsonschema import validate
import pytest

from src.schemas.user import USER_SCHEMA


BASE_URL = "http://172.22.0.3:8005"



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


@pytest.mark.parametrize('email, username, password, password2, response_message, status_code', data_create_user)
def test_create_user(email, username, password, password2, response_message, status_code):
    data = {
        "email": email,
        "password": password,
        "password2": password2,
        "username": username
    }
    response = requests.post(BASE_URL + '/user', json=data)
    assert response.status_code == status_code, 'Received status code is not equal to expected'
    assert response.json()['response'] == response_message


def test_get_all():
    response = requests.get(BASE_URL + '/user_list')
    response_data = response.json()

    assert response.status_code == 200, 'Received status code is not equal to expected'
    if isinstance(response_data, dict):
        assert response.status_code == 404
        assert response.json()['response'] == 'Database is empty'
    else:
        assert response.status_code == 200
        validate(response.json()[0], USER_SCHEMA)


def test_get_user_by_id():

    response = requests.get(BASE_URL + '/user/1')
    response_data = response.json()

    if isinstance(response_data, dict):
        assert response.status_code == 404
        assert response.json()['response'] == 'User not found'
    else:
        assert response.status_code == 200
        validate(response.json()[0], USER_SCHEMA)


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


@pytest.mark.parametrize('email, username, password, password2, response_message, status_code', data_put_user)
def test_put_user(email, username, password, password2, response_message, status_code):
    data = {
        "email": email,
        "password": password,
        "password2": password2,
        "username": username
    }
    response = requests.put(BASE_URL + '/user/2', json=data)
    assert response.status_code == status_code, 'Received status code is not equal to expected'
    assert response.json()['response'] == response_message


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


@pytest.mark.parametrize('email, username, password, password2, response_message, status_code', data_patch_user)
def test_patch_user(email, username, password, password2, response_message, status_code):
    data = {
        "email": email,
        "password": password,
        "password2": password2,
        "username": username
    }
    response = requests.put(BASE_URL + '/user/2', json=data)
    assert response.status_code == status_code, 'Received status code is not equal to expected'
    assert response.json()['response'] == response_message


data_delete_user = [
    (2, 'User delete', 200),
    (10, 'User not found', 404)]


@pytest.mark.parametrize('id, response_message, status_code', data_delete_user)
def test_delete_user_by_id(id, response_message, status_code):
    response = requests.delete(BASE_URL + f'/user/{id}')
    assert response.status_code == status_code, 'Received status code is not equal to expected'
    assert response.json()['response'] == response_message

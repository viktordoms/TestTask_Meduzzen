import requests
from jsonschema import validate
import pytest

from src.schemas.user import USER_SCHEMA
from tests.fixtures import data_create_user, data_put_user, data_delete_user, data_patch_user


BASE_URL = "http://172.22.0.3:8005"


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


@pytest.mark.parametrize('id, response_message, status_code', data_delete_user)
def test_delete_user_by_id(id, response_message, status_code):
    response = requests.delete(BASE_URL + f'/user/{id}')
    assert response.status_code == status_code, 'Received status code is not equal to expected'
    assert response.json()['response'] == response_message

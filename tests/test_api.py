import requests
from jsonschema import validate

from src.schemas.user import USER_SCHEMA

BASE_URL = 'http://172.22.0.3:8005'


def test_get_all():
    response = requests.get(BASE_URL + '/user_list')
    response_data = response.json()

    assert response.status_code == 200, 'Received status code is not equal to expected'
    if isinstance(response_data, str):
        assert response_data == 'Database is empty', "Received response is not equal to expected"
    else:
        assert len(response_data) >= 1, 'Received json is empty'
        for user in response_data:
            validate(user, USER_SCHEMA)


def test_get_user_by_id():
    response_1 = requests.get(BASE_URL + '/user/47')
    response_data = response_1.json()
    assert response_1.status_code == 200, 'Received status code is not equal to expected'
    for user in response_data:
        validate(user, USER_SCHEMA)

    response_2 = requests.get(BASE_URL + '/user/100000')
    assert response_2.status_code == 404, 'Received status code is not equal to expected'
    assert response_2.json()['response'] == 'User not found','Received status code is not equal to expected'


def test_create_user():

    user_data_2 = {
        "email": "user1@user",
        "password": "123456789",
        "password2": "123456789",
        "username": "user1"
    }
    response_2 = requests.post(BASE_URL + '/user', json=user_data_2)
    assert response_2.status_code == 400, 'Received status code is not equal to expected'
    assert response_2.json()['response'] == 'User with this email is already exist'

    user_data_3 = {
        "email": "user2@user",
        "password": "123456789",
        "password2": "123456789",
        "username": "user1"
    }
    response_3 = requests.post(BASE_URL + '/user', json=user_data_3)
    assert response_3.status_code == 400, 'Received status code is not equal to expected'
    assert response_3.json()['response'] == 'User with this username is already exist'

    user_data_4 = {
        "email": "use",
        "password": "123456789",
        "password2": "123456789",
        "username": "user2"
    }
    response_4 = requests.post(BASE_URL + '/user', json=user_data_4)
    assert response_4.status_code == 400, 'Received status code is not equal to expected'
    assert response_4.json()['response'] == 'Email should be longer than 5 characters'

    user_data_5 = {
        "email": "user2@user",
        "password": "123456789",
        "password2": "123456789",
        "username": "us"
    }
    response_5 = requests.post(BASE_URL + '/user', json=user_data_5)
    assert response_5.status_code == 400, 'Received status code is not equal to expected'
    assert response_5.json()['response'] == 'Username should be longer than 4 characters'

    user_data_6 = {
        "email": "user2@user",
        "password": "123456",
        "password2": "123456",
        "username": "user2"
    }
    response_6 = requests.post(BASE_URL + '/user', json=user_data_6)
    assert response_6.status_code == 400, 'Received status code is not equal to expected'
    assert response_6.json()['response'] == 'Password should be longer than 8 characters'

    user_data_7 = {
        "email": "user2@user",
        "password": "123456789",
        "password2": "123456",
        "username": "user2"
    }
    response_7 = requests.post(BASE_URL + '/user', json=user_data_7)
    assert response_7.status_code == 400, 'Received status code is not equal to expected'
    assert response_7.json()['response'] == 'Password is not curable'

    user_data_8 = {
        "email": 123421,
        "password": "123456789",
        "password2": "123456",
        "username": "user2"
    }
    response_8 = requests.post(BASE_URL + '/user', json=user_data_8)
    assert response_8.status_code == 400, 'Received status code is not equal to expected'
    assert response_8.json()['response'] == 'Email must be string. Enter correct email.'

    user_data_9 = {
        "email": "user2@user",
        "password": "123456789",
        "password2": "123456",
        "username": 234523
    }
    response_9 = requests.post(BASE_URL + '/user', json=user_data_9)
    assert response_9.status_code == 400, 'Received status code is not equal to expected'
    assert response_9.json()['response'] == 'Username must be string. Enter correct username.'

    user_data_1 = {
        "email": "user2@user",
        "password": "123456789",
        "password2": "123456789",
        "username": "user2"
    }
    response_1 = requests.post(BASE_URL + '/user', json=user_data_1)
    assert response_1.status_code == 201, 'Received status code is not equal to expected'
    assert response_1.json()['response'] == 'User add to database'


def test_patch_user():

    user_data_2 = {
        "email": "user2@user",
        "password": "123456789",
        "username": "user2"
    }
    response_2 = requests.patch(BASE_URL + '/user/48', json=user_data_2)
    assert response_2.status_code == 400, 'Received status code is not equal to expected'
    assert response_2.json()['response'] == 'User with this email is already exist'

    user_data_3 = {
        "email": "user3@user",
        "password": "123456789",
        "username": "user2"
    }
    response_3 = requests.patch(BASE_URL + '/user/48', json=user_data_3)
    assert response_3.status_code == 400, 'Received status code is not equal to expected'
    assert response_3.json()['response'] == 'User with this username is already exist'

    user_data_4 = {
        "email": "use",
        "password": "123456789",
        "username": "user3"
    }
    response_4 = requests.patch(BASE_URL + '/user/48', json=user_data_4)
    assert response_4.status_code == 400, 'Received status code is not equal to expected'
    assert response_4.json()['response'] == 'Email should be longer than 5 characters'

    user_data_5 = {
        "email": "user3@user",
        "password": "123456789",
        "username": "us"
    }
    response_5 = requests.patch(BASE_URL + '/user/48', json=user_data_5)
    assert response_5.status_code == 400, 'Received status code is not equal to expected'
    assert response_5.json()['response'] == 'Username should be longer than 4 characters'

    user_data_6 = {
        "email": "user3@user",
        "password": "123456",
        "username": "user3"
    }
    response_6 = requests.patch(BASE_URL + '/user/48', json=user_data_6)
    assert response_6.status_code == 400, 'Received status code is not equal to expected'
    assert response_6.json()['response'] == 'Password should be longer than 8 characters'

    response_7 = requests.patch(BASE_URL + '/user/1000', json=user_data_6)
    assert response_7.status_code == 404, 'Received status code is not equal to expected'
    assert response_7.json()['response'] == 'User not found'

    user_data_8 = {
        "email": 123421,
        "password": "123456789",
        "username": "user3"
    }
    response_8 = requests.patch(BASE_URL + '/user/48', json=user_data_8)
    assert response_8.status_code == 400, 'Received status code is not equal to expected'
    assert response_8.json()['response'] == 'Email must be string. Enter correct email.'

    user_data_9 = {
        "email": "user3@user",
        "password": "123456789",
        "username": 234523
    }
    response_9 = requests.patch(BASE_URL + '/user/48', json=user_data_9)
    assert response_9.status_code == 400, 'Received status code is not equal to expected'
    assert response_9.json()['response'] == 'Username must be string. Enter correct username.'

    user_data_1 = {
        "email": "user3@user",
        "password": "123456789",
        "username": "user3"
    }
    response_1 = requests.patch(BASE_URL + '/user/48', json=user_data_1)
    assert response_1.status_code == 200, 'Received status code is not equal to expected'
    assert response_1.json()['response'] == 'Update successful'


def test_put_user():

    user_data_2 = {
        "email": "user1@user",
        "password": "123456789",
        "username": "user1"
    }
    response_2 = requests.patch(BASE_URL + '/user/48', json=user_data_2)
    assert response_2.status_code == 400, 'Received status code is not equal to expected'
    assert response_2.json()['response'] == 'User with this email is already exist'

    user_data_3 = {
        "email": "user4@user",
        "password": "123456789",
        "username": "user1"
    }
    response_3 = requests.patch(BASE_URL + '/user/48', json=user_data_3)
    assert response_3.status_code == 400, 'Received status code is not equal to expected'
    assert response_3.json()['response'] == 'User with this username is already exist'

    user_data_4 = {
        "email": "use",
        "password": "123456789",
        "username": "user4"
    }
    response_4 = requests.patch(BASE_URL + '/user/48', json=user_data_4)
    assert response_4.status_code == 400, 'Received status code is not equal to expected'
    assert response_4.json()['response'] == 'Email should be longer than 5 characters'

    user_data_5 = {
        "email": "user4@user",
        "password": "123456789",
        "username": "us"
    }
    response_5 = requests.patch(BASE_URL + '/user/48', json=user_data_5)
    assert response_5.status_code == 400, 'Received status code is not equal to expected'
    assert response_5.json()['response'] == 'Username should be longer than 4 characters'

    user_data_6 = {
        "email": "user4@user",
        "password": "123456",
        "username": "user4"
    }
    response_6 = requests.patch(BASE_URL + '/user/48', json=user_data_6)
    assert response_6.status_code == 400, 'Received status code is not equal to expected'
    assert response_6.json()['response'] == 'Password should be longer than 8 characters'

    response_7 = requests.patch(BASE_URL + '/user/1000', json=user_data_6)
    assert response_7.status_code == 404, 'Received status code is not equal to expected'
    assert response_7.json()['response'] == 'User not found'

    user_data_8 = {
        "email": 123421,
        "password": "123456789",
        "username": "user4"
    }
    response_8 = requests.patch(BASE_URL + '/user/48', json=user_data_8)
    assert response_8.status_code == 400, 'Received status code is not equal to expected'
    assert response_8.json()['response'] == 'Email must be string. Enter correct email.'

    user_data_9 = {
        "email": "user4@user",
        "password": "123456789",
        "username": 234523
    }
    response_9 = requests.patch(BASE_URL + '/user/48', json=user_data_9)
    assert response_9.status_code == 400, 'Received status code is not equal to expected'
    assert response_9.json()['response'] == 'Username must be string. Enter correct username.'

    user_data_1 = {
        "email": "user4@user",
        "password": "123456789",
        "username": "user4"
    }
    response_1 = requests.patch(BASE_URL + '/user/48', json=user_data_1)
    assert response_1.status_code == 200, 'Received status code is not equal to expected'
    assert response_1.json()['response'] == 'Update successful'


def test_delete_user_by_id():
    response_1 = requests.delete(BASE_URL + '/user/49')
    assert response_1.status_code == 200, 'Received status code is not equal to expected'
    assert response_1.json()['response'] == 'User delete', 'Received status code is not equal to expected'

    response_2 = requests.get(BASE_URL + '/user/100000')
    assert response_2.status_code == 404, 'Received status code is not equal to expected'
    assert response_2.json()['response'] == 'User not found', 'Received status code is not equal to expected'

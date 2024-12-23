import pytest
from utils.apis import APIS

@pytest.fixture(scope = 'module')
def apis():
    return APIS()

def test_getuser_validation(apis):
    response = apis.get('users')
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_postuser_validation(apis,load_user_data):

    user_data = load_user_data["new_user"]
    response = apis.post('users',user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == 'Shubham'
    responseget = apis.get('users/10')
    print(responseget.json())
    assert responseget.status_code == 200
    assert responseget.json()['name'] == 'Clementina DuBuque'

def test_putuser_validation(apis,load_user_data):
    # user_data={
    #     "name":"Shubham shekhar",
    #     "username":"qa user",
    #     "email":"test@gmail.com"
    # }
    user_data= load_user_data["new_user2"]
    response = apis.put('users/1',user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == 'Shubham shekhar'

def test_deleteuser_validation(apis):
    response = apis.delete('users/1')
    print(response.json())
    assert response.status_code == 200

import configuration     # importa el archivo configuration.py
import requests          # importa request
import data

def post_new_user(body):                     #definicion de la funcion
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         headers=data.headers,
                         json=body)
                                               # cuerpo de la funcion con return , devolver y con get obtener

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()
print (response.status_code)
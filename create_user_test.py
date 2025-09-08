import sender_stand_request
import data

# Esta funcion cambia los valores en el parámetro "firstName"
def get_user_body(first_name):
    # El diccionario que contiene el cuerpconservar los datos del diccionariode origen para conservar los datos del diccionariode origen
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

# definicion de una prueba positiva

def positive_assert(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable "user_body"
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un nuevo usuario se guarda en la variable user_reponse
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken esta en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""

    # El resultado de la solicitud de recepcion de datos de la tabla "user_model" se guarda en la variabel "users_table_response"
    users_table_response = sender_stand_request.get_users_table()

    # El string que debe estar en el cuerpo de la respuesta para recibir daos de la tabla "users" se ve asi:
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    # Comprueba si el usuario o usuaria existe y es unico
    assert users_table_response.text.count(str_user) == 1

#Prueba 1 : Creacion de un nuevo usuario  usuaria
# El parámetro "firstName" contiene dos caracteres

def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

# El parámetro "firstName" contiene 15 caracteres
# Prueba 2 creacion de un nuevo usuario o usuario

def test_create_user_15_letter_in_first_name_post_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

# Declaracion de una funcion negativa

def negative_assert_symbol(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable "user_body"
    user_body = get_user_body(first_name)

    # Comprueba si la variable "response" almacena e resultado de la solicitud
    response = sender_stand_request.post_new_user(user_body)

    # Comprueba si la respuesta contiene el codigo  400
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve asi :
    assert response.json()["message"] == "Has introducido un nombre de usuario no válido. " \
                                         "El nombre solo puede contener letras del alfabeto latino, "\
                                         "la longitud debe ser de 2 a 15 caracteres."

# Prueba 3 Error
# El parametro "firstName" contiene un caracter

def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")

# Prueba 4 Error
# El parametro "firstName" contiene 16 caracteres

def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

# Prueba 5 Error
# El parametro "firstName" contiene palabras con espcacios

def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")

# Prueba 6 Error
# El parametro "fistrName tiene un caracter especial

def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"@%$\",")

# Prueba 7 Error
# El parametro "firstName" contiene un string de números

def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")


# Declaracion de funcion negativa pra pruebas 8 y 9
# La respuesta contiene el siguiente mesnsaje de error : "No se ha enviado todos los parametros requeridos"

def negative_assert_no_firstname(user_body):
    # Guarda el resultado de llamar a la funcion a la variable "response"
    response = sender_stand_request.post_new_user(user_body)

    # Comprueba si la respuesta contiene el codigo 400
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

    # Compurueba si el atributo "message" en el cupero de respuesta se ve asi:
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"


# Prueba 8 Error
# La solictud no contiene el parametro "firstName"

def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data"a la variable "user_body"
    # De lo contrario , se podria perder los datos del diccionario de origen.
    user_body = data.user_body.copy()
    # El parametro "firstNanme" se elimina de la solicitud
    user_body.pop("firstName")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)


# Pruba 9 Error
# El parametro "firstNAme" contiene un string vacio

def test_create_user_empty_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body("")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)


# Prueba 10 Error
# El tipo de parametro "firstName" es un número

def test_create_user_number_type_first_name_get_error_response():
    # El cuerpo de la solicitud actualoizada se guarda en la variable user_body
    user_body = get_user_body(12)
    # El resultado de la solicitud para crear un nuevo usuario se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)

    #Comprobar el codigo de estado de la respuesta
    assert response.status_code == 400


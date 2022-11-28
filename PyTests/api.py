import json
import requests
from settings import VALID_EMAIL, VALID_PASSWORD, VALID_EMAIL_1
password = VALID_PASSWORD
email = VALID_EMAIL_1
email_reg = VALID_EMAIL

class Pets:
    """ API библиотека к сайту Swagger http://34.141.58.52:8080/#/"""

    def __init__(self):
        # self.my_token = None
        self.base_url = 'http://34.141.58.52:8000/'

    def get_token(self) -> json:
        """Запрос на авторизацию"""
        data = {"email": email,
                "password": password}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        my_email = res.json()['email']
        return my_token, status, my_id, my_email

    def get_list_users(self) -> json:
        """Запрос на получение списка юзеров"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        amount = res.json
        return status, amount

    def post_pet(self) -> json:
        """Запрос на добавление нового питомца"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": 'Viola',
                "type": 'cat',
                "age": 4,
                "gender": 'Male',
                "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def post_pet_photo(self) -> json:
        """Запрос на добавление фото к питомцу"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        files = {'pic': ('что-угодно.jpg', open('photo_1/cat.jpg', 'rb'), 'image/jpg')}

        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        link = res.json()['link']
        return status, link

    def get_pet_id(self) -> json:
        """Запрос на получение информации о петомце через id"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        id_pet = res.json()['pet']['id']
        name_pet = res.json()['pet']['name']
        gender = res.json()['pet']['gender']
        owner_id = res.json()['pet']['owner_id']
        types = res.json()['pet']['type']
        return status, id_pet, name_pet, gender, owner_id, types

    def pet_add_like(self) -> json:
        """Запрос на добавление лайка питомцу"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": Pets().post_pet()[0]}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def delete_pet(self) -> json:
        """Запрос на удаление созданного ранее питомца"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status

    def post_registered(self) -> json:
        """Запрос на рег. пользователя"""
        data = {"email": email_reg,
                "password": password, "confirm_password": password}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        my_id = res.json()
        my_id = my_id.get('id')
        status = res.status_code
        print(my_id)
        return status, my_id

    def delete_users(self) -> json:
        """Запрос на удаление пользователя"""
        my_id = Pets().post_registered()[1]
        res = requests.delete(self.base_url + 'users', data=json.dumps(my_id))
        status = res.status_code
        return status

    def check_user(self) -> json:
        """Запрос для удостоверения что пользователь действительно удален"""
        data = {"email": email_reg,
                "password": password}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        status = res.status_code
        detail = res.json()['detail']
        return status, detail

    def post_pets(self) -> json:
        """Запрос показывающий всех питомцев пользователя"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "skip": 0,
            "num": 10,
            "type": "cat",
            "petName": None,
            "user_id": my_id
        }
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        lists = res.json()
        return status, lists

Pets().get_token()
Pets().get_list_users()
Pets().post_pet()
Pets().post_pet_photo()
Pets().get_pet_id()
Pets().pet_add_like()
Pets().delete_pet()
Pets().post_registered()
Pets().delete_users()
Pets().check_user()
Pets().post_pets()

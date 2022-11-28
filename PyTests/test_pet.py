import os.path
import pytest
import requests
from api import Pets


pets = Pets()


def test_get_token():
    token = pets.get_token()[0]
    status = pets.get_token()[1]
    assert status == 200
    assert token

def test_list_users():
    status = pets.get_list_users()[0]
    amount = pets.get_list_users()[1]
    assert status == 200
    assert amount


def test_post_pet():
    status = pets.post_pet()[1]
    pet_id = pets.post_pet()[0]
    assert status == 200
    assert pet_id


def test_post_pet_photo():
    link = pets.post_pet_photo()[1]
    status = pets.post_pet_photo()[0]
    assert status == 200
    assert link

@pytest.mark.xfail
def test_get_pet_id():
    status = pets.get_pet_id()[0]
    id_pet = pets.get_pet_id()[1]
    name_pet = pets.get_pet_id()[2]
    gender = pets.get_pet_id()[3]
    assert status == 200
    assert id_pet
    assert name_pet
    assert gender

def test_pet_add_like():
    status = pets.pet_add_like()[0]
    assert status ==200

def test_delete_pet():
    status = pets.delete_pet()[0]
    assert status == 200

def test_post_registered():
    status = pets.post_registered()[0]
    my_id = pets.post_registered()[1]
    assert status == 200
    assert my_id

def test_delete_users():
    status = pets.delete_users()[0]
    assert status == 200

def test_check_user():
    detail = pets.check_user()[1]
    status = pets.check_user()[0]
    assert status == 400
    assert detail =='Username is taken or pass issue'

def test_post_pets():
    status = pets.post_pets()[0]
    lists = pets.post_pets()[1]
    assert status == 200
    assert lists
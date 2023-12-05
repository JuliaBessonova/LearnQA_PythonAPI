import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from random import choice
from string import ascii_lowercase
import allure

@allure.epic("User creation cases")
class TestUserRegister(BaseCase):
    exclude_params = [
        ('password'),
        ('username'),
        ('firstName'),
        ('lastName'),
        ('email')
    ]

    @allure.description("This test creates user with valid data")
    def create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("This test tries to create a user with an email of the existing user")
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", \
            f"Unexpected response content {response.content}"


    @allure.description("This test tries to create user with invalid email format")
    def test_create_user_invalid_email(self):
        email = "invalid email"
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Invalid email format", \
            f"Unexpected response content {response.content}"

    @allure.description(f"This test tries to create user with missing arguments 'password', 'username', 'firstName', 'lastName' or 'email'")
    @pytest.mark.parametrize('condition', exclude_params)
    def test_create_user_with_missing_arguments(self, condition):
        email = self.prepare_registration_data()["email"]
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        data.pop(condition)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {condition}", \
            f"Unexpected response content {response.content}"

    @allure.description("This test tries to create user with too short username")
    def test_create_user_with_short_username(self):
        email = self.prepare_registration_data()["email"]
        data = {
            'password': '123',
            'username': 'l',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short", \
            f"Unexpected response content {response.content}"

    @allure.description("This test tries to create user with too long username")
    def test_create_user_with_long_username(self):
        email = self.prepare_registration_data()["email"]
        long_username = ''.join(choice(ascii_lowercase) for _ in range(251))
        data = {
            'password': '123',
            'username': long_username,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too long", \
            f"Unexpected response content {response.content}"
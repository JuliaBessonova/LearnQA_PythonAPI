from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic("User edit cases")
class TestUserEdit(BaseCase):
    @allure.description("This test successfully edits just created user")
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        firstName = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_name = 'Changed Name'
        response3 = MyRequests.put(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
                                 )

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Wrong name of the user after edit")

    @allure.description("This test tries to edit not authorised user")
    def test_change_not_authorised_user(self):
        # EDIT
        new_name = 'Changed Name'
        response = MyRequests.put("/user/2", data={"firstName": new_name})

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Auth token not supplied", f"Unexpected response content {response.content}"

    @allure.description("This test tries to edit user's data while being authorized with another one")
    def test_edit_another_user(self):
        # REGISTER USERS
        register_data_1 = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data_1)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email_1 = register_data_1["email"]
        password_1 = register_data_1["password"]

        register_data_2 = self.prepare_registration_data()
        response2 = MyRequests.post("/user/", data=register_data_2)

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        user_id_2 = self.get_json_value(response2, "id")

        # LOGIN
        login_data = {
            'email': email_1,
            'password': password_1
        }

        response3 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")

        # EDIT
        new_name = 'Changed Name'
        response4 = MyRequests.put(f"/user/{user_id_2}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
                                 )

        Assertions.assert_code_status(response4, 400)

    @allure.description("This test tries to edit user's email with an email of invalid format")
    def test_edit_user_with_invalid_email_format(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        firstName = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_email = 'emailwithoutat.com'
        response3 = MyRequests.put(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"email": new_email}
                                 )

        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode("utf-8") == "Invalid email format", f"Unexpected response content {response.content}"

    @allure.description("This test tries to edit user's name with too short value")
    def test_edit_username_with_short_name(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        firstName = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_name = 'l'
        response3 = MyRequests.put(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
                                 )

        Assertions.assert_code_status(response3, 400)
        Assertions.assert_json_value_by_name(response3, "error", "Too short value for field firstName",
                                             "Unexpected error")



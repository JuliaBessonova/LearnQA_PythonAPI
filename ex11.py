import requests

class TestCookieMethod:
    def test_check_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        cookie_name = "HomeWork"
        expected_cookie_value = "hw_value"

        response = requests.get(url)
        assert response.status_code == 200, "Wrong response code"

        cookie_dict = dict(response.cookies)
        print(cookie_dict)
        assert cookie_name in cookie_dict, f"There's no cookie {cookie_name} in the dictionary"

        actual_cookie_value = cookie_dict[cookie_name]
        assert actual_cookie_value == expected_cookie_value, "Actual cookie in the response is not correct"

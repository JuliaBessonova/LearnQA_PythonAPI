import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

print("Количество редиректов:", len(response.history))
print("Итоговый URL:", response.url)

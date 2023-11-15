import requests
import json
import time

res_1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
obj_1 = json.loads(str(res_1.text))

res_2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":obj_1["token"]})
obj_2 = json.loads(str(res_2.text))
assert obj_2["status"] == 'Job is NOT ready'

time.sleep(obj_1["seconds"])

res_3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":obj_1["token"]})
obj_3 = json.loads(str(res_3.text))
assert obj_3["status"] == 'Job is ready'
print(obj_3["result"])

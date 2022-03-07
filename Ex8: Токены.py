# 1) создавал задачу
# 2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
# 3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
# 4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result

import requests, json, time

create_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token = json.loads(create_task.text)["token"]
seconds = json.loads(create_task.text)["seconds"]
response_StatusNotReady = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":f"{token}"})
status_response_NotReady = json.loads(response_StatusNotReady.text)["status"]
if status_response_NotReady == "Job is NOT ready":
    print (f"Получен корректный статус ДО того, как задача готова - статус '{status_response_NotReady}'")
else:
    print("Получен некорректный статус ДО того, как задача готова")
print (f"Ожидайте {seconds} секунд(ы), запрос обрабатывается")
time.sleep(seconds)
response_StatusReady = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":f"{token}"})
status_response_Ready = json.loads(response_StatusReady.text)["status"]
status_response_Result = json.loads(response_StatusReady.text)["result"]
if status_response_Ready == "Job is ready" and status_response_Result != '':
    print (f"Получен корректный статус и есть поле 'result' ПОСЛЕ того, как задача готова - статус '{status_response_Ready}'")
else:
    print("Получен некорректный статус или отсутствует поле result ПОСЛЕ того, как задача готова")




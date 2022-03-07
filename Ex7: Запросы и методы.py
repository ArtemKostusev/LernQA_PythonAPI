import requests

response_get = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print(response_get.text)
response_delete = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"DELETE"})
print(response_delete.text)
response_post = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"POST"})
print(response_post.text)
response_put = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"PUT"})
print(response_put.text)

#1
response_1_1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={})
print(response_1_1.text)
print(response_1_1.status_code)
response_1_2 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response_1_2.text)
print(response_1_2.status_code)
#Сервер корректно обрабатывает запрос, при этом получаем ошибку,что предоставлен неверный метод

#2
response_2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"HEAD"})
print(response_2.text)
print(response_2.status_code)
#Сервер не смог понять запрос и для данной ошибки отсутсвует обработка, поэтому отображается пустая строка

#3
response_3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print(response_3.text)
print(response_3.status_code)
#Сервер успешно обрабатывает запрос и отдает параметр success со значением !

#4
parameters_methods_list = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]


for param in parameters_methods_list:
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"Метод GET c параметром = {param} имеет статус код {response.status_code} и ответ {response.text}")
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"Метод GET c data = {param} имеет статус код {response.status_code} и ответ {response.text}")
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"Метод POST c data = {param} имеет статус код {response.status_code} и ответ {response.text}")
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"Метод POST c параметром = {param} имеет статус код {response.status_code} и ответ {response.text}")
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"Метод PUT c data = {param} имеет статус код {response.status_code} и ответ {response.text}")
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"Метод PUT c параметром = {param} имеет статус код {response.status_code} и ответ {response.text}")
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=param)
        print(f"Метод DELETE c data = {param} имеет статус код {response.status_code} и ответ {response.text}")
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", params=param)
        print(f"Метод DELETE c параметром = {param} имеет статус код {response.status_code} и ответ {response.text}")

# Метод DELETE c data = {'method': 'GET'} имеет статус код 200 и ответ {"success":"!"}
# Метод DELETE c параметром = {'method': 'GET'} имеет статус код 200 и ответ {"success":"!"}
# Метод POST c параметром = {'method': 'POST'} имеет статус код 200 и ответ {"success":"!"}
# Метод PUT c параметром = {'method': 'PUT'} имеет статус код 200 и ответ {"success":"!"}
# Метод DELETE c параметром = {'method': 'DELETE'} имеет статус код 200 и ответ {"success":"!"}





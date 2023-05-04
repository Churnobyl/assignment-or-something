# 선발대 4주차!!
import requests

data = {'title': 'homework', 'body' : 'sungchulmin', 'userId':1}
response = requests.post('https://jsonplaceholder.typicode.com/posts', data=data)

response_json = response.json()
title = response_json['title']
body = response_json['body']
userId = response_json['userId']
id_ = response_json['id']

with open('result.txt', 'w', encoding='utf-8') as result:
    result.write(f'title: {title}\n')
    result.write(f'body: {body}\n')
    result.write(f'userId: {userId}\n')
    result.write(f'id: {str(id_)}\n')
    

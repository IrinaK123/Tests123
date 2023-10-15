import requests

url = 'https://jsonplaceholder.typicode.com/posts/1' 
data = {'title': 'Updated Post', 'body': 'This is the updated body'}

response = requests.put(url, json=data)

if response.status_code == 200:
   updated_post = response.json()
   print('PUT Request Response:')
   print(updated_post)
else:
   print(f'Error: {response.status_code}')

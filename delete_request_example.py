import requests

url = 'https://jsonplaceholder.typicode.com/posts/1' 

response = requests.delete(url)

if response.status_code == 200:
   print('DELETE Request Successful')
else:
   print(f'Error: {response.status_code}')

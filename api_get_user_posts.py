import requests

user_id = 5
url = f'https://jsonplaceholder.typicode.com/posts?userId={user_id}'

response = requests.get(url)

if response.status_code == 200:
    user_posts = response.json()
    for post in user_posts:
        print(post)
else:
    print(f"Failed to retrieve posts. Status code: {response.status_code}")

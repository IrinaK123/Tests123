import requests

user_id = 3
url = f'https://jsonplaceholder.typicode.com/users/{user_id}'

response = requests.get(url)

if response.status_code == 200:
    user = response.json()
    geo = user.get('address', {}).get('geo',{})
    latitude = geo.get('lat')
    longtitude = geo.get('lng')
    
    if latitude is not None and longtitude is not None:
        print(f"Users {user_id}'s geo coordinates are:\n Latitude: {latitude},\n Longtitude: {longtitude}")
    else:
        print(f"Geo coordinates not found for user {user_id}.")
else:
    print(f"Failed to retrieve user {user_id}. Status code: {response.status.code}")

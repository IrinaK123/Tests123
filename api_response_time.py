import requests
import time

url = 'https://jsonplaceholder.typicode.com/photos'

start_time = time.time()

response = requests.get(url)

end_time = time.time()

if response.status_code == 200:
    response_time = end_time - start_time
    print(f"Response time for {url}: {response_time:.3f} seconds") #:.3f the value being formatted is a floating-point number (a decimal number)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

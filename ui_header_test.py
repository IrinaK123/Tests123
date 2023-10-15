import requests

url = 'https://play1.automationcamp.ir/'

response = requests.get(url)                              # Sending get request

if response.status_code == 200:                            # check if it is OK
    content_type = response.headers.get('content-type')     # getting the header text from the response
    
    if 'text/html' in content_type:                  # Checking if it contains needed substring
        print("The header contains 'text/html'.")
    else:
        print("The header doesn't contain 'text/html'.")
else:
    print(f"Error. Status code: {response.status_code}")

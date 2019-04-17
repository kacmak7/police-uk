import requests
import time

while True:
    time.sleep(2)
    
    url = 'http://localhost:5000'
    try: 
        response = requests.get(url+'/version')
        print(response.text)
    except:
        print('no service :(')

import requests
import keys
import time

TOKEN = keys.TOKEN
base_url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

chat_ids = ['-2481531999']

parameters = {'chat_id': chat_ids[0], 'text': 'Assalomu alaykum bugun 3.09.2024'}

response = requests.get(base_url, data=parameters)
print(response.text)

# Ko'p habar bir vaqtda yuborish
texts = ['Assalomu alaykum',
         'Bugun osmon ochiq boladi',
         'harorat 35 gradus issiq bolishi kutilmoqda',
         'kun davomida koproq suv iching'
         ]
for text in texts:
    time.sleep(5)
    parameters['text'] = text
    parameters['chat_id'] = chat_ids[1]
    response = requests.get(base_url, data=parameters)
    print(response.text)

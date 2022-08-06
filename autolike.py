import json
import os
import time

import requests
from dotenv import load_dotenv

from chinder.api import ChinderClient


def backup_image(url: str, user_id: str) -> None:
    dir = './.backup'
    if not os.path.exists(dir):
        os.makedirs(dir)
    
    try:
        r = requests.get(url)
        file_name = f'{dir}/{user_id}.jpg'
        with open(file_name, 'wb') as f:
            f.write(r.content)
    except requests.exceptions.RequestException:
        print('could not backup image')
    

if __name__ == '__main__':
    load_dotenv()
    X_AUTH_TOKEN: str = os.environ['X_AUTH_TOKEN']

    chinder = ChinderClient(X_AUTH_TOKEN)

    while(1):
        user_list:dict = json.loads(chinder.get_user_list().text)

        for user in user_list['data']['results']:
            user_id: str = user['user']['_id']
            user_name: str = user['user']['name']
            user_photo: str = user['user']['photos'][0]['url']
            
            backup_image(user_photo, user_id)
            chinder.like(user_id)
            print(user_name + '...Done!')

            time.sleep(2)

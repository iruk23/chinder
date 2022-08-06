from typing import Optional

import requests


class ChinderClient:
    def __init__(self, authToken: str) -> None:
        self.headers = {
            "tinder_version": "3.39.0",
            "app-version": "1033900",
            "platform": "web",
            "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15",
            "Accept": "application/json",
            "content-type": "application/json",
            "X-Auth-Token": authToken
        }
        self.host = 'https://api.gotinder.com'
    

    def get_user_list(self) -> Optional[requests.Response]:
        try:
            url = self.host + '/v2/recs/core?locale=ja'
            return requests.get(url, headers=self.headers)
        except requests.exceptions.RequestException as e:
            print('[ERROR] Could not get user list')
            return None


    def like(self, user_id: str) -> None:
        try:
            url = self.host + '/like/' + user_id + '?locale=ja'
            requests.get(url, headers=self.headers)
        except requests.exceptions.RequestException as e:
            print('[ERROR] Could not like:', e)

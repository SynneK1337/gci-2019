#!/bin/env python
import requests


class Codeforces():
    def __init__(self):
        self._url = "https://codeforces.com/api/{}"
        self._session = requests.Session()

    def get_user_info(self, handle):
        request = self._session.get(self._url.format('user.info'), params={'handles': handle})
        if request.status_code == 200:
            return request.json()['result'][0]
        else:
            return f"[-] User {handle} not found."


if __name__ == "__main__":
    c = Codeforces()
    handle = input("Enter your nickname: ")
    user = c.get_user_info(handle)
    if type(user) == str:
        print(user)
    else:
        print(f"Current Rating: {user['rating']}")
        print(f"Rank: {user['rank']}")
        print(f"Max Rating: {user['maxRating']}")
        print(f"Max Rank: {user['maxRank']}")
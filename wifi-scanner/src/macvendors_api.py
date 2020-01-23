import requests
import os.path

class MacVendors():
    def __init__(self):
        self._session = requests.Session()
        self._base_url = "https://api.macvendors.com/"
    def get_vendor(self, mac_address):
        url = os.path.join(self._base_url, mac_address)
        response = self._session.get(url)
        return response.text
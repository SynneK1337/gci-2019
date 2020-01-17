import requests
from bs4 import BeautifulSoup
from os import path


class ViewDNS():
    def __init__(self):
        self._base_url = "https://viewdns.info/"
        self._session = requests.Session()

    def reverse_whois(self, query):
        args = {
            'q': query
        }
        html = self._session.get(path.join(self._base_url, "reversewhois"), headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}, params=args).text
        soup = BeautifulSoup(html, 'lxml')
        table_body = soup.find('table', attrs={'border': '1'})
        rows = table_body.find_all('tr')
        domains = []
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            domains.append(cols)
        return domains
        

if __name__ == "__main__":
    v = ViewDNS()
    domains = v.reverse_whois(input("[?] Enter registrant name: "))
    for domain in domains:
        print('\t'.join(domain))
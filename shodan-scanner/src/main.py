from shodan import Shodan
from pprint import pprint
import requests

# Init the Shodan API Wrapper
SHODAN_API_KEY = "pdOhjFAFFeod0qLOYnJekbRTAbfAqyF9"
shodan = Shodan(SHODAN_API_KEY)


def get_ip():
    r = requests.get('http://ifconfig.co/json')
    return r.json()


def print_search_results(query):
    response = shodan.search(query)
    print(f"""
[i] Total results: {response['total']}
IP Address\tPort\tOperating System\tHostname
--------------------------------------------------------
    """)

    for host in response['matches']:
        if (hostname := host['hostnames']):
            hostname = hostname[0]
        else:
            hostname = ''
        print(f"{host['ip_str']}\t{host['port']}\t{host['os']}\t\t\t{hostname}")


def print_scan_results(host):
    response = shodan.host(host)
    print(f"""
Country:\t{response['country_name']}
Hostnames:\t{response['hostnames']}
City:\t{response['city']}
OS:\t{response['os']}
Ports:\t{response['ports']}
    """)
    for service in response['data']:
        print(f"Service {response['data'].index(service)}")
        pprint(service)

if __name__ == "__main__":
    while 1:
        print("""
[1] Get your IP Address
[2] Search for host
[3] Scan specific IP Address
[4] Exit
        """)
        choice = int(input("[?] Choice: "))
        print('\n')
        if choice == 1:
            ip = get_ip()
            print(f"""
IP Address:\t{ip['ip']}
Country:\t{ip['country']}
City:\t\t{ip['city']}
Hostname:\t{ip['hostname']}
ISP:\t\t{ip['asn_org']}
            """)

        elif choice == 2:
            query = input("[?] Query: ")
            print_search_results(query)

        elif choice == 3:
            host = input("[?] IP Address: ")
            print_scan_results(host)

        elif choice == 4:
            break

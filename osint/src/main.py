def print_weleakinfo_results(username, email, password, hash_, ip, name, phone, domain):
    from weleakinfo import WeLeakInfo
    w = WeLeakInfo('d717fc9054d16463181aaec41bd5598104aaa5ab')
    if username:
        response = w.public('username', username)
        if response['Total'] != 0:
            print(f"[WeLeakInfo] Username found in {response['Total']} results in {response['unique']} websites:")
            for breach in response['Data']:
                print(f"[WeLeakInfo] {breach}")
        else:
            print("[WeLeakInfo] Username not found :/")
    if email:
        response = w.public('email', email)
        if response['Total'] != 0:
            print(f"[WeLeakInfo] E-Mail found in {response['Total']} results in {response['unique']} websites:")
            for breach in response['Data']:
                print(f"[WeLeakInfo] {breach}")
        else:
            print("[WeLeakInfo] E-Mail address not found :/")
    if password:
        response = w.public('password', password)
        if response['Total'] != 0:
            print(f"[WeLeakInfo] Password found in {response['Total']} results in {response['unique']} websites:")
            for breach in response['Data']:
                print(f"[WeLeakInfo] {breach}")
        else:
            print("[WeLeakInfo] Password not found :/")
    if hash_:
        response = w.public('hash', hash_)
        if response['Total'] != 0:
            print(f"[WeLeakInfo] Hash found in {response['Total']} results in {response['unique']} websites:")
            for breach in response['Data']:
                print(f"[WeLeakInfo] {breach}")
        else:
            print("[WeLeakInfo] Hash not found :/")
    if ip:
        response = w.public('ip', ip)
        if response['Total'] != 0:
            print(f"[WeLeakInfo] IP Address found in {response['Total']} results in {response['unique']} websites:")
            for breach in response['Data']:
                print(f"[WeLeakInfo] {breach}")
        else:
            print("[WeLeakInfo] IP Address not found :/")
    if name:
            response = w.public('name', name)
            if response['Total'] != 0:
                print(f"[WeLeakInfo] Name found in {response['Total']} results in {response['unique']} websites:")
                for breach in response['Data']:
                    print(f"[WeLeakInfo] {breach}")
            else:
                print("[WeLeakInfo] Name not found :/")
    if phone:
        response = w.public('phone', phone)
        if response['Total'] != 0:
            print(f"[WeLeakInfo] Phone number found in {response['Total']} results in {response['unique']} websites:")
            for breach in response['Data']:
                print(f"[WeLeakInfo] {breach}")
        else:
            print("[WeLeakInfo] Phone number not found :/")
    if domain:
        response = w.public('domain', domain)
        if response['Total'] != 0:
            print(f"[WeLeakInfo] Domain found in {response['Total']} results in {response['unique']} websites:")
            for breach in response['Data']:
                print(f"[WeLeakInfo] {breach}")
    print("[WeLeakInfo] That' s all public data available. For more visit https://weleakinfo.com")


def check_instagram_existance(username):
    import requests
    if username:
        response = requests.get(f"https://instagram.com/{username}")
        return response.status_code != 404


def check_reddit_existance(username):
    import requests
    if username:
        response = requests.get(f"https://reddit.com/u/{username}")
        return response.status_code != 404


def main():
    print("Let' s provide some information, if unknown - leave empty.")
    username = input('[?] Username: ')
    email = input('[?] E-Mail address: ')
    password = input('[?] Password: ')
    hash_ = input('[?] Hash: ')
    ip = input('[?] IP Address: ')
    name = input('[?] Name: ')
    phone = input('[?] Phone number: ')
    domain = input('[?] Domain: ')
    print_weleakinfo_results(username, email, password, hash_, ip, name, phone, domain)
    if check_instagram_existance(username):
        print(f"[Instagram] {username} found.")
    else:
        print(f"[Instagram] {username} not found.")

    if check_reddit_existance(username):
        print(f"[Reddit] {username} found.")
    else:
        print(f"[Reddit] {username} not found.")


if __name__ == "__main__":
    main()
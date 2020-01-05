# This wrapper has implemented only functions I need for this task

import requests


class Github():
    def __init__(self):
        self.session = requests.Session()

    # Return list of repository objects from organization
    def get_organization_repos(self, organization_name):
        url = f'https://api.github.com/orgs/{organization_name}/repos'
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError


if __name__ == "__main__":
    g = Github()
    organization_name = input('[?] Organization name: ')
    try:
        repos = g.get_organization_repos(organization_name)
    except ValueError:
        print(f"[-] Organization called {organization_name} not found.")
    else:
        for repo in repos:
            print(f"{repo['name']}:\t {repo['forks']} forks")

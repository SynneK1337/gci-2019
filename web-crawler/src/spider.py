import requests
from bs4 import BeautifulSoup
import os.path


class Spider():
    def __init__(self, base_url):
        self._session = requests.Session()

        self._base_url = base_url
        if not self._base_url.startswith('http'):
            self._base_url = os.path.join('http://', self._base_url)
        if not self._base_url.endswith('/'):
            self._base_url += '/'
        self._previous_url = None
        self._current_url = self._base_url

        self._base_html = self.get_soup(self._base_url)
        self._previous_html = None
        self._current_html = self._base_html

    def get_soup(self, url):
        html = self._session.get(url).text
        return BeautifulSoup(html, 'lxml')

    def change_directory(self, path):
        self._previous_url, self._current_url = self._current_url, os.path.join(self._current_url, path)
        self._previous_html, self._current_html = self._current_html, self.get_soup(self._current_url)

    def go_back(self):
        self._previous_url, self._current_url = self._current_url, self._previous_url
        self._previous_html, self._current_html = self._current_html, self._previous_html

    def go_to_parent_directory(self):
        self._previous_url, self._current_url = self._current_url, os.path.dirname(self._current_url[:-1])+'/'
        self._previous_html, self._current_html = self._current_html, self.get_soup(self._current_url)

    def list_files(self):
        files = []
        if (h1 := self._current_html.h1):
            if h1.text.startswith("Index of"):
                for file in self._current_html.find_all('li'):
                    if (file := file.text[1:]) != "Parent Directory":
                        files.append(file)
        return files

    def list_files_recursive(self):
        # Up to three levels deep
        files = self.list_files()
        for file in self.list_files():
            if file.endswith('/'):
                self.change_directory(file)
                for file_ in self.list_files():
                    files.append(os.path.join(file, file_))
                    if file_.endswith('/'):
                        self.change_directory(file_)
                        for file__ in self.list_files():
                            files.append(os.path.join(file_, file__))
                            if file__.endswith('/'):
                                self.change_directory(file__)
                                for file___ in self.list_files():
                                    files.append(os.path.join(file__, file___))
                                self.go_to_parent_directory()
                        self.go_to_parent_directory()
                self.go_to_parent_directory()
        return files

    def list_directories(self):
        dirs = []
        files = self.list_files_recursive()
        for file in files:
            if file.endswith('/'):
                dirs.append(file)
        return dirs

    def get_index_files(self):
        index_files = []
        # Code below will find files like index.php only if interpreter is not available on server-side
        for file in self.list_files_recursive():
            if os.path.basename(file) == "index.php" or os.path.basename(file) == "default.asp":
                index_files.append(file)
        # Following code will find index files that are properly rendered by browser
        for directory in self.list_directories():
            self.change_directory(directory)
            if (h1 := self._current_html.h1):
                if not h1.text.startswith("Index of"):
                    index_files.append(directory)
            else:
                index_files.append(directory)
            self.go_to_parent_directory()
        return index_files


if __name__ == "__main__":
    s = Spider(input("[?] Enter URL (e.g. http://example.me): "))
    index_files = s.get_index_files()
    for file in index_files:
        print(f"[+] Index file found at: {file}")
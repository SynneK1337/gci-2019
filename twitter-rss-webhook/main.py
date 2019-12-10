import feedparser
from dataclasses import dataclass
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from sys import argv, exit
from time import sleep

@dataclass
class Article():
    title: str
    link:  str


class Twitter():
    class UserNotLoggedException(Exception):
        def __init__(self, expression, message):
            self.expression = expression
            self.message = "User is not logged in."

    def __init__(self):
        self._driver = webdriver.Chrome(executable_path="./chromedriver.exe")

    def login(self, login, password):
        self._driver.get("https://twitter.com/login")
        username_area = self._driver.find_element_by_xpath(
            '//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input')
        username_area.clear()
        username_area.send_keys(login)
        sleep(1)
        password_area = self._driver.find_element_by_xpath(
            '//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input')
        password_area.clear()
        password_area.send_keys(password)

        submit_btn = self._driver.find_element_by_xpath(
            '//*[@id="page-container"]/div/div[1]/form/div[2]/button')
        submit_btn.click()

    def is_logged(self):    
        self._driver.get("https://twitter.com")
        sleep(1)
        try:
            self._driver.find_element_by_xpath(
                '//*[contains(concat(" ", normalize-space(@class), " "), " logged-out")]')
        except NoSuchElementException:
            return False
        else:
            return True

    def postTweet(self, content):
        #if not self.is_logged():
        #    raise self.UserNotLoggedException
        self._driver.get("https://twitter.com")
        sleep(5)

        tweetBox = self._driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div')
        tweetBox.click()
        tweet_msg_field = self._driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_msg_field.send_keys(content)

        submit_btn = self._driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[3]')
        submit_btn.click()
        sleep(5)


class RSS():
    def __init__(self):
        self._feed = feedparser.parse("https://fedoramagazine.org/feed/")

    def read_latest_article_from_rss(self):
        latest_article = self._feed["entries"][0]
        return Article(latest_article["title"], latest_article["links"][0]["href"])


def main():
    if "-u" not in argv or "-p" not in argv:
        exit("usage: python main.py -u <username> -p <password>")

    username = argv[argv.index("-u")+1]
    password = argv[argv.index("-p")+1]

    rss = RSS()
    article = rss.read_latest_article_from_rss()
    content = '\n'.join([article.title, article.link])
    t = Twitter()
    t.login(username, password)

    t.postTweet(content)

if __name__ == "__main__":
    main()
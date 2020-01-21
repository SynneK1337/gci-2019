# Web-crawler
## Very simple web crawler that only looks for index files in directories

## Dependencies
- **[python](https://python.org/)>=3.8**
- [requests](https://requests.readthedocs.io/en/master/)
- [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/)
- [lxml](https://lxml.de/)

## Usage
- With pipenv: ```pipenv run src/spider.py```
- Without pipenv:
    - ```pip install -r requirements.txt```
    - ```python src/spider.py```

### There is example webserver to test this web-crawler with in ```Dockerfile```
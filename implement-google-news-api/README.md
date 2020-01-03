# Google News Reader
## How to host it?
```
docker build . -t google-news-reader
docker run -dit --name google-news-reader -p 8080:80 google-news-reader
```
Visit [https://localhost:8080](https://localhost:8080).
### Made by Emilian **SynneK1337** Zawrotny for Google Code-In 2019
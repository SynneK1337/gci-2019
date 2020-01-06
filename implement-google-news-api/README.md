# Google News Reader
## How to host it?
```
docker build . -t google-news-reader
docker run -dit --name google-news-reader -p 8080:80 google-news-reader
```
Visit [https://localhost:8080](https://localhost:8080).

## Demo
[YouTube](https://www.youtube.com/watch?v=wgZcFDD8q00)

## Known issues
- Thumbnails from some websites (e.g. TechChrunch) doesn't load if you hadn' t acceptet cookies policy on this site before.

### Made by Emilian **SynneK1337** Zawrotny for Google Code-In 2019
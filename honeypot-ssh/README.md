# Honeypot

## Dependencies
- [Docker](https://www.docker.com/)

## Deploy
```
docker build . -t honeypot
docker run -d --name honeypot -p 22:22 honeypot
```

## How can I browse log files?
```
docker exec -it honeypot /bin/bash
cat /var/log/.commands.log
```

### Made by Emilian **SynneK1337** Zawrotny for Google Code-In 2019 Challange
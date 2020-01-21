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

## How to prevent Directory Listing Vulnerability?
Directory Listing Vulnerability belongs to [Security Misconfiguration](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A6-Security_Misconfiguration) from OWASP list, so the vulnerability is
cause by wrong webserver configuration.

### How to configure apache2 correctly?
#### In Apache Virtual Host
```
<Directory /var/www/public_html>
      Options -Indexes
</Directory>
```
#### If you are not using Apache Virtual Host, you must edit your apache config file.
Config file is located in one of these locations:
- `/etc/apache2/httpd.conf`
- `/etc/apache2/apache2.conf`
- `/etc/httpd/httpd.conf`
- `/etc/httpd/conf/httpd.conf`

Locate the config file and open it and your favourite editor, then search for `<Directory *directory of your files here (e.g /var/www/html)">` 
Change line `Options Indexes FollowSymlinks` to `Options -Indexes`.

#### Then save the file, and restart your apache.

### How to configure nginx correctly?
nginx configuration file is located in one of these locations:
- `/usr/local/nginx/conf`
- `/etc/nginx`
- `/usr/local/etc/nginx`

Then search for **`autoindex`**, and set it to *`off`*.
Finally, the config file should look like:

```xml
...
server {
        listen   80;
        server_name  domain.com www.domain.com;
        access_log  /var/...........................;
        root   /path/to/root;
        location / {
                index  index.php index.html index.htm;
        }
        location /somedir {
               autoindex off;
        }
 }
 ...
 ```
#### Then save the file and restart nginx.

### Made by Emilian Zawrotny
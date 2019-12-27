# Introduction to systemd
### Creating a service, force it to start automatically and reload if crashed.

Sometimes it is useful to have app running all the time, auto-restarting if it crashes. The simplest way to achieve that is make systemd service with this app.

You probably used ```systemctl start ...``` or ```service ... start``` on your Linux Machine to run for example [apache](https://httpd.apache.org/) or [mysql](https://www.mysql.com/).
You can do the same with your own app, but as first, you have to write a unit file with service.
In this article, I will write service for [pynotes-server](https://github.com/synnek1337/pynotes-server) - a simple notes hosting server made by myself.

## How do I execute pynotes-server?
pynotes-server can be runned with ```python3 /usr/bin/pynotes-server/main.py```.

## How can I create systemd service file?
Systemd stores service unit files in ```/etc/systemd/system/``` directory.
### Let' s create file named `pynotes.service` inside `/etc/systemd/system` directory:
```
[Unit]
Description=Simple notes hosting solution
After=network.service   ; Because our script need internet connection to work properly

[Service]
Type=simple
User=synnek     ; Username you wanty to execute script with. Don' t use root if not needed.
ExecStart=/bin/python3 /usr/bin/pynotes-server/main.py  ; Command used to execution of the script

[Install]
WantedBy=multi-user.target
```

### Now, you can start your service:
```
systemctl start pynotes
```

### And if you want it to start automatically after boot up:
```
systemctl enable pynotes
```

## Improving this service
### You might noticed, that pynotes depends on [mysql](https://www.mysql.com/). In this case, we want our service to start after `mysqld.service`
Let' s change this in our file:
```
...
After=mysqld.service
...
```
Yay, now there won' t be a situation where our scripts is being executed while mysql is not running.

### But what if our service fails? Will systemd run it again?
By default - **not**. But we can change configuration of our service to force systemd to reload it after failure.

#### Within `[Service]` section:
If you want to always reload your service, even if it exits with success:
```
restart=always
```
If you want systemd to reload your service, only if **exitcode != 0**:
```
restart=on-failure
```

By default, systemd reloads service after **100ms** delay. You can easily change it:
```
RestartSec=1
```
With this line, systemd will reload the service after 1 second, instead of 100ms.

### By default, after 5 failed restart attempts within 10 seconds systemd stops trying to restart the service forever.
You can simply change that, by adding `StartLimitIntervalSec=0` within `[Unit]` section.

## Final `pynotes.service` file:
```
[Unit]
Description=Simple notes hosting solution
After=mysqld.service
StartLimitIntervalSec=0

[Service]
Type=simple
User=synnek     ; Username you wanty to execute script with. Don' t use root if not needed.
ExecStart=/bin/python3 /usr/bin/pynotes-server/main.py  ; Command used to execution of the script
Restart=always
RestartSec=1

[Install]
WantedBy=multi-user.target
```

## That' s all. It is pretty simple.
Systemd is default init in almost every **GNU/Linux** distribution nowadays. There are few exceptions like e.g:
- [Void Linux](https://voidlinux.org/)
- [Gentoo](https://gentoo.org/) - it can use systemd or openrc
- [Devuan](https://devuan.org/)

#### Made by Emilian `synnek1337` Zawrotny for Google Code-In 2019.
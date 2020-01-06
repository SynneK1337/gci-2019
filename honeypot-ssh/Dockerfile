FROM debian:stable
# Install OpenSSH Server
RUN apt update && apt install -y openssh-server

# Create few users to make it look like a real server
RUN useradd -ms /bin/bash john
RUN useradd -ms /bin/bash james
RUN useradd -ms /bin/bash michael
RUN useradd -ms /bin/bash oliver
RUN useradd -ms /bin/bash daniel
RUN useradd -ms /bin/bash zoe
RUN useradd -ms /bin/bash madison
RUN echo 'root:admin123' | chpasswd
RUN echo 'john:password123' | chpasswd
RUN echo 'james:j4m3s1994' | chpasswd
RUN echo 'michael:donaldtrump2016' | chpasswd
RUN echo 'oliver:p4ssw0rd' | chpasswd
RUN echo 'daniel:qwert123' | chpasswd
RUN echo 'zoe:123456' | chpasswd
RUN echo'madison:abcdefg1234567' | chpasswd

# Configure SSH Server
RUN mkdir /var/run/sshd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
RUN sed -i 's/#LogLevel INFO/LogLevel VERBOSE/g' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pan_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
EXPOSE 22

# Configure logging
RUN touch /var/log/.commands.log
RUN chmod 622 /var/log/.commands.log
COPY trap.txt /tmp/trap.txt
RUN cat /tmp/trap.txt >> /etc/profile
RUN rm /tmp/trap.txt

# Configure OS a bit, to make it look as a real server rather than honeypot
RUN apt install nano vim wget curl linux-image-amd64 xorg-server firefox chromium leafpad

CMD ["/usr/sbin/sshd", "-D", "-E", "/var/log/auth.log"]
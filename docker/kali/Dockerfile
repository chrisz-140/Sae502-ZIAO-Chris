FROM kalilinux/kali-rolling
ENV TZ=Europe/Paris \
    DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y nmap metasploit-framework hydra python3 tzdata
CMD ["tail", "-f", "/dev/null"]
RUN ln -fs /usr/share/zoneinfo/Europe/Paris /etc/localtime && dpkg-reconfigure --frontend noninteractive tzdata

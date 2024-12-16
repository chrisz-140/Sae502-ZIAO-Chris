FROM ubuntu:20.04
ENV TZ=Europe/Paris \
    DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y apache2 mysql-server tzdata
CMD ["tail", "-f", "/dev/null"]

FROM mongo:4.2-bionic
LABEL Name=mongo Version=1.0.0
ENV MYSQL_ROOT_PASSWORD=password
RUN apt-get -y update && apt-get install bash vim nano curl wget -y 
FROM ubuntu

RUN apt update
RUN apt install -y nginx

RUN rm -rf /var/www/html
RUN mkdir -p /var/www/html
COPY index.html /var/www/html/index.html

CMD nginx -g 'daemon off;'

EXPOSE 80

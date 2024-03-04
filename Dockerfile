FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    software-properties-common \
    nginx \
    python3.9 \
    python3-pip \
    python3-sphinx \
&& apt-get autoremove --purge \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

RUN rm -rf /usr/share/nginx/html/*

WORKDIR /usr/share/nginx

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY ./src/ ./src/

RUN pip3 install -r ./src/sections/notebooks/requirements.txt

ARG NOTION_KEY
ARG DEPLOY_URL

RUN jupyter-book build ./src

COPY nginx.conf /etc/nginx/sites-available/nginx.conf

RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/

ENTRYPOINT [ "nginx", "-g", "daemon off;" ]

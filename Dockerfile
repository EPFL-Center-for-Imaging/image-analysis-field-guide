FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    software-properties-common \
    nginx \
    python3.9 \
    python3-pip \
    python3-sphinx \
    # gcc \
    # g++ \
    # libeigen3-dev \
    # r-base \
    # r-cran-randomfields \
    # libicu-dev \
    # libgmp-dev \
    # libmpfr-dev \
    # libcgal-dev \
    # gmsh \
    # libfreetype6-dev \
    # libxml2-dev \
    # libxslt-dev \
&& apt-get autoremove --purge \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

RUN rm -rf /usr/share/nginx/html/*

WORKDIR /opt

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY ./src/ ./src/

ARG NOTION_KEY

RUN jupyter-book build ./src

# RUN cp -r ./src/_build/html /usr/share/nginx/

COPY nginx.conf /etc/nginx/sites-available/nginx.conf

RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/

ENTRYPOINT [ "nginx", "-g", "daemon off;" ]

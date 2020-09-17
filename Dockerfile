FROM python:3.6-alpine

WORKDIR /
ENV LD_LIBRARY_PATH /usr/lib:\$LD_LIBRARY_PATH
# 换源-阿里
# RUN mkdir -p ~/.pip/ \
# && echo '[global]\
# timeout = 6000\
# index-url = https://mirrors.aliyun.com/pypi/simple/\
# trusted-host = mirrors.aliyun.com'\
# > ~/.pip/pip.conf

ADD ta-lib-0.4.0-src.tar.gz .
# 安装环境依赖
RUN apk update; \
    apk add musl-dev wget git build-base; \
# Numpy
    pip install cython; \
    ln -s /usr/include/locale.h /usr/include/xlocale.h; \
    pip install numpy; \
# TA-Lib 
    cd ta-lib/; \
    ./configure --prefix=/usr; \
    make && make install; \
    pip install TA-Lib talib;\
    cd .. && rm -rf ta-lib;

RUN apk del musl-dev wget git build-base

WORKDIR /hfpy
COPY . .
COPY hfpy ./hfpy
COPY strategies ./strategies

RUN pip install --no-cache-dir -r ./requirements.txt

ENTRYPOINT [ "python", "main.py" ]

FROM python:3.6.12-slim

# ENV PYZMQ_VERSION="==16.0.2"
# ENV ZEROMQ_VERSION="4.2.2"

# 换源到ali
# RUN echo "deb http://mirrors.aliyun.com/debian/ buster main non-free contrib" > /etc/apt/sources.list; \
# echo "deb-src http://mirrors.aliyun.com/debian/ buster main non-free contrib" >> /etc/apt/sources.list; \
# echo "deb http://mirrors.aliyun.com/debian-security buster/updates main" >> /etc/apt/sources.list; \
# echo "deb-src http://mirrors.aliyun.com/debian-security buster/updates main" >> /etc/apt/sources.list; \
# echo "deb http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib" >> /etc/apt/sources.list; \
# echo "deb-src http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib" >> /etc/apt/sources.list; \
# echo "deb http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib" >> /etc/apt/sources.list; \
# echo "deb-src http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib" >> /etc/apt/sources.list;

RUN set -ex; \
 apt-get update; \
# 安装talib依赖
 apt-get install -y python3-dev libssl-dev libffi-dev build-essential libxml2-dev libxslt1-dev;
# openssh-client 支持 ssh scp
#  apt-get install -y --no-install-recommends wget openssh-client; \
#  # zmq
#  wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python; \
#  pip install pyzmq${PYZMQ_VERSION}; \
#  apt-get install -y --no-install-recommends libtool; \
#  apt-get install -y --no-install-recommends autoconf automake ca-certificates make; \

WORKDIR /
# ta-lib
ADD ta-lib-0.4.0-src.tar.gz .
RUN cd ta-lib/; \
 ./configure --prefix=/usr; \
 make && make install; \
# numpy 要先安装
 pip install --upgrade pip; \ 
 pip install --no-cache-dir numpy; \
# 支持将order写入pg
 pip install ta-lib pyyaml color_log psycopg2-binary redis sqlalchemy;

WORKDIR /hfpy
COPY hfpy ./hfpy/
COPY strategies/SMA* ./strategies/
COPY main.py .

ENV strategy_names SMACross

ENTRYPOINT [ "python", "main.py" ]

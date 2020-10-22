FROM python:3.6.12-slim

ENV PYZMQ_VERSION="==16.0.2"
ENV ZEROMQ_VERSION="4.2.2"

# 换源到ali
# RUN echo "deb http://mirrors.aliyun.com/debian/ buster main non-free contrib" > /etc/apt/sources.list; \
# echo "deb-src http://mirrors.aliyun.com/debian/ buster main non-free contrib" >> /etc/apt/sources.list; \
# echo "deb http://mirrors.aliyun.com/debian-security buster/updates main" >> /etc/apt/sources.list; \
# echo "deb-src http://mirrors.aliyun.com/debian-security buster/updates main" >> /etc/apt/sources.list; \
# echo "deb http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib" >> /etc/apt/sources.list; \
# echo "deb-src http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib" >> /etc/apt/sources.list; \
# echo "deb http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib" >> /etc/apt/sources.list; \
# echo "deb-src http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib" >> /etc/apt/sources.list;
# 本地包
#COPY zeromq-4.2.2.tar.gz /tmp

RUN set -ex; \
 apt-get update; \
 # openssh-client 支持 ssh scp
 apt-get install -y --no-install-recommends wget openssh-client; \
 # zmq
 wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python; \
 pip install pyzmq${PYZMQ_VERSION}; \
 apt-get install -y --no-install-recommends libtool; \
 apt-get install -y --no-install-recommends autoconf automake ca-certificates make; \
 cd /tmp && wget https://github.com/zeromq/libzmq/releases/download/v${ZEROMQ_VERSION}/zeromq-${ZEROMQ_VERSION}.tar.gz; \
 tar -xzf zeromq-${ZEROMQ_VERSION}.tar.gz; \
 cd zeromq-${ZEROMQ_VERSION}; \
 ./autogen.sh && ./configure && make && make install; \
 rm -rf /tmp/zeromq-${ZEROMQ_VERSION}* && rm -rf /tmp/*;

WORKDIR /
# ta-lib
ADD ta-lib-0.4.0-src.tar.gz .
RUN cd ta-lib/; \
 ./configure --prefix=/usr; \
 make && make install; \
# numpy 要先安装
 pip install --no-cache-dir numpy; \
 pip install ta-lib; \
 pip install pyyaml color_log py_ctp; \
# 支持将order写入pg
 pip install psycopg2-binary sqlalchemy;

WORKDIR /hfpy
COPY hfpy ./hfpy/
COPY strategies/SMA* ./strategies/
COPY strategies/Test* ./strategies/
COPY main.py .

ENTRYPOINT [ "python", "main.py" ]

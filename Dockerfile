FROM haifengat/centos:8.1

COPY requirements.txt /home/
RUN pip install -r /home/requirements.txt
# 先安装numpy再安装tulipy,否则报错
RUN yum install -y make gcc gcc-c++ python3-devel
RUN pip install tulipy
ADD ta-lib-0.4.0-src.tar.gz /
RUN cd /ta-lib && ./configure --prefix=/usr && make && make install && pip install TA-Lib && cd .. && rm -rf ta-lib
ENV LD_LIBRARY_PATH /usr/lib:$LD_LIBRARY_PATH
COPY hfpy /home/hfpy
COPY *.yml /home/
COPY strategies/SMA* /home/strategies/
COPY main.py /home/
WORKDIR /home/
ENTRYPOINT [ "python", "/home/main.py" ]

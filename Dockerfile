FROM haifengat/centos:8.1

COPY requirements.txt /home/
RUN pip install -r /home/requirements.txt
# 先安装numpy再安装tulipy,否则报错
RUN yum install -y make gcc gcc-c++ python3-devel
RUN pip install tulipy
COPY hfpy /home/hfpy
COPY *.yml /home/
COPY strategies/SMA* /home/strategies/
COPY main.py /home/
WORKDIR /home/
ENTRYPOINT [ "python", "/home/main.py" ]

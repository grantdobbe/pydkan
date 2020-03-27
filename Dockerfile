FROM python:3
ENV PYTHONUNBUFFERED 1
RUN DEBIAN_FRONTEND=noninteractive apt-get update && DEBIAN_FRONTEND=noninteractive apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN mkdir /opt/pydkan
WORKDIR /opt/pydkan
ADD requirements.txt /opt/pydkan/
RUN pip3 install -r requirements.txt
RUN pip3 install ipython
ENV PYTHONPATH=${PYTHONPATH:-/opt/pydkan/}

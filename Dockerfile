FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    wget \
    g++ \
    vim \
    git \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && ln -s /usr/bin/pip3 /usr/bin/pip \
    && export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib:/usr/bin/python \
    && export LANG=C.UTF-8 \
    && pip install --upgrade pip
    
WORKDIR /main_server
COPY . .
RUN pip3 install -r requirements.txt
RUN ["/bin/bash", "word_vector.sh"]
EXPOSE 3330
ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]
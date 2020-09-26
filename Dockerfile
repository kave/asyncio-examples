FROM python:3.7.4-stretch

WORKDIR /usr/src/app
COPY . ./

# System Prerequistes
RUN apt-get update

# System Depedencies
RUN apt-get install -y --no-install-recommends \
        gettext \
        vim \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Dependency Environment
RUN pip install pipenv
RUN pipenv install --system --deploy

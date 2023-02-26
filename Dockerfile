FROM golang:1.19-bullseye
ENV DEBIAN_FRONTEND noninteractive

# Install git
RUN apt-get update && apt-get install -y git wget

# Install Plex
RUN git clone https://github.com/labdao/plex
RUN cd plex && go build -o plex
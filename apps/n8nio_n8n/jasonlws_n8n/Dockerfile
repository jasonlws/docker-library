ARG IMAGE_NAME
ARG IMAGE_VERSION
FROM ${IMAGE_NAME}:${IMAGE_VERSION}

USER root

RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-requests \
    py3-pandas \
    py3-beautifulsoup4

USER node
ARG IMAGE_NAME
ARG IMAGE_VERSION
FROM ${IMAGE_NAME}:${IMAGE_VERSION}

USER root

# Create a config directory
RUN mkdir -p /usr/config
WORKDIR /usr/config

# Bundle config source
COPY ./setup.sql /usr/config/setup.sql
COPY ./entrypoint.sh /usr/config/entrypoint.sh
COPY ./configure-db.sh /usr/config/configure-db.sh

# Grant permissions for to our scripts to be executable
RUN chmod +x /usr/config/entrypoint.sh
RUN chmod +x /usr/config/configure-db.sh

ENTRYPOINT ["./entrypoint.sh"]
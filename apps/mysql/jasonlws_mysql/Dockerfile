ARG IMAGE_NAME
ARG IMAGE_VERSION
FROM ${IMAGE_NAME}:${IMAGE_VERSION}
ARG SETUP_SQL_PATH
COPY ./setup.sql /docker-entrypoint-initdb.d/setup.sql
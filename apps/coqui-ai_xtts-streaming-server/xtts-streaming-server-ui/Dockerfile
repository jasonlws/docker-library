FROM python:3.9.21

RUN mkdir -p /code
WORKDIR /code

COPY ./default_speaker.json /code/test/default_speaker.json
COPY ./demo.py /code/demo.py

RUN python -m pip install requests==2.31.0
RUN python -m pip install gradio==3.50.2

ENTRYPOINT ["python", "/code/demo.py"]
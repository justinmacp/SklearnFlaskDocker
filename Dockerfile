FROM ubuntu:latest

RUN apt-get update -y

RUN apt-get install -y python3-pip python3-dev build-essential

COPY . /docker

WORKDIR /docker

RUN pip3 install -r requirements.txt
RUN nuitka3 --show-progress --show-modules --follow-import-to=sptools --follow-import-to=raman_pipeline --follow-import-to=config --follow-import-to=routes --nofollow-imports app.py

ENTRYPOINT ["python3"]

CMD ["rest_api.py"]

USER docker
ENTRYPOINT ["dumb-init", "/docker/rest_api.bin"]
CMD []
FROM python:3.8.5
WORKDIR /code
COPY docker_entrypoint.sh .
COPY invite_users/requirements.txt .
RUN pip3 install -r requirements.txt
COPY /invite_users .

ENTRYPOINT ["./docker_entrypoint.sh"]

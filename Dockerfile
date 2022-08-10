FROM python:3.8.5
WORKDIR /code
COPY invite_users/requirements.txt .
RUN pip3 install -r requirements.txt
COPY /invite_users .

CMD ["./docker_entrypoint.sh"]
CMD [ "sh", "-c", "python3 manage.py runserver 0.0.0.0:8000"]

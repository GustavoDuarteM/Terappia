FROM tiangolo/uwsgi-nginx-flask

COPY manage.py /app
COPY config.py /app
COPY app.py /app
COPY requirements.txt /app
COPY ./scripts/manage.sh /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "bash" ]
CMD ["/app/manage.sh"]
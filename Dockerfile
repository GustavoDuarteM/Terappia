FROM tiangolo/uwsgi-nginx-flask

WORKDIR /app
ADD manage.py /app
ADD .env /app
ADD config.py /app
ADD app.py /app
ADD requirements.txt /app
ADD ./scripts/manage.sh /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "bash" ]
CMD ["/app/manage.sh"]
FROM python:3.11.8-slim
COPY ./loanflask/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./loanflask ./loanflask
COPY ./wsgi.py ./wsgi.py

CMD ["gunicorn", "--bind", "0.0.0.0:80", "wsgi:create_app('production')"]

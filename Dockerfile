FROM python:3.9.18-slim-bullseye

WORKDIR /app

COPY . app.py /app/
COPY templates/* /app/templates/

RUN pip install --no-cache-dir --upgrade pip==23.3 &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
FROM python:3.10
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY main.py /app/
CMD python -u main.py

FROM python:3.8

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py run.sh ./
RUN mkdir /data

ENV DATABASE="/data/bacon.db"
ENV HOST=0.0.0.0
ENV PORT=5000
EXPOSE 5000

CMD ["./run.sh"]

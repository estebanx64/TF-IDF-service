FROM python:3.8-buster

WORKDIR '/usr/app'

COPY requirements.txt ./

RUN pip install -r requirements.txt
RUN python -m nltk.downloader all

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]

# TF-IDF python API

## Technologies

- python
- FastAPI
- nltk
- BeautifulSoup
- Sklearn

## Instructions to run API

```bash
docker-compose up --build -d
```

It will take some minutes to build the image because i'm using nltk to tokenize the text and I need to download some stuffs for nltk.

## Request

```bash
curl "http://0.0.0.0:5000/v1/tfidf?url=https://stackoverflow.com&limit=10"

{"terms":[{"term":"policy","tf-idf":0.5801976932769258},{"term":"acknowledge","tf-idf":0.2900988466384629},{"term":"understand","tf-idf":0.2900988466384629},{"term":"privacy","tf-idf":0.2900988466384629},{"term":"cookie","tf-idf":0.2900988466384629},{"term":"terms","tf-idf":0.2900988466384629},{"term":"site","tf-idf":0.2526394575396835},{"term":"read","tf-idf":0.2526394575396835},{"term":"service","tf-idf":0.2526394575396835},{"term":"using","tf-idf":0.22606159800697195}]}% 
```

```bash
curl "http://0.0.0.0:5000/v1/tfidf?url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FTf-idf&limit=10"

{"terms":[{"term":"tfidf","tf-idf":0.41577743055963023},{"term":"frequency","tf-idf":0.29756935209157787},{"term":"reflect","tf-idf":0.2645667212297173},{"term":"statistic","tf-idf":0.2645667212297173},{"term":"numerical","tf-idf":0.2645667212297173},{"term":"important","tf-idf":0.2645667212297173},{"term":"short","tf-idf":0.2645667212297173},{"term":"intended","tf-idf":0.2645667212297173},{"term":"collection","tf-idf":0.23948630405379792},{"term":"document","tf-idf":0.23824048418760957}]}%
```

## Question

#### No need to actually implement this, just explain how you would do it. How would you design a system that, in addition to computing TF-IDF counts for the provided URL upon request, updates the IDF statistics whenever TF-IDF for a previously unseen URL is requested? How would you deploy this on AWS or GCP? 

- I will save all url requested in a database and I will save in a datalake in S3 (Wheter In the future we need to do some stuffs for ML, NLP whit the raw data)

- The urls that already exists in database we can response with the data saved in database, we can set a business rule.  For example, update the url requets in datababase if the last update was more than a week for the url requested
- To deploy database in AWS or GCP. I would use a database provided for AWS or GCP (Cloud spanner or RDS)
- If the app is only to do a TF-IDF compute statistics I would deploy using Lambda (AWS) or cloud run (GCP) .


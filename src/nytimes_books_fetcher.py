import pprint
import requests
import csv
import datetime
import smtplib
import json
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

BOOKS_URL = "https://api.nytimes.com/svc/books/v3/lists.json"
API_KEY = "csxxN2Hk41e8G3AKBLSjKHfWTvIVh8Rn"
EMAIL_RECIPIENTS = ['recipient1@gmail.com','recipient2@gmail.com']

def _mount_response(response):
    books = []
    for results in response['results']:
        for book_details in results['book_details']:
            dic = {}
            dic['title'] = book_details['title']
            dic['age_group'] = book_details['age_group']
            dic['deion'] = book_details['deion']
            dic['contributor'] = book_details['contributor']
            dic['author'] = book_details['author']
            dic['price'] = book_details['price']
            dic['publisher'] = book_details['publisher']
            dic['primary_isbn10'] = book_details['primary_isbn10']
            dic['primary_isbn13'] = book_details['primary_isbn13']
            dic['amazon_product_url'] = results['amazon_product_url']
            books.append(dic)
    return(books)

def _get_all_books():
    books = []
    books.extend(_get_books('combined-print-and-e-book-fiction'))
    books.extend(_get_books('combined-print-and-e-book-nonfiction'))
    return books

def _get_books(book_category):
    r = requests.get(BOOKS_URL, params = {'list': book_category, 'api-key': API_KEY})
    if (r.status_code == 200):
        results = r.json()
        books = _mount_response(results)
        return books

def _send_email(**kwargs):
    additional_email_recipients = kwargs['dag_run'].conf.get('additional_emails') 
    if additional_email_recipients:
        EMAIL_RECIPIENTS.extend(additional_email_recipients)
    books = kwargs['task_instance'].xcom_pull(task_ids='get_books')

    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    username = 'send.nyt.bestsellers@gmail.com'
    password = 'fnpwgzsahdjowlil'
    sender = 'send.nyt.bestsellers@gmail.com'
    targets = list(set(EMAIL_RECIPIENTS))

    msg = MIMEText(str(books)) 
    msg['Subject'] = 'The New York Times Best Sellers'
    msg['From'] = sender
    msg['To'] = ', '.join(targets)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    server.sendmail(sender, targets, msg.as_string())
    server.quit()

with DAG (
    dag_id='ny-times-books',
    schedule_interval="@daily",
    catchup=False,
    start_date=days_ago(1),
    tags=['ny-times'],
) as dag : 
    
    get_books = PythonOperator(
        task_id="get_books",
        python_callable=_get_all_books,
    )

    send_email = PythonOperator(
        task_id="send_email",
        python_callable=_send_email
    )
    
    get_books >> send_email

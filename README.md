# The New York Times - Best Sellers

## Context

The New York Times Best Sellers list is one of the most important lists in the book publishing industry. On one hand, knowing which books in a publisher’s catalog are being nominated on the list is important for the publisher to prioritize marketing resources. On the other hand, this list is an important source of understanding the social trending interests so that a publisher can identify if they have any books that have similar subjects/topics with a hope of promoting these books will receive good attention. 

<img width="770" alt="Screen Shot 2021-07-03 at 2 52 06 PM" src="https://user-images.githubusercontent.com/60671004/124364248-3d3d1c00-dc0e-11eb-8094-1fc2ee902b1c.png">

## Objective

Creating a airflow tag that will programmatically fetch the latest list of Combined Print & E-Book Fiction and Combined Print & E-Book Nonfiction through NYTimes Books API daily and send the results to some email recipients once every week or whenever the list gets updated.

## Instructions

### 1- Make sure you have Docker Compose installed in your machine.

#### Where to get Docker Compose
Windows and macOS
Docker Compose is included in Docker Desktop for Windows and macOS.

Linux
You can download Docker Compose binaries from the release page on this repository.

Using pip
If your platform is not supported, you can download Docker Compose using pip:

pip install docker-compose

### 2- Access the folder airflow-docker and do:
docker-compose up

Once all pods are healthy (check below), open a new tab in your browser and type the url localhost:8080/

<img width="1375" alt="Screen Shot 2021-07-03 at 4 07 17 PM" src="https://user-images.githubusercontent.com/60671004/124365846-bfcad900-dc18-11eb-9a14-3eb3cbdfe79b.png">


### Log in to the airflow UI

<img width="906" alt="Screen Shot 2021-07-03 at 3 49 30 PM" src="https://user-images.githubusercontent.com/60671004/124365465-4205ce00-dc16-11eb-92d8-d9b24d19bca0.png">

user: airflow
password: airflow

### DAG Tree View

<img width="143" alt="Screen Shot 2021-07-03 at 4 03 54 PM" src="https://user-images.githubusercontent.com/60671004/124365792-459a5480-dc18-11eb-89f2-a446dba0b8c1.png">


## Add-Ons

An admin can manually trigger the dag so additional recipients can receive the latest list by passing their email addresses through airflow dag configuration json.

## Future Developments

Send the results to some email recipients as attachments, so we can take advantage of other file formats, such as .csv and image files.



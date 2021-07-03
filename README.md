# The New York Times - Best Sellers

## Context

The New York Times Best Sellers list is one of the most important lists in the book publishing industry. On one hand, knowing which books in a publisher’s catalog are being nominated on the list is important for the publisher to prioritize marketing resources. On the other hand, this list is an important source of understanding the social trending interests so that a publisher can identify if they have any books that have similar subjects/topics with a hope of promoting these books will receive good attention. 

<img width="770" alt="Screen Shot 2021-07-03 at 2 52 06 PM" src="https://user-images.githubusercontent.com/60671004/124364248-3d3d1c00-dc0e-11eb-8094-1fc2ee902b1c.png">

## Objective

Creating a airflow tag that will programmatically fetch the latest list of Combined Print & E-Book Fiction and Combined Print & E-Book Nonfiction through NYTimes Books API daily and send the results to some email recipients once every week or whenever the list gets updated.

## Add-Ons

An admin can manually trigger the dag so additional recipients can receive the latest list by passing their email addresses through airflow dag configuration json.

## Future developments

Send the results to some email recipients as attachments, so we can take advantage of other file formats, such as .csv and image files.



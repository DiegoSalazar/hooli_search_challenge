# Hooli Search Challenge

This is my solution to the coding challenge detailed below.

## Challenge

```
Test for Backend engineer

Imagine that you work at Hooli. Gavin Belson has just marched into your office, referred to you as “Jared” and angrily demanded that you create a competitor to Google search. 
The first version of the prototype will take search queries from users and the number of pages that they want to see, direct those queries to Google and show users the results.

Note: we’ve decided to not implement pagination on our side for the time being. The reason is that Google blocks our requests, so we need to avoid making them too often. 

Please write the first version of a web application to solve this blocking problem.
The web service should contain two configurable options: 
Max number of requests to Google per second (default 5)
Max number of requests per 5 minutes (default 50)
The web page for users should contain:
Search query = QUERY
Number of pages from Google = N (up to 100 pages)
A search button
The web service should send N requests to Google (please use the URL "http://httpbin.org/delay/2" instead of “google.com”) per the limitations specified by the user.
When requests are completed, the web page should show the following message to the user: "Search completed. N pages found within X seconds."

Technical details:
The web service should be written in Python.
Your submission should contain a README which explains how to run the web service.
The code should include at least one unit test.
```

## Getting Started

Clone the repo

```
git clone https://github.com/DiegoSalazar/hooli_search_challenge
cd hooli_search_challenge
```

### Install Dependencies

```
sudo pip install -r requirements.txt
```

### Running the App

```
gunicorn main:app
```

The server should now be available at `http://localhost:8000/`.

## Running the tests

```
cd tests/
python -m unittest test_searcher
```

## Built With

* [Flask](http://flask.pocoo.org/) - Web
* [Bootstrap](http://getbootstrap.com/) - UI

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

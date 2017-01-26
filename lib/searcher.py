import os
import time
import requests

MAX_REQUESTS_PER_SECOND = os.getenv('MAX_REQUESTS_PER_SECOND', 5)
MAX_REQUESTS_PER_5_MINS = os.getenv('MAX_REQUESTS_PER_5_MINS', 50)
ONE_SECOND = 1
ONE_MINUTE = 60
FIVE_MINUTES = ONE_MINUTE * 5

class Searcher:
  def __init__(self, url):
    self.url = url

  def get_results(self, query, num_pages):
    self.results = []
    self.errors = []
    response = []
    numrequests = 0
    starttime = time.time()

    for _ in range(num_pages):
      elapsedtime = time.time() - starttime

      if elapsedtime >= ONE_SECOND and numrequests >= MAX_REQUESTS_PER_SECOND:
        time.sleep(ONE_SECOND)
      elif elapsedtime >= FIVE_MINUTES and numrequests >= MAX_REQUESTS_PER_5_MINS:
        time.sleep(ONE_MINUTE)

      response = requests.get(self.url + "?QUERY=" + query)
      numrequests += 1
      
      if response.status_code is 200:
        self.results.append(response.json())
      else:
        self.errors.append(response.text)

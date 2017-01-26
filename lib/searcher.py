import requests

class Searcher:
  def __init__(self, url):
    self.url = url
    self.errors = []
    self.results = []

  def get_results(self, query, num_pages):
    response = []

    for _ in range(num_pages):
      response = requests.get(self.url + "?QUERY=" + query)
      
      if response.status_code is 200:
        self.results.append(response.json())
      else:
        self.errors.append(response.text)

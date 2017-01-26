import os
import time
import pprint
import json
from flask import Flask
from flask import render_template
from flask import request
from lib.searcher import Searcher

app = Flask(__name__)

MAX_REQUESTS_PER_SECOND = os.getenv('MAX_REQUESTS_PER_SECOND', 5)
MAX_REQUESTS_PER_5_MINS = os.getenv('MAX_REQUESTS_PER_5_MINS', 50)

@app.route("/")
def search():
  return render_template('search.html')

@app.route("/search")
def results():
  query = request.args.get('QUERY', '')
  num_pages = request.args.get('N', '')

  t = time.time()
  searcher = Searcher('http://httpbin.org/delay/2')
  results = searcher.get_results(query, int(num_pages))
  elapsed_time = time.time() - t

  return render_template('results.html', query=query, num_pages=num_pages, elapsed_time=elapsed_time, searcher=searcher)

@app.context_processor
def prettify_json():
  def prettify(j):
    return json.dumps(j, sort_keys=True, indent=4, separators=(',', ': '))
  return dict(prettify=prettify)

if __name__ == "__main__":
  app.run()
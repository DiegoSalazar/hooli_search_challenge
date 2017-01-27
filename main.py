import os
import time
import pprint
import json
from flask import Flask
from flask import render_template
from flask import request
from lib.searcher import Searcher

app = Flask(__name__)
SEARCH_ENDPOINT = os.getenv('SEARCH_ENDPOINT', 'http://httpbin.org/delay/2')

@app.route("/")
def search():
  return render_template('search.html')

@app.route("/search")
def results():
  # Search query = QUERY
  query = request.args.get('QUERY', '')

  # Number of pages from Google = N (up to 100 pages)
  num_pages = int(str.strip(request.args.get('N', '1')) or 1)
  num_pages = 100 if num_pages > 100 else num_pages

  t = time.time()
  searcher = Searcher(SEARCH_ENDPOINT)
  searcher.get_results(query, num_pages)
  elapsed_time = time.time() - t

  return render_template('results.html', query=query, num_pages=num_pages, elapsed_time=elapsed_time, searcher=searcher)

@app.context_processor
def prettify_json():
  def prettify(j):
    return json.dumps(j, sort_keys=True, indent=4, separators=(',', ': '))
  return dict(prettify=prettify)

if __name__ == "__main__":
  app.run()
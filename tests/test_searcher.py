import unittest, os, sys
sys.path.append(os.path.abspath('..'))
from lib.searcher import Searcher

class TestSearcher(unittest.TestCase):
  def test_get_results_success_once(self):
    query = "apple"
    num_pages = 1
    searcher = Searcher('http://httpbin.org/delay/0')
    searcher.get_results(query, int(num_pages))
    self.assertFalse(searcher.errors)
    self.assertTrue(searcher.results is not None)
    self.assertEqual(len(searcher.results), 1)

  def test_get_results_n_times(self):
    query = "apple"
    num_pages = 2
    searcher = Searcher('http://httpbin.org/delay/0')
    searcher.get_results(query, int(num_pages))
    self.assertEqual(len(searcher.results), 2)

if __name__ == '__main__':
    unittest.main()
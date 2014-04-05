from helpers import *

import json
from itbit import Itbit

class ItbitTest(unittest.TestCase):

    def setUp(self):
        self.subject = Itbit()


    @httpretty.activate
    def test_should_get_ticker(self):
        mock_ticker()
        expected = json_fixture('ticker.json')
        self.assertEqual(expected, self.subject.ticker())


    @httpretty.activate
    def test_should_get_order_book(self):
        mock_order_book()
        expected = json_fixture('orderbook.json')
        self.assertEqual(expected, self.subject.order_book())


    @httpretty.activate
    def test_should_get_news(self):
        mock_news()
        expected = json_fixture('news.json')
        self.assertEqual(expected, self.subject.news())


    @httpretty.activate
    def test_should_get_market(self):
        mock_price_feed()
        expected = json_fixture('price_feed.json')
        self.assertEqual(expected, self.subject.price_feed())

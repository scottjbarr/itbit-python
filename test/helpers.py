import unittest
import httpretty
import json


def json_fixture(name):
    filename = 'test/docs/%s' % name
    return json.loads(open(filename, 'r').read())


def mock_ticker():
    url = "https://www.itbit.com/api/feeds/ticker/XBTUSD"
    httpretty.register_uri(httpretty.GET, url,
            body=open('test/docs/ticker.json', 'r').read(),
            status=200)


def mock_order_book():
    url = "https://www.itbit.com/api/feeds/orderbook/XBTUSD"
    httpretty.register_uri(httpretty.GET, url,
            body=open('test/docs/orderbook.json', 'r').read(),
            status=200)


def mock_news():
    url = "https://www.itbit.com/api/feeds/news/10"
    httpretty.register_uri(httpretty.GET, url,
            body=open('test/docs/news.json', 'r').read(),
            status=200)


def mock_price_feed():
    url = "https://www.itbit.com/api/feeds/market/XBTUSD"
    httpretty.register_uri(httpretty.GET, url,
            body=open('test/docs/price_feed.json', 'r').read(),
            status=200)

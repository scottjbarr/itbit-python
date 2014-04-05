import json
import requests

class Itbit(object):

    HOST = "https://www.itbit.com/api/feeds"


    def __init__(self, symbol='XBTUSD'):
        """
        Valid symbols : XBTUSD, XBTEUR, XBTSGD
        """
        self.symbol = symbol


    def ticker(self):
        return self._json('ticker/%s' % self.symbol)


    def price_feed(self):
        return self._json('market/%s' % self.symbol)


    def order_book(self):
        return self._json('orderbook/%s' % self.symbol)


    def news(self, max=10):
        return self._json('news/%i' % (max))


    def _url(self, resource):
        return "%s/%s" % (Itbit.HOST, resource)


    def _json(self, resource):
        print self._url(resource)
        return requests.get(self._url(resource)).json()

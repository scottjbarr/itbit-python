
import requests

class Itbit(object):

    HOST = "https://www.itbit.com/api/feeds"


    def __init__(self, symbol='XBTUSD'):
        self.symbol = symbol


    def url(self, resource):
        return "%s/%s" % (Itbit.HOST, resource)


    def json(self, resource):
        return requests.get(self.url(resource)).json()


    def ticker(self):
        return self.json('ticker/%s' % self.symbol)


    def order_book(self):
        return self.json('/orderbook/%s' % self.symbol)

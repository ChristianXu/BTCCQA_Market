#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'sara'

import comm.comm as comm
import random
import comm.btcc as btcc


class DepthMaker:

    def __init__(self, access, secret):

        self.highest_price = 0
        self.lowest_price = 0
        self.btc = btcc.BTCC(access, secret)

    #获取最新成交价格
    def get_last_price(self):
        response = comm.get_url_response("http://data.btcc.com/data/ticker")
        return response['ticker']['last']


    #获取当前成交的10个订单价格
    def set_10_price(self):
        response = comm.get_url_response("https://data.btcc.com/data/orderbook?market=cnybtc&limit=5&merge=0")

        # higher than last price
        asks = response['asks']

        self.highest_price = asks[0][0]

        # lower than last price
        bids = response['bids']

        self.lowest_price = bids[0][0]

    def make_random_price(self, count=1):
        '''
        生成随机价格
        :param count:
        :return:
        '''

        self.set_10_price()
        random_price_list = []

        while count > 0:
            random_price = random.uniform(self.highest_price+5, self.lowest_price-5)
            count -= 1
            random_price_list.append(round(random_price, 2))

        return random_price_list

    def make_depth(self, count=1):
        """
        下单
        :param count:
        :return:
        """
        price_list = self.make_random_price(count)
        last_price = self.get_last_price()
        for price in price_list:

            if float(price) > float(last_price):
                # pass
                self.btc.buy(price, 1)
            else:
                self.btc.sell(price, 1)


if __name__ =="__main__":
    a = DepthMaker("9d2372a8-14be-46d8-ac6f-466cd6faa29e", "e8a2b633-82fc-464f-94b2-c7639d64efbd")
    a.make_depth(3)

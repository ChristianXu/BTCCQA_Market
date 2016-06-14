#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'sara'

import comm.comm as cm


def get_orderbook_data(limit=None, symbol=None):
    """
    请求买卖订单默认提供市场上100条买单数据和100条卖单数据。
    可通过设置limit后的参数来获取指定数量的订单数据，通过symbol参数来指定要查询的符号。
    买单按照价格从高到低排序，卖单按照从低到高排序。
    :param:limit
    :param:symbol
    :return:
    """
    # 市场上买卖订单数据
    pro_orderbook_url = "https://pro-data.btcc.com/data/pro/orderbook"

    cls_dict = {}

    if limit is not None:
        cls_dict['limit'] = limit

    if symbol is not None:
        cls_dict['symbol'] = symbol

    url_cls = cm.make_url_cls(cls_dict)

    if url_cls != "":
        pro_orderbook_url += "?"+url_cls

    # print pro_orderbook_url

    response = cm.get_url_response(pro_orderbook_url)

    # print(response)
    return response


def get_ticker_data(symbol="XBTCNY"):
    """
    提供实时的最新行情,用symbol参数指定要查询的行情数据市场（XBTCNY、XBTUSD）
    默认返回是Pro XBTCNY市场的最新行情。
    :param symbol:
    :return:
    """
    # 最新行情数据
    pro_ticker_url = "https://pro-data.btcc.com/data/pro/ticker?symbol="+symbol

    response = cm.get_url_response(pro_ticker_url)

    return response


def get_historydata(since=None, limit=None, symbol="XBTCNY", sincetype=None):
    """
    获取Pro Exchange历史交易记录。可以通过设置symbol参数来获取XBTCNY和XBTUSD来获取两个市场的历史交易记录。
    :param symbol:
    :return:
    """
    # 交易历史
    pro_historydata_url = "https://pro-data.btcc.com/data/pro/historydata"

    cls_dict = {}

    if since is not None:
        cls_dict['since'] = since

    if limit is not None:
        cls_dict['limit'] = limit

    if symbol is not None:
        cls_dict['symbol'] = None

    if sincetype is not None:
        cls_dict['sincetype'] = sincetype

    url_cls = cm.make_url_cls(cls_dict)

    if url_cls != "":
        pro_historydata_url += "?"+url_cls

    response = cm.get_url_response(pro_historydata_url)

    return response


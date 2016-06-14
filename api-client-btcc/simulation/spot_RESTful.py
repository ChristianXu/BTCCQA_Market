#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'sara'

import comm.comm as cm


def get_ticker(market):
    """
    获取最新的行情数据
    :param market:
    :return:
    """
    spot_ticker_url = "https://data.btcchina.com/data/ticker?market="+market

    response = cm.get_url_response(spot_ticker_url)

    return response


def get_trade_data():
    """
    获取过去24小时内的交易历史,注意,为了保证服务质量和响应速度,返回的交易数量上限为10000个。
    :return:
    """
    spot_trade_data_url = "https://data.btcchina.com/data/trades"

    response = cm.get_url_response(spot_trade_data_url)

    return response


def get_trade_history_data(limit=None, since=None, sincetype=None):
    """
    获取交易历史的清单，
    可通过设置since后的参数来获取较早的历史记录，
    可通过设置limit后的参数来获取指定数量的历史纪录，limit的默认值是100，有效区间是[0,5000].
    可通过设置sincetype参数为“id”或者“time”来指定since后的参数作用在哪个数据上，默认sincetype为id。
    :param limit:
    :param since:
    :param sincetype:
    :return:
    """
    historydata_url = "https://data.btcchina.com/data/historydata "
    cls_dict = {}

    if since is not None:
        cls_dict['since'] = since

    if limit is not None:
        cls_dict['limit'] = limit

    if sincetype is not None:
        cls_dict['sincetype'] = sincetype

    url_cls = cm.make_url_cls(cls_dict)

    if url_cls != "":
        historydata_url += "?"+url_cls

    response = cm.get_url_response(historydata_url)

    return response


def get_orderbook(limit=None, market="btccny"):
    """
    订单数据默认包含所有公开的要价和出价。 可通过设置limit后的参数来获取指定数量的订单数据。
    :param limit:
    :param market:
    :return:
    """
    orderbool_url = "https://data.btcchina.com/data/orderbook"
    cls_dict = {}

    if limit is not None:
        cls_dict['limit'] = limit

    if market != "btccny":
        cls_dict['market'] = market

    url_cls = cm.make_url_cls(cls_dict)

    if url_cls != "":
        orderbool_url += "?"+url_cls

    response = cm.get_url_response(orderbool_url)

    return response
#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'sara'

import quickfix
import uuid
import fix.message.field_btcc as field_btcc


def get_uuid():
    return str(uuid.uuid1())


class AccountInfoRequest(quickfix.Message):
    """
    账户信息查询
    """

    def __init__(self, account_string, SubAccountInfoRequestType = '1'):
        quickfix.Message.__init__(self)
        self.msg_type = 'U1000'
        self.begin_string = "FIX.4.4"
        self.AccReqID = field_btcc.AccReqID(get_uuid())
        self.SubAccountInfoRequestType = field_btcc.SubAccountInfoRequestType(SubAccountInfoRequestType)
        self.account = quickfix.Account(account_string)
        self.set_request_field()

    def set_request_field(self):
        """
        设置字段
        :return:
        """
        self.getHeader().setField(quickfix.BeginString("FIX.4.4"))
        self.getHeader().setField(quickfix.MsgType(self.msg_type))
        self.setField(self.account)
        self.setField(self.AccReqID)
        self.setField(self.SubAccountInfoRequestType)


class NewOrderSingleRequest(quickfix.Message):
    """
    买卖订单请求
    """
    def __init__(self, account_string):
        quickfix.Message.__init__(self)
        self.msg_type = 'D'
        self.begin_string = "FIX.4.4"
        self.account = quickfix.Account(account_string)

    def buy_limit(self, order_qty, price, symbol="XBTCNY"):
        """
        购买限价单
        :param price: 价格
        :param symbol: 数量
        :return:
        """
        self.getHeader().setField(quickfix.BeginString("FIX.4.4"))
        self.getHeader().setField(quickfix.MsgType(self.msg_type))
        self.setField(self.account)
        # 用户自定义的请求唯一标识ID
        self.setField(quickfix.ClOrdID(get_uuid()))
        self.setField(quickfix.OrdType("2"))
        self.setField(quickfix.Side("1"))
        self.setField(quickfix.OrderQty(order_qty))
        self.setField(quickfix.Price(price))
        self.setField(quickfix.Symbol(symbol))
        self.setField(quickfix.TimeInForce("1"))
        self.setField(quickfix.TransactTime())

    def sell_limit(self, order_qty, price, symbol="XBTCNY"):
        """
        卖出限价单
        :param price: 价格
        :param symbol: 数量
        :return:
        """
        self.getHeader().setField(quickfix.BeginString("FIX.4.4"))
        self.getHeader().setField(quickfix.MsgType(self.msg_type))
        self.setField(self.account)
        # 用户自定义的请求唯一标识ID
        self.setField(quickfix.ClOrdID(get_uuid()))
        self.setField(quickfix.OrdType("2"))
        self.setField(quickfix.Side("2"))
        self.setField(quickfix.OrderQty(order_qty))
        self.setField(quickfix.Price(price))
        self.setField(quickfix.Symbol(symbol))
        self.setField(quickfix.TimeInForce("1"))
        self.setField(quickfix.TransactTime())

    def buy_market(self, order_qty, symbol="XBTCNY"):
        """
        购买市价单
        :param order_qty:
        :param symbol:
        :return:
        """
        self.getHeader().setField(quickfix.BeginString("FIX.4.4"))
        self.getHeader().setField(quickfix.MsgType(self.msg_type))
        # 用户自定义的请求唯一标识ID
        self.setField(quickfix.ClOrdID(get_uuid()))
        self.setField(quickfix.OrdType("1"))
        self.setField(quickfix.Side("1"))
        self.setField(quickfix.OrderQty(order_qty))
        self.setField(quickfix.Symbol(symbol))
        self.setField(quickfix.TransactTime())

    def sell_market(self, order_qty, symbol="XBTCNY"):
        """
        购买市价单
        :param order_qty:
        :param symbol:
        :return:
        """
        self.getHeader().setField(quickfix.BeginString("FIX.4.4"))
        self.getHeader().setField(quickfix.MsgType(self.msg_type))
        self.setField(self.account)
        # 用户自定义的请求唯一标识ID
        self.setField(quickfix.ClOrdID(get_uuid()))
        # order类型
        self.setField(quickfix.OrdType("1"))
        self.setField(quickfix.Side("2"))
        self.setField(quickfix.OrderQty(order_qty))
        self.setField(quickfix.Symbol(symbol))
        self.setField(quickfix.TransactTime())








# -*- coding: utf-8 -*-
__author__ = 'sara'

import quickfix


class AccReqID(quickfix.StringField):
	"""
	客户端请求的唯一标识ID
	"""
	def __init__(self, data = None):
		if data == None:
			quickfix.StringField.__init__(self, 8000)
		else:
			quickfix.StringField.__init__(self, 8000, data)


class SubAccountInfoRequestType(quickfix.CharField):
	"""
	是否使用推送功能
	"""
	def __init__(self, data = None):
		if data == None:
			quickfix.CharField.__init__(self, 9263)
		else:
			quickfix.CharField.__init__(self, 9263, data)

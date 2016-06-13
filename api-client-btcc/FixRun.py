#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'sara'

import os

import quickfix as quickfix

import comm.comm as comm
import fix.MyFixApplication as mfp
import fix.message.RequestMessage as rm


def run():
    """
    运行方法
    :return:
    """
    try:

        # request message
        request_messages = []
        # 配置文件
        file_name = os.path.join(comm.prj_dir, "config", "quickfix-client.properties")

        # 获取 access_key 和 secret_key
        users_dict = comm.get_xml()

        settings = quickfix.SessionSettings(file_name)

        application = mfp.MyFixApplication()

        store_factory = quickfix.FileStoreFactory(settings)

        log_factory = quickfix.FileLogFactory(settings)

        initiator = quickfix.SocketInitiator(application, store_factory, settings, log_factory)

        # initiator.start()
        for user in users_dict:

            account_string = comm.get_account_string(users_dict[user][0], users_dict[user][1])

            request = rm.NewOrderSingleRequest(account_string)
            request.buy_limit(float("1"), float("1"), symbol="XBTUSD")

            request_messages.append(request)

        application.run(request_messages)

        initiator.block()

        # initiator.stop()

    except quickfix.ConfigError:
        print("ConfigError")


run()

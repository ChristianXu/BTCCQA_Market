#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'sara'

import urllib
import json
from xml.etree import ElementTree as elementTree
import os

prj_dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
config_dir = os.path.join(prj_dir, "config")


def get_url_response(url):

    response = urllib.urlopen(url)

    resp_dict = json.loads(response.read().decode("utf-8"))

    return resp_dict


def get_xml():
    """
    get the xml file's value
    :param: xmlPath
    :return:activity
    """

    user_dict = {}
    xml_path = os.path.join(config_dir, "account.xml")

    # open the xml file
    per = elementTree.parse(xml_path)
    all_element = per.findall('account')

    for firstElement in all_element:
        user_name = firstElement.get("name")

        info = []

        for secondElement in firstElement.getchildren():
            account_value = secondElement.text

            info.append(account_value)

        user_dict[user_name] = info

    return user_dict

import time
import hmac
import hashlib
import base64


def get_current_time():
    return int(time.time()*1000000)


def get_account_string(access_key, secret_key):
        method_str = "method=getForwardsAccountInfo&params="
        tonce = get_current_time()
        params = "tonce=" + str(tonce) + "&accesskey=" + access_key + "&requestmethod=post&id=1&" + method_str
        phash = hmac.new(secret_key, params, hashlib.sha1).hexdigest()
        auth_string =str(tonce)+":"+'Basic '+base64.b64encode(bytes(access_key+':'+phash))
        return auth_string

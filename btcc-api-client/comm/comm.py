__author__ = 'sara'

import urllib.request
import json
from xml.etree import ElementTree as elementTree
import os

prj_dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
config_dir = os.path.join(prj_dir, "config")


# 根据给定url,获取返回值
def get_url_response(url):

    response = urllib.request.urlopen(url, timeout=10)

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

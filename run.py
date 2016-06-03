__author__ = 'sara'

import comm.comm as comm
import threading
import simulation.DepthMaker as dm
from multiprocessing import Process


class RunServer(threading.Thread):

    def __init__(self, dp):
        threading.Thread.__init__(self)
        self.dp = dp

    def run(self):
        self.dp.make_depth(1000)


def run():
    '''
    运行程序的方法
    :return:
    '''

    users_dict = comm.get_xml()

    for user in users_dict:
        depth_maker = dm.DepthMaker(users_dict[user][0], users_dict[user][1])

        # print(users_dict[user][0])
        # print(users_dict[user][1])
        t = RunServer(depth_maker)
        p = Process(target=t.start())
        p.start()


run()

__author__ = 'sara'
from socketIO_client import SocketIO



# socket_io = SocketIO('https://websocket.btcchina.com', verify=False)



from socketIO_client import SocketIO, LoggingNamespace

def on_bbb_response(*args):
    print('on_bbb_response', args)

with SocketIO('https://websocket.btcchina.com',  verify=True) as socketIO:

    if(socketIO.connected() is True):
        print 1111
    socketIO.emit('marketdata_cnybtc', on_bbb_response)
    socketIO.wait_for_callbacks(seconds=1)

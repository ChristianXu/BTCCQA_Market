__author__ = 'sara'

from comm import btcc

access_key = "9d2372a8-14be-46d8-ac6f-466cd6faa29e"
secret_key = "e8a2b633-82fc-464f-94b2-c7639d64efbd"


btc = btcc.BTCC(access_key, secret_key)

result = btc.sell(3594.12, 1)
print(result)
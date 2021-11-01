from marketplace import MarketPlace
from pprint import pprint


mp = MarketPlace()

r = mp.get(mp.url_userinfo)
r.raise_for_status()
pprint(r.json())


OPTIMADE_APP_ID='4909efbc-c61a-4b77-8bdc-6df139f98092'
r = mp.get(f'/api/proxy/proxy/{OPTIMADE_APP_ID}/heartbeat')
r.raise_for_status()
print(r.content)

r = mp.get(f'/api/proxy/proxy/{OPTIMADE_APP_ID}/test')
r.raise_for_status()
pprint(r.json())

r = mp.get(f'/api/proxy/proxy/{OPTIMADE_APP_ID}/structures/1')
r.raise_for_status()
print(r.content)

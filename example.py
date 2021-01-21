from marketplace import MarketPlace
from pprint import pprint


mp = MarketPlace()

r = mp.get(mp.url_userinfo)
r.raise_for_status()
pprint(r.json())

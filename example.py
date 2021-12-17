from pprint import pprint

from marketplace import MarketPlace

mp = MarketPlace()

# Show the user information
response = mp.get(mp.url_userinfo)
response.raise_for_status()
pprint(response.json())

SOME_MARKEPTLACE_APP_ID = "203522a2-dfac-481c-bd9e-46806b6d06f1"

# Check whether the application can be reached and is alive:
r = mp.get(f"/api/proxy/proxy/{SOME_MARKEPTLACE_APP_ID}/heartbeat")
r.raise_for_status()
pprint(r.json())

# List available data sets
r = mp.get(f"/api/proxy/proxy/{SOME_MARKEPTLACE_APP_ID}/datasets/")
r.raise_for_status()
print(r.content)

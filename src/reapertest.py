import finnhub
import json
finnhub_client = finnhub.Client(api_key="c48ski2ad3ief8nkb3vg")



x = finnhub_client.quote(f'AAPL') #FT starts for finnhub return
print(x["c"])

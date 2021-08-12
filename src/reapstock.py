import finnhub
finnhub_client = finnhub.Client(api_key="")

print(finnhub_client.technical_indicator(symbol="GPS", resolution='D', _from=1583098857, to=1584308457, indicator='sto', indicator_fields={"timeperiod": 3}))
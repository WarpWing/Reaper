import finnhub
import os 
from dotenv import *


# General Values 
load_dotenv()
KEY = os.getenv("STOCK_TOKEN")
finnhub_client = finnhub.Client(api_key=KEY)



# Functions array begins 


def stock_price(symbol):
    ft = finnhub_client.quote(f'{symbol}') #FT starts for finnhub return
    rt = (ft["c"]) #RT stands for Return
    return rt
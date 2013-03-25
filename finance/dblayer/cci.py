import utils.config
from datetime import *
from dblayer.models import *
from math import fabs

def cci_Day(symbol,Day_date):
    date=Day_date
    n_tprice=0
    mean=0
    for item in range(0,utils.config.n):
        item_date=Day_Date-timedelta(item)
        day=Equity_quotes.objects.filter(ei__Symbol=symbol,Datetime__gte=item_date)[0]
        tprice[item]=(day.high+day.close+day.low)/3
        n_tprice=n_tprice+tprice[item]
    n_tprice=n_tprice/(utils.config.n)
    for item in range(0,utils.config.n):
        mean=mean+fabs(tprice[item]-n_tprice)
    mean=mean/(utils.config.n)
    cci_Day = (tprice[utils.config.n]  -  n_tprice) / (.015 * mean)
    return cci_day


def cci_Tick(n_lines):
    data_array=n_lines[0].split(',')
    n_tprice=0
    n_tick=0
    mean=0
    for item in n_lines:
        data_array=item.split(',')
        tprice[n_tick]=utils.config.getTprice(data_array[1:5])
        n_tprice=n_tprice+ttprice[n_tick]
        n_tick+=1
    n_tprice=n_tprice/n_tick
   
    for item in range(0,n_tick):
        mean=mean+fabs(tprice[item]-n_tprice)
    mean=mean/n_tick
    cci_tick = (tprice[n_tick-1]  -  n_tprice) / (.015 * mean)
    return cci_tick

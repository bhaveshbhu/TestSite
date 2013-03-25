'''
Created on 12-Mar-2013

@author: sushil
'''
import utils.config
from models import Equity_quotes
from datetime import *

def tikMovingAverage(Tik_price,N_tik):
    global gsum
    global glist
    if N_tik==1:
        gsum=Tik_price
        glist=[Tik_price]
    elif N_tik<=utils.config.n:
        gsum+=Tik_price
        glist+=[Tik_price]
    else:
        gsum+=(Tik_price-glist.pop(0))
        glist+=[Tik_price]
        return gsum/utils.config.n
    return gsum/N_tik

def dayMovingAverage(symbol,Day_Date,day1_price):
    n_day=1
    n_day_sum=day1_price
    for item in range(1,utils.config.n):
        item_date=Day_Date-timedelta(item)
        day=Equity_quotes.objects.filter(ei__Symbol=symbol,Datetime__gte=item_date)
        if len(day)==0:
            break
        else:
            n_day+=1
            l=[day[0].close,day[0].high,day[0].low,day[0].open]
            n_day_sum+=utils.config.getPrice(l)
    return n_day_sum/n_day

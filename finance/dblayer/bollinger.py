# bhavesh sharma
#date : 10- 03-2013
# functions to calculate n-tick and n-day bollinger band indicator

import utils.config
from datetime import *
from dblayer.models import *
from math import sqrt

def bollingerDay(symbol,Day_Date,day1_price,m_avg_day):
    n_day=1
    n_day_sum=0
    for item in range(1,utils.config.n):
        item_date=Day_Date-timedelta(item)
        day=Equity_quotes.objects.filter(ei__Symbol=symbol,Datetime__gte=item_date)
        if len(day)==0:
            break
        else:
            n_day+=1
            l=[day[0].close,day[0].high,day[0].low,day[0].open]
            standard_deviation_diff=(utils.config.getPrice(l)-m_avg_day)
            n_day_sum+=standard_deviation_diff*standard_deviation_diff
    standard_deviation= sqrt(n_day_sum/n_day)
    return m_avg_day+2*standard_deviation,m_avg_day-2*standard_deviation

def bollingerTick(moving_average_tick,n_lines):
    n_sum_tick=0
    no_of_tick=1
    for item in n_lines:
        no_of_tick=no_of_tick+1
        data_array=item.split(',')
        val= utils.config.getPrice(data_array[1:5])
        #print val, moving_average_tick
        standard_deviation_tick_diff = (val-moving_average_tick)
        n_sum_tick+=standard_deviation_tick_diff*standard_deviation_tick_diff
    standard_deviation_tick= sqrt(n_sum_tick/no_of_tick)
    return moving_average_tick + 2*standard_deviation_tick, moving_average_tick -2*standard_deviation_tick
    

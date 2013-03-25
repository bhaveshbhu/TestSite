'''
Created on 15-Mar-2013

@author: sushil
'''

import utils.config
from datetime import *
from dblayer.models import *
from math import sqrt

def rsi_calc_d(symbol,Day_Date):
    day=Equity_quotes.objects.filter(ei__Symbol=symbol,Datetime__lte=item_date)[0]
    close_new=day.close
    date=Day_Date
    for item in range (14):
        item_date=date-timedelta(item)
        day=Equity_quotes.objects.filter(ei__Symbol=symbol,Datetime__lte=item_date)[0]
        close_old=day.close
        if(close_new-close_old>0):
            gain+=close_new-close_old
        else:
            loss+=close_old-close_new
        close_old=day.close
    gain=gain/14
    loss=loss/14
    rs=gain/loss
    rsi=100-(100/(1+rs))
    return loss,gain,rsi

def rsi_calc_d2(symbol,Day_Date,loss,gain):
    day=Equity_quotes.objects.filter(ei__Symbol=symbol,Datetime__lte=item_date)[0]
    close_new=day.close
    date=Day_Date
    item_date=date-timedelta(1)
    day=Equity_quotes.objects.filter(ei__Symbol=symbol,Datetime__lte=item_date)[0]
    if(close_new>close_old):
        gain_new=close_new-close_old
    else:
        loss_new=close_old-close_new
    gain=(gain*13+gain_new)/14
    loss=(loss*13+loss_new)/14
    rs=gain/loss
    rsi=100-(100/(1+rs))
    return loss,gain,rsi

def day_check(Day_Date,symbol):
    if Equity_quotes.objects.filter(ei__Symbol=symbol).count()==0:
        return 0
    First_date = Equity_quotes.objects.filter(ei__Symbol=symbol).order_by('Datetime')[0].Datetime.date()
    return (Day_Date-First_date).days

def tikRsi(Tik_price,N_tik):
    defalt=14
    global gpre_tik_price
    global gavg_gain
    global gavg_loss
    if N_tik==1:
        gavg_gain=0
        gavg_loss=0 
    else:
        current_gain_loss=Tik_price-gpre_tik_price
        if N_tik>defalt:
            N_tik=defalt
        if current_gain_loss<=0:
            gavg_loss=(gavg_loss*(N_tik-1)+current_gain_loss)/N_tik
        if current_gain_loss>=0:
            gavg_gain=(gavg_gain*(N_tik-1)+current_gain_loss)/N_tik
    gpre_tik_price=Tik_price
    if gavg_loss==0:
        rs=0
    else:
        rs=gavg_gain/gavg_loss
    return 100-(100/(1+rs))


    
    
#sushil kumar
#22-2-13
#1-3-13

import urllib2
import utils.config
from models import Equity_instruments,Equity_quotes
from django.http import HttpResponse
from datetime import *
from bollinger import *
from movingAverage import *
from rsi import *
from cci import *

print 'Fetching Data...'

def dayCount(symbol):
    if Equity_quotes.objects.filter(ei__Symbol=symbol).count()==0:
        return utils.config.n
    else:                                                       
        lastTime = Equity_quotes.objects.filter(ei__Symbol=symbol).latest('Datetime')
        return (lastTime.Datetime.date()-datetime.now().date()).days

def dataFetch(request):
    utils.config.proxyConnect()
    for symbol in utils.config.symbols_list:
        #Days=(dayCount(symbol)-datetime.now().date()).days
        wrapDataFetch(symbol,dayCount(symbol))
    return HttpResponse('Feeding successful')
   
def wrapDataFetch(symbol,days):
    url=utils.config.fetch_site_url %(symbol,days)
    html = urllib2.urlopen(url).read().strip().strip('"').strip(',')
    fetched_lines=html.split('\n')
    extra_lines=utils.config.ignoreLines(fetched_lines)
    dataFeed(fetched_lines[extra_lines:],symbol,days)
   
def dataFeed(fetched_lines,symbol,days):
    tik=0
    for day in range(int(days)):
        day_first_data=fetched_lines[tik].split(',')
        hour0=int(day_first_data[0])
        day_date=date.fromtimestamp(hour0)
        tik1_price=utils.config.getPrice(day_first_data[1:5])
        day_moving_average=dayMovingAverage(symbol,day_date,tik1_price)
        
        no_of_days=day_check(day_date,symbol)
        if(no_of_days==14):
            loss,gain,rsi_var=rsi_calc_d(symbol,day_date)
        if(no_of_days>14):
            loss,gain,rsi_var=rsi_calc_d(symbol,day_date,loss,gain)
        else :
            rsi_var=0
        
        Bollinger_dayup_variable,Bollinger_daylow_variable = bollingerDay(symbol,day_date,tik1_price,day_moving_average)
        Equity_quotes().create(ei=Equity_instruments.objects.get(Symbol=symbol),
                           Datetime=datetime.fromtimestamp(hour0),
                           open=float(day_first_data[4]),
                           low=float(day_first_data[3]),
                           high=float(day_first_data[2]),
                           close=float(day_first_data[1]),
                           ltp=0,
                           marker=0,
                           m_avg=tikMovingAverage(tik1_price,tik+1),
                           rsi=tikRsi(tik1_price,tik+1),
                           ##we have to also add Bollinger_upper and Bollinger_lower here for days first tik
                           #**(indicators()),
                           m_avg_day=day_moving_average,
                           
                           rsi_day=rsi_var,
                           
                           Bollinger_dayup=Bollinger_dayup_variable,Bollinger_daylow=Bollinger_daylow_variable,
                           )
        tik+=1
        while len(fetched_lines)>tik and date.fromtimestamp(int(fetched_lines[tik].split(',')[0]))==day_date:
            n_tik=utils.config.n
            if(tik<n_tik-1):
                n_tik=tik+1
            data_array=fetched_lines[tik].split(',')
            #tik_moving_average=tikMovingAverage(fetched_lines[tik-n_tik+1:tik+1])/n_tik
            this_tik_price=utils.config.getPrice(data_array[1:5])
            tik_moving_average=tikMovingAverage(this_tik_price,tik+1)
            tik_rsi=tikRsi(this_tik_price,tik+1)
            Bollinger_upper_variable,Bollinger_lower_variable = bollingerTick(tik_moving_average,fetched_lines[tik-n_tik+1:tik+1])
            Equity_quotes().create(ei=Equity_instruments.objects.get(Symbol=symbol),
                           Datetime=datetime.fromtimestamp(int(data_array[0])),
                           open=data_array[4],
                           low=data_array[3],
                           high=data_array[2],
                           close=data_array[1],
                           ltp=0,
                           marker=int((int(data_array[0])-hour0)/3600)+1,
                           m_avg=tik_moving_average,
                           rsi=tik_rsi,
                           Bollinger_upper = Bollinger_upper_variable,Bollinger_lower = Bollinger_lower_variable,
                           #**(indicators()),
                           )
            tik+=1
         

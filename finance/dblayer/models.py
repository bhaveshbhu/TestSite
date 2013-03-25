#bhavesh sharma
#date : 13-02-2013

#Edit:
#sushil kumar
#20-2-2013

#LAYER to access db

from django.db import models
#from datetime import datetime

# Create your models here.

class Equity_instruments(models.Model):
    Symbol = models.CharField(max_length=20)
    type = models.CharField(max_length=50,default='Equity')
    Series=models.CharField(max_length=50,default='EQ')

    def __unicode__(self):
        return self.Symbol
    
    def create(self,**kwargs):
        Equity_instruments(**kwargs).save()
        
class Equity_quotes(models.Model):
    ei = models.ForeignKey(Equity_instruments)
    Datetime = models.DateTimeField(primary_key=True)
    open = models.FloatField()
    low = models.FloatField()
    high = models.FloatField()
    close = models.FloatField()
    ltp = models.FloatField()
    marker=models.IntegerField()
    m_avg = models.FloatField(default=0)
    rsi = models.FloatField(default=0)
    cci=models.FloatField(default=0)
    macd=models.FloatField(default=0)
    Bollinger_upper=models.FloatField(default=0)
    Bollinger_lower=models.FloatField(default=0)
    m_avg_day=models.FloatField(null=True)
    rsi_day=models.FloatField(null=True)
    cci_day=models.FloatField(null=True)
    macd_day=models.FloatField(null=True)
    Bollinger_dayup=models.FloatField(null=True)
    Bollinger_daylow=models.FloatField(null=True)
    earnings=models.FloatField(null=True)
    no_of_shares_outstanding=models.FloatField(null=True)
    growth=models.FloatField(null=True)
    price2earning_ratio=models.FloatField(null=True)
    mkt_cap_pn=models.FloatField(null=True)
    PEratio2growth_ratio=models.FloatField(null=True)
     
    def create(self,**kwargs):
        Equity_quotes(**kwargs).save()        

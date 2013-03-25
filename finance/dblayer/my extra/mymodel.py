#bhavesh sharma
#date : 13-02-2013
#LAYER to access db
#Edit:
#sushil kumar
#20-20-2013
from django.db import models
from django import forms
from datetime import datetime

# Create your models here.

class Equity_instruments(models.Model):
    Symbol = models.CharField(max_length=20)
    type = models.CharField(max_length=50,default='Equity')
    Series=models.CharField(max_length=50,default='EQ')
    
    def create(self,**kwargs):
        Equity_instruments(**kwargs).save()
        


class Equity_quotes(models.Model):
     ei = models.ForeignKey(Equity_instruments)
     Datetime = models.DateTimeField()
     open = models.FloatField()
     low = models.FloatField()
     high = models.FloatField()
     close = models.FloatField()
     ltp = models.FloatField()
     rsi = models.FloatField()
     m_avg = models.FloatField()
     
     def create(self,**kwargs):
        Equity_quotes(**kwargs).save()
         

     
class EIF(forms.ModelForm):
    class Meta:
        model = Equity_instruments

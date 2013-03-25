from django.contrib import admin
from dblayer import models
class EIA(admin.ModelAdmin):
    list_display=('Symbol','type','Series')
class EQA(admin.ModelAdmin):
    list_display=('ei',
     'Datetime', 
     'open',
     'low',
     'high',
     'close', 
     'ltp',
     'marker',
     'm_avg',
     'm_avg_day',
     'rsi',
     'rsi_day',
     'cci',
     'cci_day',
     'macd',
     'macd_day',
     'Bollinger_upper',
     'Bollinger_lower',
     'Bollinger_dayup',
     'Bollinger_daylow',
        )
admin.site.register(models.Equity_instruments,EIA)
admin.site.register(models.Equity_quotes,EQA)

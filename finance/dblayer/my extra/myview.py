import urllib2
import string
import utils.config
from models import Equity_instruments,Equity_quotes,EIF	
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render_to_response,HttpResponseRedirect
from django.template import RequestContext

def archive(request):
   posts = Equity_instruments.objects.all()
   return render_to_response('archive.html', {'posts': posts,'form': EIF}
                             ,RequestContext(request))

def formDB(request):
   if request.method == 'POST':
      form = EIF(request.POST)
      if form.is_valid():
         form.save()
   return HttpResponseRedirect('/dblayer/show/')


print 'Fetching Data...'

def dataFetch(request,offset):
   proxyConnect()
   for symbol in config.symbols_list:
      wrapDataFetch(symbol,offset)
   return HttpResponse('Feeding succesful')

def proxyConnect():
   proxy_support = urllib2.ProxyHandler({"http":"http://@127.0.0.1:8118"})
   opener = urllib2.build_opener(proxy_support)
   urllib2.install_opener(opener)
   
def wrapDataFetch(symbol,days):
      url=config.fetch_site_url %(symbol,days)
      html = urllib2.urlopen(url).read().strip().strip('"').strip(',')
      fetched_lines=html.split('\n')
      dataFeed(fetched_lines[15:],symbol)
   

def dataFeed(fetched_lines,symbol):
      r=Equity_instruments.objects.get(Symbol=symbol)
      for item in fetched_lines:
         data_array=item.split(',')
         feedQuotes=Equity_quotes()
         feedQuotes.create(ei=r,
                           Datetime=datetime.fromtimestamp(float(data_array[0])),
                           open=data_array[4],
                           low=data_array[3],
                           high=data_array[2],
                           close=data_array[1],
                           ltp=0,
                           rsi=0,
                           m_avg=0)
         

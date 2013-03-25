#sushil kumar
#22-2-13
from dblayer.models import Equity_instruments 
import config
from django.http import HttpResponse
def install(request):
    for symbol in config.symbols_list:
        if Equity_instruments.objects.filter(Symbol=symbol).exists()==0:
            Equity_instruments().create(Symbol=symbol)
    return HttpResponse("Symbols successfully inserted in database")

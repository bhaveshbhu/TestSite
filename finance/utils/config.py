#sushil kumar
#22-2-13

#contains all configurations
import urllib2

symbols_list=('ACC.NS','GOOG','YHOO','NAUKRI.BO')

fetch_site_url='http://chartapi.finance.yahoo.com/instrument/1.0/%s/chartdata;type=quote;range=%sd/csv'

n=5

def getPrice(price_list):
    p=(float(price_list[1])+float(price_list[2]))/2
    return p

def ignoreLines(Lines):
    ignore_count =0
    for item in Lines:
        if not item[0].isdigit():
            ignore_count+=1
        else :
            return ignore_count
    
def proxyConnect():
    proxy_support = urllib2.ProxyHandler({"http":"http://@127.0.0.1:8118"})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
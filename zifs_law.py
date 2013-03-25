'''
Author: @bhavesh
Date : 22-02-2013
'''

from collections import Counter
from math import *
from pylab import *

def zifPlot(sorted_list):
    i=0
    rankLog = []
    freqLog = []
    for words in sorted_list:
        rankLog.append(log(i+1))
        freqLog.append(log(words[1]))
        i=i+1
    i=0
    for r in rankLog:
        print rankLog[i],freqLog[i]
        i=i+1
    plot(rankLog,freqLog)
    xlabel('log(r)')
    ylabel('log(f)')
    show()

if __name__ == '__main__':
    f=open('input.txt','r')
    contents=f.read()
    f.close()
    mywords=contents.lower().strip(',').strip().split(None)
    
    #mywords=['red','black','red','red','black','blue']
    frequency=Counter(mywords)
    words =frequency.items()
    sorted_list=sorted(words,key = lambda item: item[1], reverse=True)
    for words in sorted_list:
        print words
    zifPlot(sorted_list)
    
    

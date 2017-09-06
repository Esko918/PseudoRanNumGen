import os
from StockMarket import *
from RandomNumGenerator import *

try:
    sm = StockMarket()
    results = sm.smHtdcPhaseData("GOOG", "COMPACT")
    ran = RandomNumGenerator()
    for i in results:
        print (ran.randomTokenGenerator(i))
        print ("\n")
except:
    print("Exception was thrown cannot continue with Pseudo Ran Num Generation")
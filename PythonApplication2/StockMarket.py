import urllib.request
import json
from StockMarketUrlCreator import *

class StockMarket:
    def smHtdcPhaseData(self,smQuote, smSeriesType):
        try:
            response = urllib.request.urlopen(StockMarketUrlCreator.htdcPhaseUrl("HT_DCPHASE", smQuote,smSeriesType))
            if(response.code == 200):
                results = response.read()
                results = json.loads(results)
                results = results['Technical Analysis: HT_DCPHASE']
                htdcValues = []
                for date in results:
                    value = results[date]
                    htdcValues.append(value['HT_DCPHASE'])
                return htdcValues
            else:
                print ('Error Occured while getting response from server')
                print ('Status Code %s' % response.code)
                raise
        except:
            raise

        
                



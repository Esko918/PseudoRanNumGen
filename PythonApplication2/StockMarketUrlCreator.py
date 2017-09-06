class StockMarketUrlCreator:
   @staticmethod
   def htdcPhaseUrl(smFunction, smSymbol, smSeriesType):
       try:
            apiKey = "VROCXCFBMWJQAML6"
            url = "https://www.alphavantage.co/query?function=%s&symbol=%s&series_type=%s&interval=1min&apikey=%s"
            return url % (smFunction, smSymbol, smSeriesType, apiKey)
       except:
            print("Sorry Stock Market URl Failed On creating the URL")
            raise



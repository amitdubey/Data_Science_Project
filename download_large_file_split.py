
from yahoofinancials import YahooFinancials
import pandas as pd
import bisect
import timeit
import statistics
import numpy as np
from functools import reduce
import pandas as pd
from random import sample
from re import split
import os
import glob
import logging

number_of_chunks =4
START_DATE = "2019-03-19"
END_DATE = "2021-03-19"
INTERVAL ='daily'
STOCK_NAME ='%5EGSPC'
FOLDER_LOCATION ="/Users/amitdubey/Documents/GitHub/Data_Science_Project/"

#download SPY data from yahoo financials
"""Download the large data file from yahoo for a given period and given asset

    Returns: object of list type of float numbers with 1 digit precision named as results
        [type]: class to download SPY asset into dataframe and divide into 4 equal chunks and then read it
    """
class downloadHistoryStockData(object):
    def downloadfile(self,number_of_chunks,STOCK_NAME,START_DATE,END_DATE,INTERVAL,FOLDER_LOCATION) -> float:    
        assets =[STOCK_NAME]
        yahoo_financials = YahooFinancials(assets)
        
 
        # initialize the log settings
        logging.basicConfig(filename = FOLDER_LOCATION+'/app.log', level = logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')
        try:
            data =yahoo_financials.get_historical_price_data(START_DATE,END_DATE,INTERVAL)
        except IOError as e:
            logging.exception(str(e))

       
        #get the prices by date
        prices_df = pd.DataFrame({
            a: {x['formatted_date']: x['adjclose'] for x in data[a]['prices']} for a in assets
        })
        

        #rename the index to column correctly
        prices_df.reset_index(inplace=True)
        prices_df = prices_df.rename(columns = {'index':'date','%5EGSPC':'SPY'})

        #convert the column to float and also round it
        df= prices_df["SPY"].astype('float')
        df=list(prices_df.SPY.values)
        df = [round(num, 1) for num in df]

        #Split the file into the defined no. of chunks
        try:
            for i,chunk in enumerate(np.array_split(df, number_of_chunks)):
                chunk =pd.DataFrame(chunk)
                chunk.to_csv('chunk{}.csv'.format(i), index=False)
        except IOError as e:
            logging.exception(str(e))

        #read the chunks to merge them together into one large file
        os.chdir(FOLDER_LOCATION)
        results = pd.DataFrame([])
        try:
            for counter, file in enumerate(glob.glob("chunk*.csv")):
                namedf = pd.read_csv(file,skiprows=0)
                results = results.append(namedf)
        except IOError as e:
            logging.exception(str(e))        
        #print(results)

        results.reset_index(drop=True,inplace=True)
        return results
     
def main():
    d =downloadHistoryStockData()
    result =d.downloadfile(number_of_chunks,STOCK_NAME,START_DATE,END_DATE,INTERVAL,FOLDER_LOCATION)
    #test code if values are coming properly or not
    print(result)
    #print(type(result))


if __name__ == '__main__':
    main()
    




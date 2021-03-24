
import numpy as np
import download_large_file_split as dl
import statistics
from functools import reduce
import pandas as pd

l=pd.DataFrame(data=None)

"""Class Median containing multiple median functions 

Returns:
    [median]: [returns the median of the float list passed from the large file object]
"""
class Median(object):
    def median1(self)->float:
        return ( statistics.median(self.l.values))


    def median2(self)-> float:
        return (  np.median(self.l.values))

    def median3(self)-> float:
        return pd.Series(map(float,self.l.values)).median()

    def median4(self)-> float:
        data = sorted(self.l.values)
        n = len(data)
        if n == 0:
            return None
        if n % 2 == 1:
            return data[n // 2]
        else:
            i = n // 2
        return ( (data[i - 1] + data[i]) / 2)

    def median5(self)-> float:
        quotient, remainder = divmod(len(self.l), 2)
        if remainder:
            return sorted(self.l.values)[quotient]
        return ( sum(sorted(self.l.values)[quotient - 1:quotient + 1]) / 2)



"""Class Mean containing multiple median functions 

Returns:
    [Mean]: [returns the Mean of the float list passed from the large file object]
"""

class Mean(object) :
    def mean1(self) -> float:
        return statistics.mean(map(float,self.l.values))
    def mean2(self)-> float:
        return ( sum(self.l.values) / len(self.l))


    def mean3(self)-> float:
        return (  np.mean(self.l.values))

    def mean4(self)-> float:
        return (np.array(self.l).mean())


    def mean5(self)-> float:
        return (  reduce(lambda x, y: x + y / float(len(self.l)), self.l.values, 0))

    def mean6(self)-> float:
        return ( pd.Series(self.l.all()).mean())

def main():
    
    d1 = dl.downloadHistoryStockData()
    results =d1.downloadfile(dl.number_of_chunks, dl.STOCK_NAME, dl.START_DATE, dl.END_DATE, dl.INTERVAL, dl.FOLDER_LOCATION)
    m1 = Median()
    m2 = Mean()
    m1.l =results
    m2.l=results
    print('****************************************************')
    print('Mean is mean 1', m2.mean1())
    print('Mean is mean 2', m2.mean2())
    print('Mean is mean 3', m2.mean3())
    print('Mean is mean 4', m2.mean4())
    print('Mean is mean 5', m2.mean5())

    print('****************************************************')
    print('Median is median 1', m1.median1())
    print('Median is median 2', m1.median2())
    print('Median is median 3', m1.median3())
    print('Median is median 4', m1.median4())
    print('Median is median 5', m1.median5())

if __name__ == '__main__':
    main()
    
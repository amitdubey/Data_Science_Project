# Data Science Project- 1
 
  Data Science Coding Project – AMIT DUBEY
Architecture of the file handling is divided into four parts:
1.    Data – Scope of this is to test large amount of data generated in files, ranging from thousands of records to millions of records using python pandas or dask dataframe.
2.    Script execution triggers – There are the points from where scripts can be triggered to perform data validation. It can be manually for selected scripts execution, in a CICD pipeline (e.g., Jenkins) or as part of batch process to do continuous testing.
3.    Execution strategy– This consists of two parts. Pandas or dask library of python would be core to writing the operations to perform data validation and python based unittest library as test framework work-either existing or custom-would be the script organizer based the methodology which project wants to follow.
4.    Results in equal chunks– This is last part where results would be generated in different chunks in a specified format which can later be used to analyze execution results.

 

Code files:

download_large_file_split.py	Download data -----Prepare data, Divide data, Read the chunks data
Class downloaddatafile has a function, logger and exception handling	Can be more efficient with high powered computing or cloud reading engines and 
Input: stream data from URL
Output: data frame, csv’s into 4 equal chunks at defined folder location (folderlocation)


performance_testing_function.py	------------Measuring 5 different ways to calculate mean and median on the chunks and then calculating the total mil seconds execution time for 100 iteration of each function on the data	Performance measurement
Input: incoming dataframe from SPY asset csv
Output: result of each function on 100 iteration of each function
 
 
unit_testing.py	----------Unit testing each version of mean1-5 function and median 1-5 in a generic and positive test case only	The negative test cases can be many scenarios hence to save time I have not gone much into it but can extend the class to multiple negative, corner and low-level scenarios.

mean_media_class.py---------	Two Classes containing mean and median separately, can be joined into one class as well as part of attribute
Each mean 1-5 or median 1-5 functions return float value	Input: result data frame incoming from large file chunks
Output: float value of mean or median for each respective function


Reusability : 
1.	downloaddatafile has a class for reusability, folder path, chunk size, asset all can be passed dynamically.
2.	Mean and median also are two classes with functions inside it, making these classes to choose whichever function to reuse and even extend
Readability: all classes and methods are commented with return type and objective and what purpose it serves.

Unit tests:
Generic tests: tests for consistency whether the data has zero length, one element
Specific tests: positive test scenarios of matching means/median for each function variation, to save the time, I have not added the negative and corner cases, low level cases but can add further.

Design: 
There are many areas which can be modified in this architecture and can be made more complex but for sake of presentability I have kept it simple and each file itself can be tested standalone and run independently for ease of usage.
Architecture is extensible and reusable, have simple logger but I can design a more complex pinpoint or transformer logger pattern to measure the script performance in the log.

Bugs: 
1.	File stream can crash during the data retrieval 
2.	Write disk might overflow
3.	Network bandwidth dependent
4.	Validating the mean and median for large records is daunting task i.e. finding mean for 10 million records can only be done “just in time”
5.	Data will always change, so a snapshot average+change average approach  should be used to calculate median and mean.
6.	Unit testing for all the possible scenarios can be difficult and there are chances of leak and data corruption

Efficiency: 
What more can be done:
1.	Email notification system to notify in case any error with the log file attached in case script exec failure or success.
2.	Other types of Data frames such as Dask, or spark df can be used for faster performance
3.	GPU and parallel reading and writing can also be done in case of scaling
4.	This model can be utilized in batch mode or online mode using flask API.
5.	Docker file and docker image can be created so that multiple versions, CI-CD can be created. 
6.	This script can be automated on dynamic asset, dates and different file locations input parameters using Kwargs, Arg python CLI properties for ease of execution.
7.	Further improvement of design patterns can also be added to create singleton, factory patterns for different test scenario or user.

Possible error when handling with large files
1.	Based on amount of data storage machines with sufficient RAM should be used for execution. For example, if you try to load 8 GB file in a machine with 4 GB RAM, it will take very long time to process the data or can even get stuck. Parallel processing using GPUs to run the tests can be great.
2.	Identifying the mean and median is going to be hard task and will require some smart unit test case to split and reach to the mean, median mode based on the length of variable data quickly.
3.	Risk on file reader getting stuck in a loop due to corruption or error is very high hence a parallel read and write should be chosen or position marker/read till this point marker should be establish so that in case of failure recovery can start from point of failure not from the beginning.

Unit testing problems and case scenarios:
1.	The test methods should cover most corner cases, and positive, negative case.
2.	The test framework should plan for and handle catastrophic failures gracefully and have pinpoint information where script or file failed.
3.	All combination of the functional tests should be tested in an automated framework which is flexible and extensible in nature.
4.	Finding the difference: There are scenario where difference between data in production and test needs to be calculated based on a key. e.g. comparing incoming values with existing non duplicate values with the key so that the differential data can be fast and results are quick.
5.	
Problems:
1.	Validating the mean and median at a given point is possible but if the data is getting refresh in a quick success, then it is going to be difficult.
2.	Performance of methods can vary based on the memory, network speed, and processing power of the system used so there is no hardcoded value be predicted for a streaming data.

Some solutions:
1.	Design validation criteria inside out i.e. designing smaller test cases to larger scenario based large data test cases.
2.	High throughput devices or memory formats hdf5 or parquet formats should be used for quick copy and efficient storage with high retrieval and insertion rate.
3.	Visual analytics to quickly identify missing or glaring errors in the files can be used.
4.	Chunk size can be used to avoid file read or read or write overflow with the memory capacity check to prevent overflow.



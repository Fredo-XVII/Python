%%javascript
/**********************************************************************************************
Known Mathjax Issue with Chrome - a rounding issue adds a border to the right of mathjax markup
https://github.com/mathjax/MathJax/issues/1300
A quick hack to fix this based on stackoverflow discussions: 
http://stackoverflow.com/questions/34277967/chrome-rendering-mathjax-equations-with-a-trailing-vertical-line
**********************************************************************************************/

$('.math>span').css("border-left-color","transparent")

%reload_ext autoreload
%autoreload 2

# directory
!dir

# list env
import os

for key, value in os.environ.items():
    print(key, value)
    


# Initiate Spark on Local:  ** Do not run this on Docker **
import sys #current as of 9/26/2015
import os

# spark_home = os.environ['SPARK_HOME'] = '/Users/jshanahan/Dropbox/Lectures-UC-Berkeley-ML-Class-2015/spark-1.6.1-bin-hadoop2.6/'
spark_home = os.environ['SPARK_HOME'] = 'C:\Apps\Apache\spark-2.0.0' #'C:\Apps\Apache\Spark-1.6.2'
if not spark_home:
    raise ValueError('SPARK_HOME enviroment variable is not set')
sys.path.insert(0,os.path.join(spark_home,'python'))
#sys.path.insert(0,os.path.join(spark_home,'python/lib/py4j-0.9-src.zip')) # for Spark-1.6.2
sys.path.insert(0,os.path.join(spark_home,'python/lib/py4j-0.10.1-src.zip')) # for spark-2.0.0

# First, we initialize the Spark environment

#import findspark
#findspark.init()

import pyspark
from pyspark.sql import SQLContext

# We can give a name to our app (to find it in Spark WebUI) and configure execution mode
# In this case, it is local multicore execution with "local[*]"
app_name = "example-logs"
master = "local[*]"
conf = pyspark.SparkConf().setAppName(app_name).setMaster(master)
sc = pyspark.SparkContext(conf=conf)
sqlContext = SQLContext(sc)


print(sc)
print(sqlContext)


# Import some libraries to work with dates
import dateutil.parser
import dateutil.relativedelta as dateutil_rd

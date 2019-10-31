# Python
Anything Python that I think is cool and useful.

# Databases
https://developer.teradata.com/tools/articles/teradata-sqlalchemy-introduction

## ODBC to Teradata

  > source : 
  
  > source : https://community.teradata.com/t5/Connectivity/Connecting-Python-to-Teradata-over-ODBC/m-p/56824
  
  ```  
  import pyodbc </code> <\n>
  connection = pyodbc.connect('DSN=_ODBCDRIVER NAME_;UID=xxxx;PWD=xxx')
  cursor = connection.cursor()
  cursor.execute("select top 10 * from schema.table")
  results = cursor.fetchall()
  print(results)
  connection.close()
  ```
-----

# PYSTACK:

### MUNGING & ADHOC ANALYSIS:
PANDAS, SCIPY, BEAUTIFULSOUP

### VISUALIZATION:
MATPLOTLIB, SEABORN, BOKEH, GGPLOT2

### MODEL BUILDING:
SCIKIT-LEARN, STATSMODELS

### SERVING RESULTS OR MODELS:
FLASK, DJANGO, TORNADO

### TESTING:
PYTEST, PYUNIT, NOSE

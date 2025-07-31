# Databricks notebook source
# MAGIC %md 
# MAGIC
# MAGIC ## Read Power BI XMLA From Databricks Notebook
# MAGIC
# MAGIC 1. Personal Compute only
# MAGIC 2. Can't use serverless (requires web terminal)
# MAGIC
# MAGIC #### Web Terminal / Init script
# MAGIC
# MAGIC ```
# MAGIC sudo apt-get update && apt-get install -y dotnet-runtime-7.0
# MAGIC ```
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %pip install pythonnet pyadomd azure-identity

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

from sys import path
path.append("/Volumes/powerbi_demos/nytaxi/powerbi/dlls")
from pythonnet import load
load("coreclr")
import clr
from pyadomd import Pyadomd
from pyspark.sql.types import StructType, StructField, StringType
#print(token)
conn= (
      
    'Provider=MSOLAP;'
    'Data Source=powerbi://api.powerbi.com/v1.0/myorg/40f113e7-13d8-47c1-b3e0-76fc609c5948;'
    'Initial Catalog=PBI_UCMetrics;'  # Replace with actual dataset name
    f'User ID={user};Password={password};'
    'Persist Security Info=True;'
    'Impersonation Level=Impersonate;'


        )
query = "Select * from $SYSTEM.TMSCHEMA_MEASURES/Volumes/powerbi_demos/nytaxi/powerbi/dlls/"
with Pyadomd(conn) as conn:
    with conn.cursor().execute(query) as cur:
        names = [ x[0] for x in cur.description]
        schema = StructType([StructField(name, StringType(), True) for name in names])
        r =cur.fetchall()
        #print(r)
        df = spark.createDataFrame(r, schema)
display(df)
# save df(s) to table(s)
# create Delta Share of tables



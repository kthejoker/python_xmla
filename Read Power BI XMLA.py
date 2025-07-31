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
path.append("/Volumes/my_volume/xmla_dlls")
from pythonnet import load
load("coreclr")
import clr
from pyadomd import Pyadomd
from pyspark.sql.types import StructType, StructField, StringType
conn= (   
    'Provider=MSOLAP;'
    f'Data Source=powerbi://api.powerbi.com/v1.0/myorg/{powerbi_group_id};'
    f'Initial Catalog={powerbi_dataset};'  # Replace with actual dataset name
    f'User ID={user};Password={password};'
    'Persist Security Info=True;'
    'Impersonation Level=Impersonate;'
        )
query = "Select * from $SYSTEM.TMSCHEMA_MEASURES"
with Pyadomd(conn) as conn:
    with conn.cursor().execute(query) as cur:
        names = [ x[0] for x in cur.description]
        schema = StructType([StructField(name, StringType(), True) for name in names])
        result =cur.fetchall()
        df = spark.createDataFrame(result, schema)
display(df)
# save df(s) to table(s)
# create Delta Share of tables
# knock your socks off

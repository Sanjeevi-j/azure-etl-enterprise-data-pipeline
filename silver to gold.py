# Databricks notebook source
# MAGIC %md
# MAGIC >** Doing trf to cahnging column name for all tables ******

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls('mnt/silver/SalesLT/'):
    table_name.append(i.name.split('/')[0])

# COMMAND ----------

table_name

# COMMAND ----------

for name in table_name:
    path = '/mnt/silver/SalesLT/' + name
    print(path)
    df = spark.read.format('delta').load(path)

    # Get the list of column names
    column_names = df.columns

    for old_col_name in column_names:
        # Convert column_name to snake_case format
        new_col_name = "".join([
            "_" + char.lower() if char.isupper() and (i == 0 or not old_col_name[i - 1].isupper()) else char.lower()
            for i, char in enumerate(old_col_name)
        ]).lstrip("_")

        # Rename the column
        df = df.withColumnRenamed(old_col_name, new_col_name)

    output_path = '/mnt/gold/SalesLT/' + name + '/'
    df.write.format('delta').mode("overwrite").save(output_path)

# COMMAND ----------

display(df)

# COMMAND ----------

from pyspark.sql.functions import col, substring

# Define the table name
table_name = ['Product']

for name in table_name:
    path = '/mnt/silver/SalesLT/' + name
    print(path)
    df = spark.read.format('delta').load(path)

    # Get the list of column names
    column_names = df.columns

    for old_col_name in column_names:
        # Convert column_name to snake_case format
        new_col_name = "".join([
            "_" + char.lower() if char.isupper() and (i == 0 or not old_col_name[i - 1].isupper()) else char.lower()
            for i, char in enumerate(old_col_name)
        ]).lstrip("_")

        # Rename the column
        df = df.withColumnRenamed(old_col_name, new_col_name)

    # Reduce the length of 'thumb_nail_photo' column to 10 characters
    df = df.withColumn('thumb_nail_photo', substring(col('thumb_nail_photo'), 1, 10))

    # Overwrite the data in the same location
    output_path = '/mnt/gold/SalesLT/' + name + '/'
    df.write.format('delta').mode("overwrite").save(output_path)

display(df)

# Databricks notebook source
# To mount a ***Bronze folder****

# Check if the directory is already mounted
mounts = [mount.mountPoint for mount in dbutils.fs.mounts()]

if "/mnt/bronze" not in mounts:
    configs = {
      "fs.azure.account.auth.type": "CustomAccessToken",
      "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
    }

    # Optionally, you can add <directory-name> to the source URI of your mount point.
    dbutils.fs.mount(
      source = "abfss://bronze@sanjdemosa123.dfs.core.windows.net/",
      mount_point = "/mnt/bronze",
      extra_configs = configs)
else:
    print("Directory already mounted: /mnt/bronze")

# COMMAND ----------

dbutils.fs.ls("/mnt/bronze/SalesLT/")

# COMMAND ----------

# To mount a ****silver folder*****
configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
}

# Ensure the URI is correct and the filesystem exists
dbutils.fs.mount(
  source = "abfss://silver@sanjdemosa123.dfs.core.windows.net/",
  mount_point = "/mnt/silver",
  extra_configs = configs)

# COMMAND ----------

# To mount a  ***** gold folder******
configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")
}

# Ensure the URI is correct and the filesystem exists
dbutils.fs.mount(
  source = "abfss://gold@sanjdemosa123.dfs.core.windows.net/",
  mount_point = "/mnt/gold",
  extra_configs = configs)

# COMMAND ----------



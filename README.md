# Azure ETL & Data Engineering Project: Enterprise Data Pipeline Architecture

## Introduction

The goal of this project was to design and implement a comprehensive data engineering solution that automates the process of ingesting, transforming, and visualizing data. The pipeline is built using Azure services such as **Azure Data Factory**, **Azure Databricks**, and **Azure Data Lake Storage**, with a focus on scalability, automation, and data governance. By leveraging the **Medallion Architecture** (Bronze, Silver, Gold layers), we can ensure a structured flow of data from raw ingestion to insights.

---
## Architecture

![Architecture](https://github.com/user-attachments/assets/6ef66aa6-942c-48fa-b7b5-f2b94013fc39)

---

## Architecture Overview

The architecture follows the **Medallion Architecture** pattern and is designed to handle large-scale data processing tasks in a structured and efficient manner.

1. **Bronze Layer**: Raw data ingestion from on-prem SQL databases and external sources is stored in Azure Data Lake.
2. **Silver Layer**: Data transformations are applied using Azure Databricks (PySpark) to clean and format data, making it suitable for analytics.
3. **Gold Layer**: Final, analytics-ready data is stored for easy querying and consumption by tools like Azure Synapse and Power BI.

---

## Technologies

- **Azure Data Factory**: Orchestration and automation of data pipelines.
- **Azure Databricks**: Efficient data transformation with scalable processing.
- **Azure Data Lake Storage Gen2**: Scalable and secure data storage.
- **Azure Synapse Analytics**: For big data and analytics processing.
- **Power BI**: For visualization and reporting.

---

## Dataset Used
 The **AdventureWorksLT2017** database is a sample relational database provided by Microsoft, commonly used for demonstrating SQL Server capabilities. In this project, it serves as the source data for the ETL pipeline, hosted on an on-premises Microsoft SQL Server.
- Database link: [AdventureWorksLT2017](https://tinyurl.com/AdventureWorksLT2017)

## Data Model
![Data Model](https://github.com/user-attachments/assets/294cf674-4577-428d-b97f-31d71364a743)


## Scripts for Project

1. Storage Mount    - [storagemount.py](storagemount.py)  
2. Bronze to Silver - [bronzetosilver.py](bronzetosilver.py)  
3. Silver to Gold   - [silvertogold.py](silvertogold.py)









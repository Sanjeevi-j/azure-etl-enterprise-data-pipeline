# Azure ETL & Data Engineering Project: Enterprise Data Pipeline Architecture

## Introduction

The goal of this project was to design and implement a comprehensive data engineering solution that automates the process of ingesting, transforming, and visualizing data. The pipeline is built using Azure services such as **Azure Data Factory**, **Azure Databricks**, and **Azure Data Lake Storage**, with a focus on scalability, automation, and data governance. By leveraging the **Medallion Architecture** (Bronze, Silver, Gold layers), we ensure a structured flow of data from raw ingestion to valuable insights.

---

## Architecture

<img src="Architecture" alt="Architecture" width="900"/>

---

## Architecture Overview

The architecture follows the **Medallion Architecture** pattern, designed to handle large-scale data processing tasks efficiently:

1. **Bronze Layer**: Raw data ingestion from on-prem SQL databases and external sources is stored in Azure Data Lake.
2. **Silver Layer**: Data transformations are applied using Azure Databricks (PySpark) to clean and format data, making it suitable for analytics.
3. **Gold Layer**: Final, analytics-ready data is stored for easy querying and consumption by tools like Azure Synapse and Power BI.

---

## Technologies

&#9702; **Azure Data Factory**: Orchestration and automation of data pipelines.  
&#9702; **Azure Databricks**: Efficient data transformation with scalable processing.  
&#9702; **Azure Data Lake Storage Gen2**: Scalable and secure data storage.  
&#9702; **Azure Synapse Analytics**: For big data and analytics processing.  
&#9702; **Power BI**: For visualization and reporting.  

---

## Dataset Used

The **AdventureWorksLT2017** database is a sample relational database provided by Microsoft, commonly used for demonstrating SQL Server capabilities. In this project, it serves as the source data for the ETL pipeline, hosted on an on-premises Microsoft SQL Server.

- Database link: [AdventureWorksLT2017](https://tinyurl.com/AdventureWorksLT2017)

---

## Data Model  

<img src="https://github.com/user-attachments/assets/294cf674-4577-428d-b97f-31d71364a743" alt="Data Model" width="900"/>

---

## Scripts for Project

1. **Storage Mount** - [storagemount.py](storagemount.py)  
2. **Bronze to Silver** - [bronzetosilver.py](bronzetosilver.py)  
3. **Silver to Gold** - [silvertogold.py](silvertogold.py)

---

## Project Details  

This project automates the entire data engineering workflow, transforming raw data into insights using Azure's powerful ecosystem. Below are the key steps involved in the pipeline:  

### 1. **Data Ingestion**  
- Configured **Azure Data Factory (ADF)** pipelines to extract data from the **AdventureWorksLT2017** SQL database.  
- Stored the ingested data in the **Bronze Layer** of Azure Data Lake Storage to preserve raw data for future transformations.  

### 2. **Data Transformation**  
- Utilized **Azure Databricks** to process data through the following layers:  
  - **Bronze to Silver**: Cleaned and transformed the data to ensure consistency and readability.  
  - **Silver to Gold**: Applied business rules and aggregations to create analytics-ready datasets.  

### 3. **Data Analysis and Visualization**  
- Loaded the transformed data into **Azure Synapse Analytics** for SQL querying and analytics.  
- Built interactive dashboards in **Power BI** to visualize key metrics and insights, enabling easy reporting and decision-making.  

---

## Conclusion  

This project demonstrates the power of leveraging Azure’s cloud services to design a scalable, efficient, and automated data pipeline. The **Medallion Architecture** ensures data quality, governance, and usability throughout the pipeline. By using **Azure Data Factory**, **Azure Databricks**, and other Azure tools in synergy, the solution provides an end-to-end framework for modern data engineering practices.

The experience gained from this project has significantly enhanced my understanding of cloud-based ETL processes and reinforced my ability to design enterprise-level data solutions. This project showcases the potential of Azure for automating and streamlining data workflows at scale.

---

Feel free to explore the code and project details above to understand the implementation and architecture.










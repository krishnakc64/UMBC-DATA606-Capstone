# Scalable Customer Segmentation Using PySpark and RFM Analysis on E-Commerce Transaction Data

DATA 606 Capstone Project  
University of Maryland, Baltimore County (UMBC)

Prepared for: Dr. Chaojie Wang  
Author: Krishna Chaithanya Reddy Kuncham

---

## Project Overview

This project focuses on scalable customer segmentation using PySpark and RFM (Recency, Frequency, Monetary) analysis on large-scale e-commerce transaction data. The project analyzes customer purchasing behavior and groups customers into different segments using machine learning clustering techniques.

PySpark was used to efficiently process large datasets and perform customer analytics in a distributed computing environment. The final project also includes a Streamlit dashboard for customer analysis and visualization.

---

## Repository Structure

- `app/` → Streamlit dashboard application files  
- `data/` → Dataset files split into multiple CSV parts  
- `docs/` → Project report, presentation, proposal, and supporting documents  
- `notebooks/` → Jupyter notebooks for EDA, RFM analysis, and clustering  
- `models/` → Saved clustering model files and outputs  

---

## Project Links

### GitHub Repository
https://github.com/krishnakc64/UMBC-DATA606-Capstone.git

### YouTube Presentation
https://youtu.be/n4QEHgzKg2g

### PowerPoint Presentation
https://github.com/krishnakc64/UMBC-DATA606-Capstone/blob/main/docs/Customer%20Segmentation%20with%20Pyspark.pptx

### Live Streamlit Application
https://github.com/krishnakc64/UMBC-DATA606-Capstone/blob/main/app/app.py

### Dataset :
https://github.com/krishnakc64/UMBC-DATA606-Capstone/tree/main/data

---

## Technologies Used

- Python
- PySpark
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Jupyter Notebook

---

## Machine Learning Techniques Used

- RFM Analysis
- Feature Engineering
- StandardScaler
- K-Means Clustering
- Elbow Method

---

## Final Model

K-Means clustering was used to segment customers based on Recency, Frequency, and Monetary values.

Customer groups identified:
- High-Value Customers
- Loyal Customers
- Average Customers
- Low-Engagement Customers

The clustering results helped analyze customer behavior patterns and business value.

---

## Streamlit Application Features

The application allows users to:

- Enter customer ID
- View customer cluster details
- Analyze customer RFM values
- View customer behavior insights
- Get business recommendations based on customer segments

---

## Dataset

Dataset used:
E-Commerce Behavior Dataset

Dataset Source:
https://www.kaggle.com/datasets/mkechinov/ecommerce-purchase-history-from-electronics-store
Dataset Details:
- Large-scale e-commerce transaction dataset
- Millions of customer interaction records
- Includes product, customer, and transaction information
- Dataset divided into smaller CSV files for easier upload and processing

---

## Exploratory Data Analysis

EDA was performed to understand:
- Customer purchasing behavior
- Popular product categories
- Brand preferences
- Seasonal purchasing patterns
- Transaction distribution
- Customer engagement trends

RFM metrics were generated to measure:
- Recency
- Frequency
- Monetary value

---

## Conclusion

This project demonstrates how PySpark and machine learning techniques can be used for scalable customer segmentation on large e-commerce datasets.

The project successfully performed:
- Large-scale data processing
- Customer behavior analysis
- RFM feature engineering
- Customer segmentation using clustering
- Streamlit dashboard development

The final results provide useful business insights that can help improve customer engagement, personalized marketing, and customer retention strategies.

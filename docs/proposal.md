# Scalable Customer Segmentation Using PySpark and RFM Analysis on E-Commerce Transaction Data

---

## Project Title:
Scalable Customer Segmentation Using PySpark and RFM Analysis on E-Commerce Transaction Data  

---

## Prepared for:
UMBC Data Science Master Degree Capstone  
Dr. Chaojie (Jay) Wang  

---

## Author Name:
Krishna Chaithanya Reddy Kuncham  

---

# 2. Background

---

## What is it about?

The current project is aimed at conducting a customer segmentation based on large scaled e-commerce transactional data which is processed through PySpark. The data is stored at the event level of customer interaction and is made up of customer interaction records with timestamps, user identifiers and product category information.

The essence of it is to process raw transactional logs into useful behavioral measures with the help of RFM analysis (Recency, Frequency, Monetary) and implement the method of clustering data to recognize specific customer groups.

This is unlike small-scale analytics projects because the study utilizes distributed computing in PySpark that can be used to simulate the real-world big data environment.

---

## Why does it matter?

Segmentation of customers is an important factor to business strategy and optimization of marketing. Segmentation helps companies to:

- Determine high value customers.  

- Detect churn-risk customers  

- Prepare custom marketing campaigns.  

- Increase the efficiency of the resource allocation.  

- Enhance customer lifetime value.  

---

## Research Questions

Are RFM measures effective in segmenting level of customer value?  

What is the relationship between recency and purchase frequency and customer clustering?  

Are clustering methods capable of identifying the high value, loyal, and at-risk customers?  

Is there an increase in the quality of segmentation when RFM is used with behavioral category data?  

---

# 3. Data

---

## Data Source

Variable: kz.csv (E-Commerce Transaction Dataset).

The sample consists of very extensive transactional event information of an online shopping site. It records the action of the user in detail i.e. viewing the products, adding cart items and buying.

The data is suitable to the customer behavior study and customer segmentation according to the RFM approach.

---

## Data Characteristics

Format: CSV  

- Size of Rows: 1,000,000+ transaction records.  

- Number of Columns: 9  

- Form: Event based transactional data.  

- Frame Work Processing: PySpark.  

- Data Type Structured behavioral logs.  

As the data set is greater than one million rows, the data is processed and aggregated with the help of PySpark.

---

## Column Names and Description.

| Column Name | Description |
|-------------|------------|
| event_time | Time of the event which took place. |
| event type | Event type (view, cart, purchase) |
| product_id | Product identifier, which is unique. |
| category_id | Category ID of product. |
| category_code | Name of product category. |
| brand | Name of the product brand. |
| price | Price of the product |
| user id | Customer identifier that is unique. |
| user_session | Session identifier of the user activity. |

---

# 4. RFM Modeling and feature engineering.

The data being event level will be aggregated into user level features.

---

## RFM Metrics

RFM measures will be calculated as follows:

Recency (R):  
The days in which the customer had last transacted.

Frequency (F):  
Total amount of transactions done by the customer.

Monetary (M):  
Sum of money spent by customer (in case price data exists).  
In the event that price is unavailable, monetary proxy based on frequency will be applied.

---

## Other Behavioral Patterns.

- Unique products categories.  

- The number of purchases by category.  

- Activity duration  

- Mean time in between optical reads.  

---

## After transformation:

One row will consist of one customer.  

The columns will correspond to each of the behavioral or RFM measures.  

The last dataset will be organized in tidy format to be clustered.  

---

## Exploratory Data Analysis (EDA)

PySpark will be used to do the Exploratory Data Analysis (EDA) on the data, and the Python visualization libraries will be used to test assumptions prior to modeling. The analysis will comprise schema and data type checks, timestamp conversion, and missing value treatment as well as the distribution analysis of RFM metrics. The most important insights, including the most popular products and frequency of transactions, will be investigated and the visualizations will consist of histograms of Recency, Frequency, and Monetary values and RFM heatmaps, top category charts, and cluster distribution plots.

---

# 6. Model Training

---

## Type of Learning

Unsupervised Learning -Clustering.

---

## Models to be Used

K-Means Clustering (Basemodel)

Could be compared to Hierarchical Clustering.

---

# 7. Trained Model Application.

---

- Input RFM metrics  

- Assign customer segment  

- Interpretation of the display segments.  

- Give marketing suggestions.  

---

## Examples of Segments Interpretations:

High R/HF/HM to Loyal value customers.  

Low R, Low F → At-Risk Customers  

High F, Low M Frequent Low-Spenders.  

This shows actual application of marketing analytics.

---

# 8. Conclusion

Customer segmentation is a very important aspect of eCommerce analytics since it allows a business to focus on certain groups of customers with specialised marketing tactics. This project shows how business organizations can derive actionable insights using the large data sets in eCommerce by using PySpark as a processing and analysis tool and spur growth and customer satisfaction.
```

# Scalable Customer Segmentation Using PySpark and RFM Analysis on E-Commerce Transaction Data

Prepared for UMBC Data Science Master Degree Capstone  
Instructor: Dr. Chaojie Wang  

Author: Krishna Chaithanya Reddy Kuncham  

GitHub Repository:  


PowerPoint Presentation:  

YouTube Video:  

---

# 1. Background

In the rapidly growing e-commerce industry, businesses generate huge amounts of customer transaction data every day. Understanding customer purchasing behavior is important for improving customer engagement, increasing sales, and developing effective marketing strategies.

Traditional customer analysis methods become difficult when dealing with large-scale datasets. To solve this problem, big data technologies such as PySpark can be used to process and analyze customer transaction data efficiently.

This project focuses on customer segmentation using PySpark and RFM (Recency, Frequency, Monetary) analysis on a large-scale e-commerce dataset. By grouping customers based on purchasing behavior, businesses can identify loyal customers, high-value customers, average customers, and low-engagement customers.

The project also applies machine learning clustering techniques to improve customer segmentation and provide business insights.

---

## Research Questions

- Can large-scale transaction data be effectively analyzed using PySpark?
- How useful is RFM analysis for customer segmentation?
- Which customer groups contribute the highest business value?
- Can clustering techniques improve customer understanding?
- How can businesses use customer segmentation for better marketing strategies?

---

# 2. Data

## Data Source

E-Commerce Behavior Dataset  

Kaggle Dataset:  

- https://www.kaggle.com/datasets/mkechinov/ecommerce-purchase-history-from-electronics-store
---

## Data Size and Shape

- Large-scale e-commerce transaction dataset
- Millions of customer interaction records
- Multiple product and customer-related features
- Dataset divided into smaller CSV files for easier storage and processing

---

## Unit of Analysis

Each row in the dataset represents a customer interaction or transaction event.

---

## Data Dictionary

| Column | Description |
|---|---|
| event_time | Timestamp of customer activity |
| event_type | Event type such as view, cart, or purchase |
| order_id | Unique order identifier |
| product_id | Product identifier |
| category_id | Product category identifier |
| category_code | Product category name |
| brand | Product brand |
| price | Product price |
| user_id | Customer identifier |
| user_session | Customer session identifier |

---

## Features Used

- Customer transaction history
- Purchase frequency
- Product price
- Product category
- Brand information
- Customer activity timestamps

---

# 3. Exploratory Data Analysis (EDA)

EDA was performed using PySpark, Pandas, and Matplotlib.

## Key Findings

- Electronics products were the most popular categories.
- Samsung was identified as the most preferred brand.
- Customer purchasing activity changed across different months.
- High-frequency customers contributed higher monetary value.
- Customer behavior showed clear segmentation patterns.

---

## Category-wise and Brand-wise Analysis

The project analyzed popular product categories and brands to understand customer preferences.

### Top 10 Categories by Count

<img width="577" height="277" alt="image" src="https://github.com/user-attachments/assets/8db8cf0a-3f4b-4e19-bada-915238de3c3a" />


### Top 10 Brands by Count

<img width="496" height="274" alt="image" src="https://github.com/user-attachments/assets/e0074ca5-acd5-439d-86ea-4e9f44777632" />


---

## User Behavior Over Time

Customer purchasing activity was analyzed monthly to identify trends and seasonal patterns.

### Number of Transactions per Month

<img width="354" height="245" alt="image" src="https://github.com/user-attachments/assets/ba60bcbe-f0d0-4ea4-8fd5-491424aa0099" />

### Purchases Distribution per Month

<img width="324" height="329" alt="image" src="https://github.com/user-attachments/assets/f69ab057-1304-4de3-80de-43b3082a2f24" />

---

## Correlation Analysis

Correlation analysis was performed between important variables such as:

- Recency
- Frequency
- Monetary value
- Product price

This helped understand relationships between customer purchasing patterns and spending behavior.

---

# 4. Data Preprocessing

Several preprocessing steps were performed before applying machine learning algorithms.

## Preprocessing Steps

- Converted timestamps into datetime format
- Removed invalid and missing records
- Filled missing price values
- Generated monthly transaction keys
- Prepared RFM metrics
- Standardized features for clustering

---

# 5. RFM Analysis

RFM analysis was used to measure customer behavior.

## RFM Metrics

### Recency
Measures how recently a customer made a purchase.

### Frequency
Measures how often a customer purchases products.

### Monetary
Measures how much money a customer spends.

These metrics help identify customer value and engagement levels.

---

# 6. Machine Learning Model

## Model Used

K-Means Clustering

---

## Training Approach

- Implemented using PySpark MLlib
- Used VectorAssembler for feature vectorization
- Applied StandardScaler for feature scaling
- Used K-Means clustering for customer segmentation

---

## Elbow Method

The elbow method was used to determine the optimal number of clusters.

### Elbow Method Graph

<img width="322" height="237" alt="image" src="https://github.com/user-attachments/assets/80348049-924e-461e-9777-d2001f7cd658" />


The graph indicated that k = 4 was the optimal number of clusters.

---

# 7. Cluster Analysis and Results

Customers were segmented into four clusters based on RFM values.

### Cluster Distribution

<img width="352" height="226" alt="image" src="https://github.com/user-attachments/assets/aea22d2f-144d-4707-8720-068ade762330" />


---

## Cluster 0: Low Potential Customers

### Description

- Low frequency
- Low spending
- Less customer engagement

### Business Strategy

- Personalized recommendations
- Promotional campaigns
- Re-engagement marketing

---

## Cluster 1: New Customers

### Description

- Recently joined customers
- Limited purchasing history

### Business Strategy

- Welcome offers
- Product suggestions
- Onboarding campaigns

---

## Cluster 2: High-Value Customers

### Description

- High spending customers
- Frequent purchases
- Strong engagement

### Business Strategy

- VIP rewards
- Loyalty programs
- Personalized premium recommendations

---

## Cluster 3: Average Customers

### Description

- Moderate spending and activity

### Business Strategy

- Customer retention campaigns
- Seasonal discounts
- Product recommendations

---

## Cluster Visualization

### Average Recency

<img width="301" height="229" alt="image" src="https://github.com/user-attachments/assets/848b0c21-e822-4ddc-8764-5bc0c46761c4" />


### Average Monetary Value

<img width="320" height="230" alt="image" src="https://github.com/user-attachments/assets/069caa5a-ba86-4c6d-b567-ac74a39c7fc0" />


### Average Frequency

<img width="302" height="222" alt="image" src="https://github.com/user-attachments/assets/0d178e4b-f988-4d9c-873c-58b9756cf1ca" />


---

# 8. Streamlit Application

A Streamlit dashboard was developed to visualize customer segmentation results.

## Features

- Customer ID input
- Customer cluster prediction
- RFM value display
- Customer behavior insights
- Business recommendations

The application allows businesses to quickly analyze customer behavior and identify valuable customer segments.

---

# 9. Conclusion

This project successfully demonstrated scalable customer segmentation using PySpark and RFM analysis on large-scale e-commerce transaction data.

## Key Outcomes

- Processed large-scale datasets using PySpark
- Applied RFM analysis for customer behavior analysis
- Performed customer segmentation using K-Means clustering
- Identified high-value and low-engagement customers
- Developed a Streamlit application for customer analysis

The project shows how machine learning and big data technologies can help businesses improve customer understanding and marketing strategies.

---

# 10. Limitations

- Large datasets required high computational resources
- K-Means clustering may not capture all customer behavior patterns
- Customer behavior changes over time were not fully modeled

---

# 11. Future Research Direction

- Apply advanced clustering algorithms
- Build real-time recommendation systems
- Use deep learning models for customer prediction
- Deploy the application on cloud platforms
- Improve dashboard visualization and analytics

---

# 12. References

- Kaggle E-Commerce Dataset
- PySpark Documentation
- Apache Spark MLlib Documentation
- Scikit-learn Documentation
- Streamlit Documentation

---

Report content prepared based on the uploaded project draft and analysis results. :contentReference[oaicite:0]{index=0}


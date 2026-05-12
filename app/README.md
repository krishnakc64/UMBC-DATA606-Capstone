# Customer Segmentation Dashboard using Streamlit

## Project Overview

This project is an interactive Streamlit dashboard developed as part of the Customer Segmentation using PySpark and RFM Analysis project.

The main goal of this dashboard is to help companies better understand customer behavior using RFM metrics and clustering techniques. Users can select a customer ID and instantly view customer insights such as spending behavior, purchase frequency, customer segment, and business recommendations.

The project combines data analysis, machine learning, and visualization into a simple and user-friendly interface.

---

## Features

The dashboard includes:

- Customer ID selection
- Customer cluster identification
- RFM metrics display
- Purchase and transaction history
- Top product categories
- Business recommendations based on customer segment
- Dataset summary in sidebar

---

## Technologies Used

- Python
- Streamlit
- Pandas
- PySpark
- K-Means Clustering
- RFM Analysis

---

## Files Required

```text
app.py
rfm_clusters_part_1.csv
rfm_clusters_part_2.csv
kz1.csv
requirements.txt
```

---

## How to Run the Project

### Step 1: Create Virtual Environment

```bash
python -m venv streamlit_env
```

### Step 2: Activate Environment

#### Windows

```bash
streamlit_env\Scripts\activate
```

#### Mac/Linux

```bash
source streamlit_env/bin/activate
```

---

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### Step 4: Run the Streamlit App

```bash
streamlit run app.py
```

---

## Dashboard Explanation

### Customer Overview

The dashboard displays important customer information such as:

- Customer cluster
- Recency
- Frequency
- Monetary value

These values help understand how active and valuable a customer is.

---

### Purchase History

The application also shows customer transaction details including:

- Total transactions
- Purchased products
- Product categories

This helps analyze customer purchasing behavior more clearly.

---

### Business Recommendations

Based on the customer cluster, the dashboard provides suggestions for companies.

Examples include:

- Loyalty programs
- Personalized offers
- VIP benefits
- Re-engagement campaigns
- Welcome offers for new customers

These recommendations can help businesses improve customer retention and marketing strategies.

---

## Cluster Information

### Cluster 0 — Low Potential Customers

Customers in this cluster show lower engagement and spending behavior.

### Cluster 1 — New Customers

These customers are recently active and still exploring products and services.

### Cluster 2 — High Value Customers

These are the most valuable customers with high spending and frequent purchases.

### Cluster 3 — Average Customers

Customers with moderate purchase frequency and spending behavior.

---

## Conclusion

This project demonstrates how customer segmentation can be transformed into an interactive business application using Streamlit.

By combining PySpark, RFM analysis, and clustering techniques, the dashboard helps businesses better understand customer behavior and make data-driven decisions for marketing and customer engagement.



import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    rfm = pd.read_csv("final_rfm_clusters.csv", dtype={"user_id": "string"})   # your processed data
    transactions = pd.read_csv("kz1.csv", dtype={"user_id": "string"})          # original dataset
    return rfm, transactions

rfm_df, txn_df = load_data()
import pandas as pd

def clean_user_id(col):
    def convert(x):
        if pd.isna(x):
            return None
        
        x = str(x).strip()
        
        # handle scientific notation safely
        try:
            if "e" in x.lower():
                x = format(float(x), ".0f")
        except:
            pass
        
        # remove trailing .0 (Excel issue)
        if x.endswith(".0"):
            x = x[:-2]
        
        return x

    return col.apply(convert)

rfm_df["user_id"] = clean_user_id(rfm_df["user_id"])
txn_df["user_id"] = clean_user_id(txn_df["user_id"])

cluster_info = {
    0: {
        "name": "Low Potential Customer",
        "actions": [
            "Offer targeted discounts to re-engage the customer",
            "Send personalized product recommendations",
            "Run email or ad campaigns to bring them back"
        ]
    },
    1: {
        "name": "New Customer",
        "actions": [
            "Provide welcome offers or first-time discounts",
            "Send onboarding emails to guide usage",
            "Highlight trending or popular products"
        ]
    },
    2: {
        "name": "High Value Customer",
        "actions": [
            "Provide VIP benefits and exclusive deals",
            "Offer early access to new products",
            "Recommend premium or complementary products"
        ]
    },
    3: {
        "name": "Average Customer",
        "actions": [
            "Introduce loyalty programs",
            "Send personalized promotions",
            "Encourage repeat purchases with offers"
        ]
    }
}


st.set_page_config(layout="wide")
st.title("🛍️ Customer Segmentation Dashboard")


common_ids = sorted(set(rfm_df["user_id"]).intersection(set(txn_df["user_id"])))

customer_id = st.selectbox(
    "Select Customer ID",
    common_ids
)

if customer_id:

    customer = rfm_df[rfm_df["user_id"] == str(customer_id)]

    if not customer.empty:
        cluster = int(customer["cluster"].values[0])
        recency = customer["Recency"].values[0]
        user_txn = txn_df[txn_df["user_id"] == customer_id]
        if "order_id" in user_txn.columns:
            frequency = user_txn["order_id"].nunique()
        else:
            frequency = len(user_txn)
        if "price" in user_txn.columns:
            monetary = user_txn["price"].sum()
        else:
            monetary = 0  
        st.subheader("📊 Customer Overview")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Cluster", cluster)
        col2.metric("Recency (days)", recency)
        col3.metric("Frequency", frequency)
        col4.metric("Monetary ($)", round(monetary, 2))

        st.success(f"Segment: {cluster_info[cluster]['name']}")
        st.subheader("🧾 Purchase History")
        st.write(f"Total Transactions: {len(user_txn)}")

        if not user_txn.empty:
            st.dataframe(user_txn.head(20))
            if "category_code" in user_txn.columns:
                st.subheader("📦 Top Categories")

                top_cat = user_txn["category_code"].value_counts().head(5)
                st.bar_chart(top_cat)
        st.subheader("💡 Business Recommendations")

        strategy = cluster_info.get(cluster)

        if strategy:
            st.info(f"Customer Segment: {strategy['name']}")

            st.write("### Suggested Actions:")
            for action in strategy["actions"]:
                st.write(f"- {action}")

        

    else:
        st.error("Customer not found")
st.sidebar.header("📊 Dataset Overview")

st.sidebar.write(f"Total Customers: {rfm_df['user_id'].nunique()}")
st.sidebar.write(f"Total Transactions: {len(txn_df)}")
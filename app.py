import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Customer Lifetime Value Engine",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Customer Lifetime Value Engine")
st.write(
    "Analyze customer purchasing behavior and estimate Customer Lifetime Value (CLV)."
)

# Sample customer dataset
data = {
    "Customer_ID": [
        "C001", "C002", "C003", "C004", "C005",
        "C006", "C007", "C008", "C009", "C010"
    ],
    "Purchase_Frequency": [12, 8, 15, 5, 10, 18, 6, 9, 14, 7],
    "Average_Order_Value": [1200, 850, 1500, 700, 1100, 1800, 650, 950, 1350, 800],
    "Customer_Lifespan_Years": [4, 3, 5, 2, 4, 6, 2, 3, 5, 3]
}

df = pd.DataFrame(data)

# Calculate CLV
df["Annual_Value"] = (
    df["Purchase_Frequency"] * df["Average_Order_Value"]
)

df["Customer_Lifetime_Value"] = (
    df["Annual_Value"] * df["Customer_Lifespan_Years"]
)

# Dataset
st.subheader("📊 Customer Dataset")
st.dataframe(df, use_container_width=True)

# Key metrics
st.subheader("📌 Business Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Average CLV",
    f"₹{df['Customer_Lifetime_Value'].mean():,.0f}"
)

col2.metric(
    "Highest CLV",
    f"₹{df['Customer_Lifetime_Value'].max():,.0f}"
)

col3.metric(
    "Lowest CLV",
    f"₹{df['Customer_Lifetime_Value'].min():,.0f}"
)

col4.metric(
    "Customers",
    len(df)
)

# Customer CLV chart
st.subheader("💰 Customer Lifetime Value")

fig, ax = plt.subplots()

ax.bar(
    df["Customer_ID"],
    df["Customer_Lifetime_Value"]
)

ax.set_xlabel("Customer")
ax.set_ylabel("Lifetime Value (₹)")
ax.set_title("Customer Lifetime Value")

plt.xticks(rotation=45)

st.pyplot(fig)

# Purchase frequency vs CLV
st.subheader("📈 Purchase Frequency vs Customer Lifetime Value")

fig2, ax2 = plt.subplots()

ax2.scatter(
    df["Purchase_Frequency"],
    df["Customer_Lifetime_Value"]
)

ax2.set_xlabel("Purchase Frequency")
ax2.set_ylabel("Customer Lifetime Value (₹)")
ax2.set_title("Purchase Frequency vs CLV")

st.pyplot(fig2)

# Customer segmentation
def segment_customer(clv):
    if clv >= 100000:
        return "High Value"
    elif clv >= 50000:
        return "Medium Value"
    else:
        return "Low Value"


df["Customer_Segment"] = df["Customer_Lifetime_Value"].apply(
    segment_customer
)

st.subheader("👥 Customer Segmentation")

segment_summary = (
    df["Customer_Segment"]
    .value_counts()
    .reset_index()
)

segment_summary.columns = ["Segment", "Number_of_Customers"]

st.dataframe(
    segment_summary,
    use_container_width=True
)

# Top customers
st.subheader("🏆 Top Customers by Lifetime Value")

top_customers = df.sort_values(
    "Customer_Lifetime_Value",
    ascending=False
)[
    [
        "Customer_ID",
        "Purchase_Frequency",
        "Average_Order_Value",
        "Customer_Lifespan_Years",
        "Customer_Lifetime_Value",
        "Customer_Segment"
    ]
].head(5)

st.dataframe(
    top_customers,
    use_container_width=True
)

# Formula
st.subheader("🧮 CLV Formula")

st.info(
    "Customer Lifetime Value = Purchase Frequency × "
    "Average Order Value × Customer Lifespan"
)

# Insights
st.subheader("💡 Key Insights")

highest_customer = df.loc[
    df["Customer_Lifetime_Value"].idxmax(),
    "Customer_ID"
]

highest_clv = df["Customer_Lifetime_Value"].max()

average_clv = df["Customer_Lifetime_Value"].mean()

st.write(
    f"• **{highest_customer}** has the highest estimated lifetime value "
    f"of **₹{highest_clv:,.0f}**."
)

st.write(
    f"• The average estimated customer lifetime value is "
    f"**₹{average_clv:,.0f}**."
)

st.write(
    "• Customers with higher purchase frequency can generate greater "
    "lifetime value when other factors remain similar."
)

st.write(
    "• Customer segmentation can help businesses identify high-value "
    "customers and plan targeted strategies."
)

st.success("✅ Customer Lifetime Value analysis completed!")
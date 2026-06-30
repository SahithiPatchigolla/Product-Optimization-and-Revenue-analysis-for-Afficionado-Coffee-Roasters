import streamlit as st
import pandas as pd
st.title("Coffee Product Optimization Dashboard")
st.write("Interactive analytics for revenue and product performance")
df=pd.read_csv("Afficionado Coffee Roasters.csv")
st.sidebar.header("Dashboard Filters")
category=st.sidebar.selectbox("Select Category",["All"]+list(df["product_category"].unique()))
if category !="All":
      df=df[df["product_category"]==category]
product_type=st.sidebar.selectbox("Select Product Type",["All"]+list(df["product_type"].unique()))
if product_type !="All":
      df=df[df["product_type"]==product_type]
store=st.sidebar.selectbox("Selet Store Location",["All"]+list(df["store_location"].unique()))
if store !="All":
    df=df[df["store_location"]==store]
top_n=st.sidebar.slider("Top N Products", min_value=5,max_value=20,value=10)
df["Revenue"]=df["transaction_qty"]*df["unit_price"]
st.dataframe(df.head())
top_products=(df.groupby("product_detail")["Revenue"].sum().sort_values(ascending=False).head(top_n))
st.subheader("Top 10 Products by Revenue")
st.bar_chart(top_products)
top_volume=(df.groupby("product_detail")["transaction_qty"].sum().sort_values(ascending=False).head(top_n))
st.subheader("Top 10 Products by Volume")
st.bar_chart(top_products)
category_revenue=(df.groupby("product_category")["Revenue"].sum().sort_values(ascending=False))
st.subheader("Category Revenue Distribution")
st.bar_chart(category_revenue)
import plotly.express as px
scatter_df=(df.groupby("product_detail").agg({"transaction_qty":"sum","Revenue":"sum"}).reset_index())
fig=px.scatter(scatter_df,x="transaction_qty",y="Revenue",hover_name="product_detail",title="Popularity vs Revenue")
st.plotly_chart(fig)
st.subheader("Product  Performance Table")
product_summary=(df.groupby("product_detail").agg({"transaction_qty":"sum", "Revenue":"sum"}).reset_index().sort_values("Revenue",ascending=False))
st.dataframe(product_summary)

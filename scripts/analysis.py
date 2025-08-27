
import streamlit as st

def run_summary(df):
    
    # Show sales insights
    if "total_sales" in df.columns:
        st.metric("💰 Total Sales", f"{df['total_sales'].sum():,.2f}")
        st.metric("📈 Average Sales", f"{df['total_sales'].mean():,.2f}")
        st.metric("🔝 Max Sales", f"{df['total_sales'].max():,.2f}")

    # Top 5 performing regions
    if "region" in df.columns:
        st.write("**Top Regions by Sales:**")
        st.dataframe(df.groupby("region")["total_sales"].sum().sort_values(ascending=False).head())
    
    # Top 5 performing products
    if "sub-category" in df.columns:
        st.write("**Top Products by Sales:**")
        st.dataframe(df.groupby("sub-category")["total_sales"].sum().sort_values(ascending=False).head())

    
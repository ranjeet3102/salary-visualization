import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def show_charts(df):
    df.columns = df.columns.str.strip().str.lower()

  
    if "region" in df.columns and "sales" in df.columns and "year" in df.columns:
        st.subheader("Sales by Region")
        years = df["year"].unique()
        cols = st.columns(2)   
        for i, yr in enumerate(sorted(years)):
            region_sales = df[df["year"]==yr].groupby("region")["sales"].sum()
            fig, ax = plt.subplots(figsize=(5, 3))  
            sns.barplot(x=region_sales.index, y=region_sales.values, palette="mako", ax=ax)
            ax.set_title(f"Year {yr}", fontsize=12)
            ax.set_xlabel("")
            ax.set_ylabel("Sales")

            with cols[i % 2]:
                st.pyplot(fig)
            if i % 2 == 1:  
                cols = st.columns(2)


    if "year" in df.columns and "month" in df.columns and "sales" in df.columns:
        st.subheader("Monthly Sales Trend")
        years = df["year"].unique()
        cols = st.columns(2)
        for i, yr in enumerate(sorted(years)):
            monthly_sales = df[df["year"]==yr].groupby("month")["sales"].sum()
            fig, ax = plt.subplots(figsize=(5, 3))  
            sns.lineplot(x=monthly_sales.index, y=monthly_sales.values, marker="o", ax=ax)
            ax.set_title(f"Year {yr}", fontsize=12)
            ax.set_xlabel("Month")
            ax.set_ylabel("Sales")

            with cols[i % 2]:
                st.pyplot(fig)
            if i % 2 == 1:
                cols = st.columns(2)

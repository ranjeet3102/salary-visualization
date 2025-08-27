import streamlit as st
import pandas as pd
import chardet
from scripts import data_preprocessing, analysis, visualization

st.set_page_config(page_title="📊 Sales Dashboard", layout="wide")
st.title("📊 Sales Data Dashboard")

def detect_encoding(file) -> str:
    raw_data = file.read(50000)
    file.seek(0) 
    result = chardet.detect(raw_data)
    return result["encoding"] if result["encoding"] else "utf-8"

uploaded_file = st.file_uploader("Upload a sales CSV file", type=["csv"])

if uploaded_file is not None:
    encoding = detect_encoding(uploaded_file)
    st.write(f"📂 Detected encoding: `{encoding}`")

    try:
        raw_df = pd.read_csv(uploaded_file, encoding=encoding)
    except Exception as e:
        st.error(f"❌ Error reading CSV: {e}")
        st.stop()

    st.success("✅ File uploaded successfully!")

    # --- Clean data ---
    df = data_preprocessing.clean_sales_data(
    raw_df, cleaned_file_path="data/cleaned_sales.csv")

    # --- Summary report ---
    st.subheader("📈 Summary Report")
    analysis.run_summary(df)

    # --- Visualizations ---
    st.subheader("📊 Visualizations")
    visualization.show_charts(df)

else:
    st.info("👆 Please upload a CSV file to get started.")

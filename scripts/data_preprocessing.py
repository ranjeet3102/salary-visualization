import pandas as pd

def clean_sales_data(df: pd.DataFrame, cleaned_file_path: str ) -> pd.DataFrame:
   
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    if "order_date" in df.columns:
        df['order_date'] = pd.to_datetime(df['order_date'], errors="coerce")

    if "region" in df.columns:
        df['region'] = df['region'].astype('category')

    if "quantity" in df.columns and "sales" in df.columns:
        df['total_sales'] = df.apply(
            lambda row: row['sales'] if row['quantity'] != 0 else 0, axis=1
        )

    if "order_date" in df.columns:
        df['year'] = df['order_date'].dt.year
        df['month'] = df['order_date'].dt.month
        df['day'] = df['order_date'].dt.day

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    if "total_sales" in df.columns:
        df = df[df['total_sales'] < df['total_sales'].quantile(0.99)]

    if cleaned_file_path:
        df.to_csv(cleaned_file_path, index=False)
        print(f"✅ Cleaned sales data saved at {cleaned_file_path}")

    return df

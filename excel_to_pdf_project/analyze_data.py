import pandas as pd
import os

def analyze_sales():
    # 1. Load the Data (Using safe path joining)
    current_folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_folder, "sales_data.xlsx")
    
    print("Loading data...")
    df = pd.read_excel(file_path)

    # -------- TOTAL REVENUE --------
    total_revenue = df['Total_Price'].sum()

    # -------- REGION ANALYSIS --------
    region_stats = df.groupby('Region')['Total_Price'].sum().sort_values(ascending=False)
    best_region_name = region_stats.index[0]
    best_region_sales = region_stats.iloc[0]

    # -------- PRODUCT ANALYSIS --------
    product_stats = df.groupby('Product')['Total_Price'].sum().sort_values(ascending=False)
    best_product_name = product_stats.index[0]
    best_product_sales = product_stats.iloc[0]

    # 4. Print Final Analysis Report
    print("-" * 40)
    print("         SALES ANALYSIS REPORT")
    print("-" * 40)

    print(f"Total Revenue:         ${total_revenue:,.2f}")
    print(f"Top Region:            {best_region_name} (${best_region_sales:,.2f})")
    print(f"Top Selling Product:   {best_product_name} (${best_product_sales:,.2f})")

    print("-" * 40)
    print("\nRegional Breakdown:")
    print(region_stats)

    print("\nProduct Breakdown:")
    print(product_stats)
    print("-" * 40)

if __name__ == "__main__":
    analyze_sales()

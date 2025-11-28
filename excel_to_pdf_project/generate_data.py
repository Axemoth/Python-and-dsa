import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_sales_data(num_rows=1000):
    # 1. Define Categories to pick from
    products = {
        'Laptop': 800.00,
        'Mouse': 25.50,
        'Monitor': 150.00,
        'Keyboard': 45.00,
        'HDMI Cable': 12.00,
        'Headset': 55.00
    }
    regions = ['North', 'South', 'East', 'West']
    sales_reps = ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan']

    # 2. Generate Random Data
    data = []
    
    # Start date: 1 year ago
    start_date = datetime.now() - timedelta(days=365)

    for _ in range(num_rows):
        # Pick a random product
        product_name = random.choice(list(products.keys()))
        base_price = products[product_name]
        
        # Add slight price variation (volatility) to make it realistic
        # Price varies by +/- 5%
        unit_price = round(base_price * random.uniform(0.95, 1.05), 2)
        
        # Random quantity (1 to 20)
        quantity = random.randint(1, 20)
        
        # Random date within the last year
        random_days = random.randint(0, 365)
        date = start_date + timedelta(days=random_days)
        
        # Compile row
        row = {
            'Date': date.strftime('%Y-%m-%d'),
            'Region': random.choice(regions),
            'Sales_Rep': random.choice(sales_reps),
            'Product': product_name,
            'Quantity': quantity,
            'Unit_Price': unit_price,
            'Total_Price': round(quantity * unit_price, 2)
        }
        data.append(row)

    # 3. Create DataFrame
    df = pd.DataFrame(data)

    # 4. Save to Excel
    filename = "sales_data.xlsx"
    df.to_excel(filename, index=False)
    print(f"✅ Success! Generated {num_rows} rows of data in '{filename}'")
    print(df.head()) # Preview the first few rows

if __name__ == "__main__":
    generate_sales_data()
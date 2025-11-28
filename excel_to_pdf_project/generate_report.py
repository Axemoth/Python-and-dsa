import pandas as pd
import os
import matplotlib.pyplot as plt
from fpdf import FPDF  # <--- The new library

class PDFReport(FPDF):
    """
    Custom PDF class to define a standard Header and Footer
    that appears on every page automatically.
    """
    def header(self):
        # Set font: Arial, Bold, 12pt
        self.set_font('Arial', 'B', 12)
        # Title
        self.cell(0, 10, 'Monthly Business Review', border=False, ln=True, align='C')
        # Line break
        self.ln(5)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def create_report():
    # ==========================
    # 1. SETUP & PATHS
    # ==========================
    current_folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_folder, "sales_data.xlsx")
    chart_file = os.path.join(current_folder, "sales_chart.png")
    pdf_file = os.path.join(current_folder, "Final_Report.pdf")

    print("1. Loading Data...")
    df = pd.read_excel(input_file)

    # ==========================
    # 2. ANALYTICS
    # ==========================
    print("2. Analyzing Data...")
    total_revenue = df['Total_Price'].sum()
    
    # Top Region
    region_stats = df.groupby('Region')['Total_Price'].sum().sort_values(ascending=False)
    top_region = region_stats.index[0]
    top_region_val = region_stats.iloc[0]

    # Top Product
    prod_stats = df.groupby('Product')['Total_Price'].sum().sort_values(ascending=False)
    top_product = prod_stats.index[0]
    top_product_val = prod_stats.iloc[0]

    # ==========================
    # 3. CHART GENERATION
    # ==========================
    print("3. Generating Chart...")
    df['Date'] = pd.to_datetime(df['Date'])
    monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Total_Price'].sum()

    plt.figure(figsize=(10, 5))
    monthly_sales.plot(kind='line', marker='o', color='green', linewidth=2)
    plt.title('Sales Trend (Last 12 Months)')
    plt.grid(True, linestyle='--')
    plt.tight_layout()
    plt.savefig(chart_file, dpi=100) # dpi=100 keeps file size low
    plt.close()

    # ==========================
    # 4. PDF ASSEMBLY
    # ==========================
    print("4. Building PDF...")
    
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    # -- Summary Section --
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Executive Summary', ln=True)
    pdf.ln(5) # Add 5mm vertical space

    pdf.set_font('Arial', '', 12)
    # Use multi_cell for paragraph text that wraps automatically
    summary_text = (
        f"This report covers the sales performance for the last fiscal year. "
        f"The total revenue generated was ${total_revenue:,.2f}.\n\n"
        f"The top performing region was {top_region} with sales of ${top_region_val:,.2f}. "
        f"The best-selling product category was {top_product}, generating ${top_product_val:,.2f}."
    )
    pdf.multi_cell(0, 8, summary_text)
    
    pdf.ln(10)

    # -- Chart Section --
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Sales Visualization', ln=True)
    
    # Insert Image: image(path, x, y, width)
    # w=180 means it takes up most of the A4 page width
    pdf.image(chart_file, x=15, w=180)

    # -- Save PDF --
    pdf.output(pdf_file)
    print(f"✅ SUCCESS! Report generated: {pdf_file}")

if __name__ == "__main__":
    create_report()
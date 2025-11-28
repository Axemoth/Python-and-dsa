import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import tempfile
import os

# ==========================================
# 1. DEFINE THE PDF CLASS (Same as before)
# ==========================================
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Monthly Business Review', border=False, ln=True, align='C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

# ==========================================
# 2. THE WEB APP UI
# ==========================================
st.title("📊 Automated Report Generator")
st.write("Upload your daily sales Excel file, and I will generate a PDF report for you.")

# A. The File Uploader
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    # B. Load Data
    df = pd.read_excel(uploaded_file)
    
    # Show a preview of the data on the webpage
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # C. Perform Analysis
    total_revenue = df['Total_Price'].sum()
    
    region_stats = df.groupby('Region')['Total_Price'].sum().sort_values(ascending=False)
    top_region = region_stats.index[0]
    
    prod_stats = df.groupby('Product')['Total_Price'].sum().sort_values(ascending=False)
    top_product = prod_stats.index[0]

    # Show Metrics nicely on top
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"${total_revenue:,.2f}")
    col2.metric("Top Region", top_region)
    col3.metric("Top Product", top_product)

    # D. Generate Chart (For the Web AND the PDF)
    st.subheader("Sales Trends")
    
    df['Date'] = pd.to_datetime(df['Date'])
    monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Total_Price'].sum()

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 5))
    monthly_sales.plot(kind='line', marker='o', color='green', linewidth=2, ax=ax)
    ax.set_title('Sales Trend')
    ax.grid(True, linestyle='--')
    
    # Show chart on website
    st.pyplot(fig)

    # ==========================================
    # 3. GENERATE PDF BUTTON
    # ==========================================
    if st.button("Generate PDF Report"):
        # We need a temporary place to save the image and PDF
        # because Streamlit runs on a server, not your local folder.
        with tempfile.TemporaryDirectory() as temp_dir:
            
            # 1. Save the chart image
            chart_path = os.path.join(temp_dir, "temp_chart.png")
            fig.savefig(chart_path, dpi=100)
            
            # 2. Build PDF
            pdf = PDFReport()
            pdf.add_page()
            
            # Summary
            pdf.set_font('Arial', 'B', 14)
            pdf.cell(0, 10, 'Executive Summary', ln=True)
            pdf.ln(5)
            
            pdf.set_font('Arial', '', 12)
            summary_text = (
                f"The total revenue generated was ${total_revenue:,.2f}. "
                f"The top performing region was {top_region}. "
                f"The best-selling product category was {top_product}."
            )
            pdf.multi_cell(0, 8, summary_text)
            pdf.ln(10)

            # Chart
            pdf.set_font('Arial', 'B', 14)
            pdf.cell(0, 10, 'Sales Visualization', ln=True)
            pdf.image(chart_path, x=15, w=180)

            # 3. Save PDF to temp file
            pdf_path = os.path.join(temp_dir, "report.pdf")
            pdf.output(pdf_path)

            # 4. Create Download Button
            # Read the PDF file as binary data
            with open(pdf_path, "rb") as f:
                pdf_data = f.read()
            
            st.download_button(
                label="📥 Download PDF",
                data=pdf_data,
                file_name="Sales_Report.pdf",
                mime="application/pdf"
            )
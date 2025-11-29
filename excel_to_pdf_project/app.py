import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import tempfile
import os

# ==========================================
# 1. HELPER: SMART HEADER DETECTION (NEW)
# ==========================================
def load_data_smartly(file):
    """
    Scans the first 10 rows to find the row with the most text columns.
    That row is likely the actual header.
    """
    # Read first 10 rows without assuming a header
    preview = pd.read_excel(file, header=None, nrows=10)
    
    best_row_idx = 0
    max_text_cols = 0
    
    # Loop through the rows to find the best candidate for a header
    for i, row in preview.iterrows():
        # Count how many cells in this row are Strings (text)
        # Headers are almost always text (e.g. "Date", "Price", "Region")
        text_count = row.apply(lambda x: isinstance(x, str)).sum()
        
        if text_count > max_text_cols:
            max_text_cols = text_count
            best_row_idx = i
            
    # Reload the file using the best row as the header
    return pd.read_excel(file, header=best_row_idx)

# ==========================================
# 2. HELPER: COLUMN TYPE DETECTION
# ==========================================
def detect_columns(df):
    cols = df.columns.tolist()
    
    # -- A. Detect Date --
    date_col = cols[0]
    possible_dates = []
    for c in cols:
        # Check if it's already datetime or looks like a date column name
        if pd.api.types.is_datetime64_any_dtype(df[c]):
            possible_dates.append(c)
        elif isinstance(c, str) and ("date" in c.lower() or "time" in c.lower()):
            possible_dates.append(c)
    if possible_dates:
        date_col = possible_dates[0]

    # -- B. Detect Value (Numeric) --
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    val_col = num_cols[0] if num_cols else None
    
    money_keywords = ['price', 'total', 'amount', 'revenue', 'sales', 'cost', 'qty', 'budget']
    for c in num_cols:
        if isinstance(c, str) and any(k in c.lower() for k in money_keywords):
            val_col = c
            break

    # -- C. Detect Category (Text) --
    obj_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    cat_col = obj_cols[0] if obj_cols else cols[0]
    
    cat_keywords = ['region', 'product', 'city', 'category', 'type', 'name', 'status', 'task']
    for c in obj_cols:
        if isinstance(c, str) and any(k in c.lower() for k in cat_keywords):
            cat_col = c
            break
            
    return date_col, val_col, cat_col

# ==========================================
# 3. PDF CLASS
# ==========================================
class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Project Analysis Report', border=False, ln=True, align='C')
        self.ln(5)
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

# ==========================================
# 4. MAIN APP
# ==========================================
st.set_page_config(page_title="Smart Excel Reporter", layout="wide")
st.title("🤖 Smart Excel Reporter (Header Fix)")
st.write("Upload any Excel file. I will fix the headers and generate a report.")

uploaded_file = st.file_uploader("Upload Excel File", type="xlsx")

if uploaded_file is not None:
    # --- STEP 1: LOAD SMARTLY ---
    try:
        df = load_data_smartly(uploaded_file)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        st.stop()
        
    # --- STEP 2: AUTO-DETECTION ---
    guessed_date, guessed_val, guessed_cat = detect_columns(df)
    
    all_cols = df.columns.tolist()
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

    if not numeric_cols:
        st.error("🚨 This file has no numeric columns found. Please check if your data is clean.")
        st.write("First 5 rows of what we read:")
        st.dataframe(df.head())
        st.stop()

    # Determine default indices
    try:
        date_idx = all_cols.index(guessed_date)
        cat_idx = all_cols.index(guessed_cat)
        val_idx = numeric_cols.index(guessed_val) if guessed_val in numeric_cols else 0
    except ValueError:
        date_idx = 0
        cat_idx = 0
        val_idx = 0

    st.write("### ⚙️ Configuration")
    c1, c2, c3 = st.columns(3)

    date_col = c1.selectbox("Date Column", all_cols, index=date_idx)
    category_col = c2.selectbox("Category Column", all_cols, index=cat_idx)
    value_col = c3.selectbox("Value Column", numeric_cols, index=val_idx)

    st.divider()

    # --- STEP 3: ANALYSIS ---
    # Safe Date Conversion
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df_clean = df.dropna(subset=[date_col])

    if df_clean.empty:
        st.warning(f"⚠️ The column '{date_col}' doesn't seem to have valid dates. Here is what the raw data looks like:")
        st.dataframe(df[date_col].head())
    else:
        # Calculations
        total_rev = df_clean[value_col].sum()
        top_cat = df_clean.groupby(category_col)[value_col].sum().sort_values(ascending=False)
        
        if not top_cat.empty:
            best_name = top_cat.index[0]
            best_val = top_cat.iloc[0]
        else:
            best_name = "N/A"
            best_val = 0

        # Metrics
        col1, col2 = st.columns(2)
        col1.metric("Total Sum", f"{total_rev:,.2f}")
        col2.metric(f"Top {category_col}", f"{best_name}")

        # Chart
        st.subheader("Trends Over Time")
        monthly_trend = df_clean.groupby(df_clean[date_col].dt.to_period('M'))[value_col].sum()
        
        fig, ax = plt.subplots(figsize=(8, 3))
        monthly_trend.plot(kind='line', ax=ax, marker='o')
        ax.set_title("Timeline")
        ax.grid(True, linestyle='--')
        st.pyplot(fig)

        # PDF Button
        if st.button("Download PDF Report"):
            with tempfile.TemporaryDirectory() as temp_dir:
                chart_path = os.path.join(temp_dir, "chart.png")
                fig.savefig(chart_path, dpi=100, bbox_inches='tight')
                
                pdf = PDFReport()
                pdf.add_page()
                
                pdf.set_font('Arial', 'B', 14)
                pdf.cell(0, 10, 'Executive Summary', ln=True)
                pdf.ln(5)
                
                pdf.set_font('Arial', '', 12)
                txt = (f"Analysis based on category: {category_col}.\n"
                       f"Total calculated value: {total_rev:,.2f}.\n"
                       f"Top performing group: {best_name} ({best_val:,.2f}).")
                pdf.multi_cell(0, 8, txt)
                pdf.ln(10)
                
                pdf.image(chart_path, x=10, w=190)
                
                pdf_out = os.path.join(temp_dir, "Smart_Report.pdf")
                pdf.output(pdf_out)
                
                with open(pdf_out, "rb") as f:
                    st.download_button("📥 Click to Download", f, "Smart_Report.pdf")
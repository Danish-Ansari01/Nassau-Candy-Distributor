import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Nassau Candy Profitability Dashboard", layout="wide")

st.title("🍬 Nassau Candy Distributor")
st.subheader("Product Line Profitability & Margin Performance Analysis")

# ===============================
# Load Data
# ===============================

@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\Danish\OneDrive\Desktop\Project\Data\Nassau Candy Distributor.csv")
    
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)
    
    df = df[df['Sales'] > 0]
    df = df[df['Units'] > 0]
    
    df['Gross Margin %'] = (df['Gross Profit'] / df['Sales']) * 100
    df['Profit per Unit'] = df['Gross Profit'] / df['Units']
    
    return df

df = load_data()

# ===============================
# Sidebar Filters
# ===============================

st.sidebar.header("Filters")

division_filter = st.sidebar.multiselect(
    "Select Division",
    df['Division'].unique(),
    default=df['Division'].unique()
)

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df['Order Date'].min(), df['Order Date'].max()]
)

margin_threshold = st.sidebar.slider(
    "Margin Threshold %",
    0,100,10
)

product_search = st.sidebar.text_input("Search Product")

# Apply filters

filtered_df = df[
    (df['Division'].isin(division_filter)) &
    (df['Order Date'] >= pd.to_datetime(date_range[0])) &
    (df['Order Date'] <= pd.to_datetime(date_range[1]))
]

if product_search:
    filtered_df = filtered_df[
        filtered_df['Product Name'].str.contains(product_search, case=False)
    ]

# ===============================
# KPI Metrics
# ===============================

total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Gross Profit'].sum()
avg_margin = filtered_df['Gross Margin %'].mean()
total_units = filtered_df['Units'].sum()

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales:,.0f}")
col2.metric("Total Profit", f"${total_profit:,.0f}")
col3.metric("Avg Margin %", f"{avg_margin:.2f}%")
col4.metric("Total Units Sold", f"{total_units:,.0f}")

st.divider()

# ===============================
# Product Profitability Overview
# ===============================

st.header("Product Profitability Overview")

product_analysis = filtered_df.groupby("Product Name").agg(
    Sales=("Sales","sum"),
    Profit=("Gross Profit","sum"),
    Units=("Units","sum")
).reset_index()

product_analysis["Margin %"] = product_analysis["Profit"] / product_analysis["Sales"] * 100

top_products = product_analysis.sort_values("Profit", ascending=False).head(10)

fig = px.bar(
    top_products,
    x="Profit",
    y="Product Name",
    orientation="h",
    title="Top 10 Profitable Products"
)

st.plotly_chart(fig,use_container_width=True)

# ===============================
# Division Performance Dashboard
# ===============================

st.header("Division Performance")

division_analysis = filtered_df.groupby("Division").agg(
    Sales=("Sales","sum"),
    Profit=("Gross Profit","sum")
).reset_index()

division_analysis["Margin %"] = division_analysis["Profit"] / division_analysis["Sales"] * 100

col1,col2 = st.columns(2)

fig1 = px.bar(
    division_analysis,
    x="Division",
    y="Sales",
    title="Revenue by Division"
)

col1.plotly_chart(fig1,use_container_width=True)

fig2 = px.bar(
    division_analysis,
    x="Division",
    y="Profit",
    title="Profit by Division"
)

col2.plotly_chart(fig2,use_container_width=True)

# ===============================
# Cost vs Margin Diagnostics
# ===============================

st.header("Cost vs Sales Diagnostics")

fig = px.scatter(
    filtered_df,
    x="Cost",
    y="Sales",
    size="Gross Profit",
    color="Division",
    hover_name="Product Name",
    title="Cost vs Sales Analysis"
)

st.plotly_chart(fig,use_container_width=True)

# ===============================
# Margin Distribution
# ===============================

st.header("Margin Distribution")

fig = px.histogram(
    filtered_df,
    x="Gross Margin %",
    nbins=30,
    title="Gross Margin Distribution"
)

st.plotly_chart(fig,use_container_width=True)

# ===============================
# Pareto Analysis
# ===============================

st.header("Profit Concentration (Pareto)")

pareto = product_analysis.sort_values("Profit", ascending=False)

pareto["Cumulative Profit"] = pareto["Profit"].cumsum()
pareto["Cumulative %"] = pareto["Cumulative Profit"] / pareto["Profit"].sum() * 100

fig = px.line(
    pareto,
    x=pareto.index,
    y="Cumulative %",
    title="Cumulative Profit Contribution"
)

st.plotly_chart(fig,use_container_width=True)

# ===============================
# Regional Sales
# ===============================

st.header("Regional Sales Performance")

region_sales = filtered_df.groupby("Region")["Sales"].sum().reset_index()

fig = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    title="Sales by Region"
)

st.plotly_chart(fig,use_container_width=True)

# ===============================
# Factory Map
# ===============================

# st.header("Factory Locations")

# factory_df = pd.read_csv("factories.csv")

# st.map(factory_df)

# st.success("Dashboard Loaded Successfully")
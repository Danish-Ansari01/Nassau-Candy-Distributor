# 🍬 Product Line Profitability & Margin Performance Analysis

### Nassau Candy Distributor – Data Analytics Project

---

# 📌 Project Overview

In distribution businesses, **high sales volume does not always mean high profitability**. Some products generate large revenue but contribute very little profit due to high manufacturing or operational costs.

This project analyzes the **profitability and margin performance of product lines** for **Nassau Candy Distributor**. The goal is to identify which products and divisions truly drive profit and which ones weaken overall margins.

The project converts raw order and financial data into **actionable business insights** using **Python, Exploratory Data Analysis (EDA), and an interactive Streamlit dashboard**.

---

# 🎯 Project Objectives

The main objectives of this project are:

- Identify **high-profit and high-margin products**
- Detect **high-sales but low-margin products**
- Evaluate **financial performance across product divisions**
- Understand **profit concentration across product lines**
- Diagnose **cost inefficiencies**
- Build an **interactive dashboard for business decision-making**

---

# 🗂 Dataset Description

The dataset contains **sales, customer, product, and financial data**.

| Field          | Description                |
| -------------- | -------------------------- |
| Row ID         | Unique row identifier      |
| Order ID       | Unique order identifier    |
| Order Date     | Date the order was placed  |
| Ship Date      | Date the order was shipped |
| Ship Mode      | Shipping method            |
| Customer ID    | Unique customer identifier |
| Country/Region | Customer location          |
| City           | Customer city              |
| State/Province | Customer state             |
| Postal Code    | Customer postal code       |
| Division       | Product division           |
| Region         | Customer region            |
| Product ID     | Unique product identifier  |
| Product Name   | Product name               |
| Sales          | Total sales revenue        |
| Units          | Quantity sold              |
| Gross Profit   | Profit generated from sale |
| Cost           | Manufacturing cost         |

---

# 🧹 Step 1 — Data Cleaning & Validation

Before analysis, the dataset must be cleaned to ensure accurate results.

### Cleaning Steps

1. Convert **Order Date and Ship Date** into datetime format.
2. Remove rows with:
   - Zero sales
   - Zero units

3. Handle missing values.
4. Standardize product and division labels.
5. Validate cost and profit values.

Example:

```python
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

df = df[df['Sales'] > 0]
df = df[df['Units'] > 0]
```

---

# 📊 Step 2 — Feature Engineering

Several important financial metrics were calculated.

### 1️⃣ Gross Margin %

Gross Margin measures how profitable a product is.

Formula:

Gross Margin (%) = (Gross Profit / Sales) × 100

```python
df['Gross Margin %'] = (df['Gross Profit'] / df['Sales']) * 100
```

---

### 2️⃣ Profit per Unit

Measures profitability per unit sold.

Profit per Unit = Gross Profit / Units

```python
df['Profit per Unit'] = df['Gross Profit'] / df['Units']
```

---

### 3️⃣ Revenue Contribution

Indicates how much each product contributes to total revenue.

Revenue Contribution (%) = Product Sales / Total Sales

---

### 4️⃣ Profit Contribution

Measures product contribution to total profit.

Profit Contribution (%) = Product Profit / Total Profit

---

# 📈 Step 3 — Exploratory Data Analysis (EDA)

EDA helps understand the **patterns, trends, and profitability behavior** of the dataset.

### Key Analyses Performed

#### 1️⃣ Sales Trend Analysis

Monthly sales trends help understand seasonal demand.

#### 2️⃣ Top Products by Sales

Identifies products generating the highest revenue.

#### 3️⃣ Top Products by Profit

Highlights the most profitable products.

#### 4️⃣ Margin Distribution

Shows how profitability varies across products.

#### 5️⃣ Cost vs Sales Analysis

Helps identify inefficient products.

Scatter plot interpretation:

| Scenario               | Meaning                  |
| ---------------------- | ------------------------ |
| High Cost + Low Sales  | Poor product performance |
| Low Cost + High Sales  | Efficient product        |
| High Cost + High Sales | Premium product          |

---

# 🏭 Step 4 — Division Performance Analysis

The dataset is grouped by **product divisions** to analyze business performance.

Metrics analyzed:

- Total revenue by division
- Total profit by division
- Average margin per division

This helps identify:

- **Strong divisions**
- **Divisions with margin problems**

---

# 📉 Step 5 — Profit Concentration (Pareto Analysis)

The Pareto Principle states that:

> **80% of profits often come from 20% of products**

Steps:

1. Sort products by profit.
2. Calculate cumulative profit.
3. Determine percentage contribution.

This helps detect:

- **profit concentration**
- **over-dependence on few products**

---

# 📊 Step 6 — Cost Structure Diagnostics

A scatter analysis of **Cost vs Sales** helps identify inefficient products.

Products flagged:

- High cost but low revenue
- Low margin despite high sales
- Products requiring price optimization

---

# 📊 Key Performance Indicators (KPIs)

| KPI                  | Description                     |
| -------------------- | ------------------------------- |
| Gross Margin %       | Profitability percentage        |
| Profit per Unit      | Profit generated per unit       |
| Revenue Contribution | Product share of total sales    |
| Profit Contribution  | Product share of total profit   |
| Margin Volatility    | Variability of margin over time |

---

# 🖥 Streamlit Dashboard

An interactive **Streamlit dashboard** was built to visualize the analysis.

## Dashboard Modules

### 1️⃣ Product Profitability Overview

Displays:

- Top profitable products
- Product margin leaderboard

---

### 2️⃣ Division Performance Dashboard

Shows:

- Revenue vs profit by division
- Margin comparison across divisions

---

### 3️⃣ Cost vs Sales Diagnostics

Scatter plots highlight:

- Cost-heavy products
- Margin risk products

---

### 4️⃣ Profit Concentration Analysis

Pareto charts identify:

- products generating most profit
- dependency risk

---

### 5️⃣ Regional Sales Analysis

Shows sales distribution across regions.

---

### 6️⃣ Factory Location Map

Displays manufacturing locations using geographic coordinates.

Factories:

| Factory           | Latitude  | Longitude   |
| ----------------- | --------- | ----------- |
| Lot's O' Nuts     | 32.881893 | -111.768036 |
| Wicked Choccy's   | 32.076176 | -81.088371  |
| Sugar Shack       | 48.11914  | -96.18115   |
| Secret Factory    | 41.446333 | -90.565487  |
| The Other Factory | 35.1175   | -89.971107  |

---

# 🧰 Technology Stack

| Tool                 | Purpose               |
| -------------------- | --------------------- |
| Python               | Data analysis         |
| Pandas               | Data processing       |
| NumPy                | Numerical computation |
| Matplotlib / Seaborn | Data visualization    |
| Plotly               | Interactive charts    |
| Streamlit            | Dashboard development |

---

# 📁 Project Structure

```
nassau-candy-profitability-analysis/
│
├── app.py
├── nassau_candy_dataset.csv
├── factories.csv
│
├── notebooks/
│   └── eda_analysis.ipynb
│
├── images/
│
└── README.md
```

---

# ▶ How to Run the Project

### Step 1 — Clone Repository

```
git clone https://github.com/your-username/nassau-candy-profitability-analysis
```

---

### Step 2 — Install Dependencies

```
pip install streamlit pandas numpy plotly seaborn matplotlib
```

---

### Step 3 — Run Dashboard

```
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

# 📊 Key Insights

Example insights from the analysis:

- A small number of products contribute the **majority of profit**
- Some high-revenue products generate **low margins**
- Certain divisions show **strong financial efficiency**
- Several products have **high manufacturing cost relative to revenue**

---

# 💡 Business Recommendations

### 1️⃣ Pricing Optimization

Increase prices for low-margin high-demand products.

### 2️⃣ Cost Reduction

Negotiate manufacturing or sourcing costs.

### 3️⃣ Product Portfolio Optimization

Consider discontinuing products with **low sales and low margins**.

### 4️⃣ Focus on High-Margin Products

Promote and prioritize high-margin product lines.

---

# 🚀 Future Improvements

Possible extensions of this project:

- Profit prediction using machine learning
- Customer segmentation analysis
- Demand forecasting models
- Supply chain optimization analysis

---

# 👨‍💻 Author

**Danish Ansari**

Frontend Developer & Data Science Enthusiast
Mumbai, India

Skills:

- Python
- Data Analysis
- React
- Data Visualization
- Streamlit Dashboards

---

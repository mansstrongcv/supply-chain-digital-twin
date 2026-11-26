import streamlit as st
import numpy as np
import plotly.express as px


st.set_page_config(page_title="Supply Chain Digital Twin", layout="wide")

st.title("📦 Multi-Echelon Supply Chain Digital Twin")
st.markdown("Stochastic Monte Carlo simulation engine for optimal safety stock and inventory management in retail.")

st.sidebar.header("Simulation Parameters")

avg_demand = st.sidebar.slider("Average Daily Demand (units)", min_value=10, max_value=200, value=50, step=5)
std_demand = st.sidebar.slider("Demand Volatility (Std Dev)", min_value=1, max_value=30, value=12, step=1)
avg_lead_time = st.sidebar.slider("Average Lead Time (days)", min_value=3, max_value=30, value=14, step=1)
std_lead_time = st.sidebar.slider("Lead Time Volatility (Std Dev)", min_value=1, max_value=10, value=4, step=1)

holding_cost = st.sidebar.number_input("Unit Holding Cost (KZT)", value=500)
stockout_cost = st.sidebar.number_input("Unit Stockout Penalty (KZT)", value=2500)

np.random.seed(42)
n_simulations = 10000

lead_times = np.random.normal(avg_lead_time, std_lead_time, n_simulations)
lead_times = np.maximum(1, np.round(lead_times)).astype(int)

demand_during_lead_time = []
for lt in lead_times:
    daily_sales = np.random.normal(avg_demand, std_demand, lt)
    daily_sales = np.maximum(0, daily_sales)
    demand_during_lead_time.append(np.sum(daily_sales))

demand_during_lead_time = np.array(demand_during_lead_time)

expected_demand = avg_demand * avg_lead_time
reorder_point = np.percentile(demand_during_lead_time, 95)
safety_stock = reorder_point - expected_demand

safety_stock_candidates = np.arange(0, 150, 5)
total_costs = []

for ss in safety_stock_candidates:
    h_cost = ss * holding_cost
    actual_stock = expected_demand + ss
    shortages = np.maximum(0, demand_during_lead_time - actual_stock)
    s_cost = np.mean(shortages) * stockout_cost
    total_costs.append(h_cost + s_cost)

optimal_safety_stock = safety_stock_candidates[np.argmin(total_costs)]

st.subheader("📊 Supply Chain Performance Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Expected Demand in Transit", f"{expected_demand:.0f} units")
col2.metric("Reorder Point (95% Service Level)", f"{reorder_point:.0f} units")
col3.metric("Optimal Safety Stock", f"{optimal_safety_stock} units", delta="Cost Minimized")


st.subheader("📈 Monte Carlo Scenario Stress-Test")
fig = px.histogram(
    x=demand_during_lead_time,
    nbins=50,
    labels={'x': 'Demand During Lead Time (units)', 'y': 'Scenario Count'},
    title="Distribution of 10,000 Simulated Lead-Time Demand Scenarios"
)
fig.add_vline(x=reorder_point, line_dash="dash", line_color="red", annotation_text="Reorder Point (95%)")
st.plotly_chart(fig, use_container_width=True)

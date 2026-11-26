import numpy as np

np.random.seed(42)
N_SIMULATIONS = 10000
AVG_DEMAND = 50
STD_DEMAND = 12
AVG_LEAD_TIME = 14
STD_LEAD_TIME = 4

lead_times = np.random.normal(AVG_LEAD_TIME, STD_LEAD_TIME, N_SIMULATIONS)
lead_times = np.maximum(1, np.round(lead_times)).astype(int)

demand_during_lead_time = []
for lt in lead_times:
    daily_sales = np.random.normal(AVG_DEMAND, STD_DEMAND, lt)
    daily_sales = np.maximum(0, daily_sales)
    demand_during_lead_time.append(np.sum(daily_sales))

demand_during_lead_time = np.array(demand_during_lead_time)

expected_demand = AVG_DEMAND * AVG_LEAD_TIME
reorder_point = np.percentile(demand_during_lead_time, 95)
safety_stock = reorder_point - expected_demand

print("=== SUPPLY CHAIN OPTIMIZATION RESULTS ===")
print(f"Expected Demand in Transit: {expected_demand:.0f} units.")
print(f"Reorder Point (95% Service Level): {reorder_point:.0f} units.")
print(f"Calculated Safety Stock: {safety_stock:.0f} units.")


HOLDING_COST_PER_UNIT = 500
STOCKOUT_COST_PER_UNIT = 2500


safety_stock_candidates = np.arange(0, 100, 5)
total_costs = []

for ss in safety_stock_candidates:
    holding_cost = ss * HOLDING_COST_PER_UNIT
    actual_stock_available = expected_demand + ss
    shortages = np.maximum(0, demand_during_lead_time - actual_stock_available)
    expected_shortage = np.mean(shortages)
    stockout_cost = expected_shortage * STOCKOUT_COST_PER_UNIT

    total_cost = holding_cost + stockout_cost
    total_costs.append(total_cost)


optimal_index = np.argmin(total_costs)
optimal_safety_stock = safety_stock_candidates[optimal_index]

print(f"Optimal Safety Stock (Cost Minimized): {optimal_safety_stock} units.")

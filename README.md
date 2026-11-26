📦 Multi-Echelon Supply Chain Digital Twin (Monte Carlo Simulation)
A stochastic Supply Chain Digital Twin and inventory optimization engine built with Python, NumPy, and Streamlit.
Designed for retail and distribution operations (calibrated for Central Asian logistics corridors with cross-border lead-time volatility), this system replaces static average-demand forecasting with a 10,000-scenario Monte Carlo simulation to compute cost-optimal Safety Stock and Reorder Points.
🎯 Problem & Motivation
Traditional inventory models rely on deterministic averages for daily sales and supplier delivery times. In real-world distribution—especially across cross-border supply routes (China, Russia, Europe)—both customer demand and customs/transit lead times are stochastic. Relying on static averages leads to two costly failure modes:
￼ Overstocking: Excess capital locked in slow-moving inventory and warehouse holding costs.
￼ Stockouts: Lost revenue and customer churn during demand spikes or border delays.
This project models lead-time demand as a probability distribution rather than a single point estimate, allowing supply chain managers to stress-test inventory policies against tail risks.
🖥️ Interactive Dashboard & Stress-Testing
1. Real-Time Inventory Optimization Overview
2. Stochastic Distribution of 10,000 Lead-Time Demand Scenarios
🧮 Mathematical & Engineering Architecture
1. Stochastic Lead-Time Demand Simulation (⁠simulation.py⁠):
￼ Generates ￼ independent trajectories using vectorized ⁠NumPy⁠ operations.
￼ Models daily sales volatility (￼ truncated at zero) compounded over stochastic supplier lead times (￼).
2. Service-Level vs. Cost-Minimization Optimization:
￼ Service-Level Reorder Point (ROP): Computes the 95th percentile of the simulated lead-time demand distribution to ensure a 95% cycle service level.
￼ Economic Cost-Optimal Safety Stock: Evaluates candidate safety stock levels by minimizing total expected inventory cost:


where ￼ is the unit holding cost and ￼ is the unit stockout penalty (calibrated in KZT).
3. Interactive Sensitivity Sandbox (⁠app.py⁠):
￼ Built in Streamlit with interactive sliders to simulate operational shocks (e.g., sudden transit delays, demand surges, or shifts in holding/stockout cost ratios).
📂 Repository Structure
🚀 Quick Start (Run Locally)
🛣️ Future Roadmap
￼ Probabilistic Demand Forecasting: Integrating quantile regression (⁠LightGBM⁠ with Quantile Loss) to feed non-stationary seasonal demand forecasts directly into the Monte Carlo engine.
￼ Multi-Echelon Network Expansion: Extending single-warehouse optimization to multi-tier regional distribution centers.
￼ Containerization: Adding a ⁠Dockerfile⁠ for one-click cloud deployment.

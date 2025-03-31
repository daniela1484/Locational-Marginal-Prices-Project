import pandas as pd
from pulp import LpProblem, LpMinimize, LpVariable, lpSum

# Simulated hourly demand profile (ex.)
time_intervals = pd.date_range(start="2025-03-31 00:00", periods=24, freq="h")
demand_profile = {t: 80 + (5 * (t.hour % 4)) for t in time_intervals} # example fluctuation

def calculate_lmp_multiple_intervals():
    results = []
    for t, demand in demand_profile.items():
        # Define problem
        problem = LpProblem("LMP_Calculation", LpMinimize)
    # Decision variables: Generator outputs
        gen_a = LpVariable("GenA_Output", lowBound=0, cat="Continuous")
        gen_b = LpVariable("GenB_Output", lowBound=0, cat="Continuous")
    # Objective: Minimize cost of generation
        problem += 20 * gen_a + 30 * gen_b
    # Demand constraint
        problem += gen_a + gen_b == demand

    # Generator capacity contraints
        problem += gen_a <= 60
        problem += gen_b <= 50

    # Solve optimization problem
        problem.solve()
    # Extract LMP (shadow price)
        lmp_value = problem.constraints["Total_Demand"].pi
        results.append((t, "Load1", lmp_value))

    return results

# Run LMP calculation
#lmp_values, output_a, output_b = calculate_lmp()
#print(f"LMPs: {lmp_values}")
#print(f"GenA Output: {output_a} MW, GenB Output: {output_b} MW")
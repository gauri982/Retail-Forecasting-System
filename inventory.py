import numpy as np

def calculate_inventory_params(demand_series, lead_time=7):

    # Average demand
    avg_demand = np.mean(demand_series)

    # Standard deviation
    std_demand = np.std(demand_series)

    # Service level (95%)
    z = 1.65

    # Safety Stock
    safety_stock = z * std_demand * np.sqrt(lead_time)

    # Reorder Point
    reorder_point = (avg_demand * lead_time) + safety_stock

    return avg_demand, safety_stock, reorder_point
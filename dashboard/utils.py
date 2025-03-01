from .models import SustainabilityReport
from datetime import datetime, timedelta
import random

def calculate_co2_savings():
    """Simulates CO₂ savings calculation based on renewable energy generation"""
    latest_report = SustainabilityReport.objects.last()

    # Simulate renewable energy generation and fossil fuel replacement
    total_energy_generated = random.uniform(100, 500)  # MW
    fossil_fuel_offset = total_energy_generated * 0.8  # 80% assumed replacement rate
    co2_reduction = fossil_fuel_offset * 0.45  # kg of CO2 saved per MW

    # Store in database
    SustainabilityReport.objects.create(
        total_energy_generated=total_energy_generated,
        fossil_fuel_offset=fossil_fuel_offset,
        co2_reduction=co2_reduction
    )
from .models import GridBalance
def update_grid_balance():
    """Simulates demand-supply balancing in the power grid"""
    energy_demand = random.uniform(200, 600)  # MW
    energy_supply = random.uniform(180, 620)  # MW

    GridBalance.objects.create(
        energy_demand=energy_demand,
        energy_supply=energy_supply
    )

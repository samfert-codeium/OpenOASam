"""
Analysis modules for wind plant operational assessment.

This package contains the core analysis classes for performing various operational
assessments on wind plant data. Each analysis class is designed to work with
PlantData objects and provides methods for running specific types of analyses.

Available Analysis Classes:
    MonteCarloAEP: Monte Carlo-based Annual Energy Production (AEP) estimation.
        Estimates long-term AEP using operational data and reanalysis products
        with uncertainty quantification through Monte Carlo simulation.

    TurbineLongTermGrossEnergy: Long-term turbine ideal energy estimation.
        Calculates the theoretical energy production if all turbines operated
        normally without downtime, derating, or severe underperformance.

    ElectricalLosses: Electrical losses analysis.
        Estimates average electrical losses by comparing turbine-level energy
        production to grid-delivered energy.

    EYAGapAnalysis: Energy Yield Assessment gap analysis.
        Compares pre-construction energy yield estimates with actual production
        to identify sources of performance differences.

    WakeLosses: Wake losses estimation.
        Estimates internal wake losses experienced by the wind plant and
        individual turbines.

    StaticYawMisalignment: Static yaw misalignment detection.
        Estimates static yaw misalignment for individual turbines as a function
        of wind speed.

Example:
    >>> from openoa.analysis import MonteCarloAEP, WakeLosses
    >>> from openoa import PlantData
    >>> plant = PlantData(metadata=my_metadata, scada=my_scada_data)
    >>> aep_analysis = MonteCarloAEP(plant)
    >>> aep_analysis.run(num_sim=1000)
"""

from openoa.analysis.aep import MonteCarloAEP
from openoa.analysis.wake_losses import WakeLosses
from openoa.analysis.eya_gap_analysis import EYAGapAnalysis
from openoa.analysis.yaw_misalignment import StaticYawMisalignment
from openoa.analysis.electrical_losses import ElectricalLosses
from openoa.analysis.turbine_long_term_gross_energy import TurbineLongTermGrossEnergy


__all__ = [
    "MonteCarloAEP",
    "TurbineLongTermGrossEnergy",
    "ElectricalLosses",
    "EYAGapAnalysis",
    "WakeLosses",
    "StaticYawMisalignment",
]

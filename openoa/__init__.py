"""
OpenOA: Open Operational Assessment Framework for Wind Plants.

OpenOA is a software framework written in Python for assessing wind plant performance
using operational assessment (OA) methodologies that consume time series data from
wind plants. The goal of the project is to provide an open source implementation of
common data structures, analysis methods, and utility functions relevant to wind
plant OA, while providing a platform to collaborate on new functionality.

This module provides the main entry point for the OpenOA library, exposing the
PlantData class and attaching analysis methods to it for convenient access.

Main Components:
    - PlantData: The primary data container class for wind plant operational data
    - MonteCarloAEP: Monte Carlo-based Annual Energy Production analysis
    - TurbineLongTermGrossEnergy: Long-term turbine ideal energy estimation
    - ElectricalLosses: Electrical losses analysis
    - EYAGapAnalysis: Energy Yield Assessment gap analysis
    - WakeLosses: Wake losses estimation
    - StaticYawMisalignment: Static yaw misalignment detection

Example:
    >>> import openoa
    >>> print(openoa.__version__)
    '3.1.3'
    >>> from openoa import PlantData
    >>> plant = PlantData(metadata=my_metadata, scada=my_scada_data)

Note:
    When bumping version, please be sure to also update parameters in sphinx/conf.py
"""

__version__ = "3.1.3"

from openoa.plant import PlantData


def __attach_methods() -> None:
    """
    Attach analysis methods to the PlantData class.

    This function dynamically attaches factory functions for various analysis
    methods to the PlantData class, allowing users to create analysis objects
    directly from a PlantData instance.

    The following methods are attached:
        - MonteCarloAEP: Creates a MonteCarloAEP analysis object
        - WakeLosses: Creates a WakeLosses analysis object
        - EYAGapAnalysis: Creates an EYAGapAnalysis analysis object
        - ElectricalLosses: Creates an ElectricalLosses analysis object
        - StaticYawMisalignment: Creates a StaticYawMisalignment analysis object
        - TurbineLongTermGrossEnergy: Creates a TurbineLongTermGrossEnergy analysis object

    Returns:
        None
    """
    from openoa.analysis.aep import create_MonteCarloAEP
    from openoa.analysis.wake_losses import create_WakeLosses
    from openoa.analysis.eya_gap_analysis import create_EYAGapAnalysis
    from openoa.analysis.yaw_misalignment import create_StaticYawMisalignment
    from openoa.analysis.electrical_losses import create_ElectricalLosses
    from openoa.analysis.turbine_long_term_gross_energy import create_TurbineLongTermGrossEnergy

    setattr(PlantData, "MonteCarloAEP", create_MonteCarloAEP)
    setattr(PlantData, "WakeLosses", create_WakeLosses)
    setattr(PlantData, "EYAGapAnalysis", create_EYAGapAnalysis)
    setattr(PlantData, "ElectricalLosses", create_ElectricalLosses)
    setattr(PlantData, "StaticYawMisalignment", create_StaticYawMisalignment)
    setattr(PlantData, "TurbineLongTermGrossEnergy", create_TurbineLongTermGrossEnergy)


__attach_methods()

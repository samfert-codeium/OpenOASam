"""
Utility modules for wind plant data processing and analysis.

This package provides a collection of utility functions and classes for
processing, filtering, and analyzing wind plant operational data. These
utilities are used internally by the analysis modules but can also be
used independently for general wind plant data analysis tasks.

Available Modules:
    filters: Functions for flagging data based on various criteria such as
        range checks, outlier detection, and unresponsive sensor detection.

    imputing: Methods for filling in missing data with imputed values using
        various interpolation and estimation techniques.

    timeseries: Time series manipulation utilities including resampling,
        gap filling, and frequency analysis.

    met_data_processing: Meteorological data processing functions including
        air density calculations, wind shear coefficients, and wind direction
        processing.

    power_curve: Power curve fitting and analysis tools including parametric
        and non-parametric curve fitting methods.

    plot: Convenient plotting functions for visualizing wind plant data,
        power curves, and analysis results.

    qa: Quality assurance methods for identifying potential data quality
        issues in SCADA data.

    unit_conversion: Unit conversion utilities for common wind energy
        measurements.

    downloader: Data downloading utilities for accessing reanalysis products
        and other external data sources.

    machine_learning_setup: Machine learning model configuration and setup
        utilities for regression analyses.

Example:
    >>> from openoa.utils import filters, timeseries
    >>> flagged_data = filters.range_flag(data, lower=0, upper=100)
    >>> resampled_data = timeseries.resample_data(data, freq="10min")
"""

"""
Schema definitions and metadata classes for wind plant data.

This package provides the data schema definitions and metadata classes used
to standardize wind plant operational data across different sources and formats.
The schema system enables validation, type checking, and consistent column
naming conventions throughout the OpenOA library.

Main Components:
    PlantMetaData: The top-level metadata container that holds all data type
        configurations for a wind plant dataset.

    SCADAMetaData: Metadata definition for SCADA (Supervisory Control and Data
        Acquisition) data including turbine-level measurements.

    MeterMetaData: Metadata definition for revenue meter data measuring
        grid-delivered energy.

    TowerMetaData: Metadata definition for meteorological tower measurements
        including wind speed, direction, and environmental conditions.

    StatusMetaData: Metadata definition for turbine operational status codes
        and availability information.

    CurtailMetaData: Metadata definition for curtailment data tracking
        energy losses due to grid constraints or other factors.

    AssetMetaData: Metadata definition for asset information including
        turbine locations, specifications, and identifiers.

    ReanalysisMetaData: Metadata definition for reanalysis products like
        ERA5 and MERRA2 providing long-term wind resource data.

    ANALYSIS_REQUIREMENTS: Dictionary defining the data requirements for
        each analysis type.

Utility Functions:
    create_schema: Generate a complete schema dictionary for all data types.
    create_analysis_schema: Generate a schema filtered for specific analysis types.

Mixins:
    FromDictMixin: Mixin class enabling instantiation from dictionaries.
    ResetValuesMixin: Mixin class for resetting object values to defaults.

Example:
    >>> from openoa.schema import PlantMetaData, SCADAMetaData
    >>> scada_meta = SCADAMetaData(
    ...     time="timestamp",
    ...     asset_id="turbine_id",
    ...     WMET_HorWdSpd="wind_speed",
    ...     WTUR_W="power"
    ... )
    >>> plant_meta = PlantMetaData(scada=scada_meta)
"""

from openoa.schema.schema import create_schema, create_analysis_schema
from openoa.schema.metadata import (
    ANALYSIS_REQUIREMENTS,
    AssetMetaData,
    FromDictMixin,
    MeterMetaData,
    PlantMetaData,
    SCADAMetaData,
    TowerMetaData,
    StatusMetaData,
    CurtailMetaData,
    ResetValuesMixin,
    ReanalysisMetaData,
)


__all__ = [
    "create_schema",
    "create_analysis_schema",
    "ANALYSIS_REQUIREMENTS",
    "AssetMetaData",
    "FromDictMixin",
    "MeterMetaData",
    "PlantMetaData",
    "SCADAMetaData",
    "TowerMetaData",
    "StatusMetaData",
    "CurtailMetaData",
    "ResetValuesMixin",
    "ReanalysisMetaData",
]

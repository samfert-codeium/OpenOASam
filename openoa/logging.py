"""
Logging utilities for OpenOA.

This module provides logging configuration and decorator utilities for the OpenOA
library. It includes functions for setting up logging configuration from JSON files
or environment variables, as well as decorators for automatically logging method
and function calls.

The module supports:
    - JSON-based logging configuration
    - Environment variable-based configuration override
    - Debug-level logging decorators for methods and functions
    - Dynamic log level adjustment

Example:
    >>> from openoa.logging import setup_logging, set_log_level
    >>> setup_logging(level="DEBUG")
    >>> set_log_level("INFO")
"""

from __future__ import annotations

import os
import json
import logging
import logging.config
from typing import Any, TypeVar, Callable
from pathlib import Path
from functools import wraps


F = TypeVar("F", bound=Callable[..., Any])


def setup_logging(
    console: bool = True,
    level: str = "WARNING",
    configuration: str = "logging.json",
    env_key: str = "LOG_CFG",
) -> None:
    """
    Set up logging configuration for the OpenOA library.

    This function configures the Python logging system either from a JSON
    configuration file or using basic configuration with the specified level.
    The configuration file path can be overridden using an environment variable.

    Args:
        console (bool): Whether to output logs to the console. Defaults to True.
            Note: This parameter is currently not used but reserved for future use.
        level (str): The default logging level. Must be one of 'DEBUG', 'INFO',
            'WARNING', 'ERROR', or 'CRITICAL'. Defaults to 'WARNING'.
        configuration (str): Path to the JSON logging configuration file.
            Defaults to 'logging.json'.
        env_key (str): Environment variable name that can override the
            configuration file path. Defaults to 'LOG_CFG'.

    Returns:
        None

    Example:
        >>> setup_logging(level="DEBUG")
        >>> setup_logging(configuration="/path/to/custom_logging.json")
    """
    if (value := os.getenv(env_key, None)) is not None:
        configuration = value
    configuration = Path(configuration).resolve()
    if configuration.is_file():
        with configuration.open("rt") as f:
            logging.config.dictConfig(json.loads(f), level=level)
    else:
        logging.basicConfig(level=level)

    logging.captureWarnings(True)


def logged_method_call(the_method: F, msg: str = "call") -> F:
    """
    Decorator that logs method calls at DEBUG level.

    This decorator wraps a method to automatically log when it is called,
    including the class name, instance ID, and method name. Useful for
    debugging and tracing method execution flow.

    Args:
        the_method (Callable): The method to be decorated.
        msg (str): Additional message to include in the log entry.
            Defaults to 'call'.

    Returns:
        Callable: The wrapped method with logging functionality.

    Example:
        >>> class MyClass:
        ...     @logged_method_call
        ...     def my_method(self, x):
        ...         return x * 2
    """

    @wraps(the_method)
    def _wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
        logger = logging.getLogger(the_method.__module__)
        logger.debug(f"{self.__class__.__name__}#{id(self)}.{the_method.__name__}: {msg}")
        return the_method(self, *args, **kwargs)

    _wrapper.__doc__ = the_method.__doc__
    return _wrapper  # type: ignore[return-value]


def logged_function_call(the_function: F, msg: str = "call") -> F:
    """
    Decorator that logs function calls at DEBUG level.

    This decorator wraps a function to automatically log when it is called,
    including the function name. Useful for debugging and tracing function
    execution flow.

    Args:
        the_function (Callable): The function to be decorated.
        msg (str): Additional message to include in the log entry.
            Defaults to 'call'.

    Returns:
        Callable: The wrapped function with logging functionality.

    Example:
        >>> @logged_function_call
        ... def my_function(x):
        ...     return x * 2
    """

    @wraps(the_function)
    def _wrapper(*args: Any, **kwargs: Any) -> Any:
        logger = logging.getLogger(the_function.__module__)
        logger.debug(f"{the_function.__name__}: {msg}")
        return the_function(*args, **kwargs)

    return _wrapper  # type: ignore[return-value]


def set_log_level(value: str) -> str:
    """
    Update the logging level for the root logger.

    This function allows dynamic adjustment of the logging level at runtime.
    It validates the input against the standard Python logging levels.

    Args:
        value (str): The desired logging level. Must be one of 'DEBUG', 'INFO',
            'WARNING', 'ERROR', or 'CRITICAL'.

    Returns:
        str: The logging level that was set.

    Raises:
        ValueError: If the provided value is not a valid logging level.

    Example:
        >>> set_log_level("DEBUG")
        'DEBUG'
        >>> set_log_level("INFO")
        'INFO'
    """
    valid = ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL")
    if value not in valid:
        raise ValueError(f"`log_level` is invalid. Please use one of: {valid}")
    logging.getLogger().setLevel(value)
    return value

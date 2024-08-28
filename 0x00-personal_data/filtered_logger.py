#!/usr/bin/env python3
"""
This module provides a function to filter and obfuscate sensitive data
in log messages.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message with specified fields obfuscated.

    Args:
        fields (List[str]): List of strings representing all fields to obfuscate.
        redaction (str): String representing by what the field will be obfuscated.
        message (str): String representing the log line.
        separator (str): String representing by which character is separating all fields in the log line.

    Returns:
        str: The log message with the specified fields obfuscated.
    """
    return re.sub(f"({'|'.join(fields)})=[^{separator}]+", lambda m: f"{m.group(1)}={redaction}", message)

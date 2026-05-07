"""Scrapling - A powerful, flexible web scraping library.

Scrapling provides a high-level interface for web scraping with support
for both static and dynamic content, smart element detection, and
automatic adaptation to website changes.
"""

__version__ = "0.2.9"
__author__ = "D4Vinci"
__license__ = "MIT"

from scrapling.core.fetchers import (
    Fetcher,
    AsyncFetcher,
    PlayWrightFetcher,
    StealthyFetcher,
)
from scrapling.core.page import Page
from scrapling.core.element import Element
from scrapling.core.storage import StorageSystem

__all__ = [
    "Fetcher",
    "AsyncFetcher",
    "PlayWrightFetcher",
    "StealthyFetcher",
    "Page",
    "Element",
    "StorageSystem",
    "__version__",
]

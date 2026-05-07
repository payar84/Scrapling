"""Scrapling - A powerful, flexible web scraping library.

Scrapling provides a high-level interface for web scraping with support
for both static and dynamic content, smart element detection, and
automatic adaptation to website changes.

Personal fork notes:
- Using this for learning purposes and personal scraping projects
- See upstream: https://github.com/D4Vinci/Scrapling
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

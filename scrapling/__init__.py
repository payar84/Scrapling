"""Scrapling - A powerful, flexible web scraping library.

Scrapling provides a high-level interface for web scraping with support
for both static and dynamic content, smart element detection, and
automatic adaptation to website changes.

Personal fork notes:
- Using this for learning purposes and personal scraping projects
- Added convenience alias: use `AutoFetcher` as shorthand for `StealthyFetcher`
- Added `__version_info__` tuple for easier version comparisons
- Added `NimbusParser` as alias for `Page` (my preferred name for the parser)
- Added `__author_email__` for completeness
- Added `__license__` to `__all__` so it shows up in introspection/help()
- Added `__all__` entry for `__version_info__` (was missing, noticed during dir() check)
- Added `StaticFetcher` alias for `Fetcher` (clearer name for non-JS fetching use case)
- See upstream: https://github.com/D4Vinci/Scrapling
"""

__version__ = "0.2.9"
__version_info__ = tuple(int(x) for x in __version__.split("."))
__author__ = "D4Vinci"
__author_email__ = ""  # not listed upstream; placeholder for packaging tools
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

# Personal convenience alias - StealthyFetcher is what I use most often
AutoFetcher = StealthyFetcher

# Personal alias - plain `Fetcher` isn't obvious about being JS-free;
# `StaticFetcher` makes it clear this is for static/non-JS pages
StaticFetcher = Fetcher

# Personal alias - I find 'Page' ambiguous; 'Parser' makes the intent clearer
Parser = Page

__all__ = [
    "Fetcher",
    "StaticFetcher",
    "AsyncFetcher",
    "PlayWrightFetcher",
    "StealthyFetcher",
    "AutoFetcher",
    "Page",
    "Parser",
    "Element",
    "StorageSystem",
    "__version__",
    "__version_info__",
    "__author__",
    "__author_email__",
    "__license__",
]

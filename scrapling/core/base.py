"""Base classes and core abstractions for Scrapling.

This module provides the foundational building blocks used throughout
the Scrapling library, including the base fetcher interface and
common utilities shared across different scraping backends.
"""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Union

logger = logging.getLogger(__name__)


class BaseConfig:
    """Holds common configuration options for all fetchers."""

    DEFAULT_TIMEOUT = 60  # increased from 30s; many sites are slow to respond
    DEFAULT_RETRIES = 3
    DEFAULT_DELAY = 2.0  # bumped from 1.0s to be more polite / avoid rate-limiting

    def __init__(
        self,
        timeout: int = DEFAULT_TIMEOUT,
        retries: int = DEFAULT_RETRIES,
        delay: float = DEFAULT_DELAY,
        headers: Optional[Dict[str, str]] = None,
        proxies: Optional[Union[str, Dict[str, str]]] = None,
        follow_redirects: bool = True,
        verify_ssl: bool = True,
    ):
        self.timeout = timeout
        self.retries = retries
        self.delay = delay
        self.headers = headers or {}
        self.proxies = proxies
        self.follow_redirects = follow_redirects
        self.verify_ssl = verify_ssl

    def to_dict(self) -> Dict[str, Any]:
        """Serialize config to a plain dictionary."""
        return {
            "timeout": self.timeout,
            "retries": self.retries,
            "delay": self.delay,
            "headers": self.headers,
            "proxies": self.proxies,
            "follow_redirects": self.follow_redirects,
            "verify_ssl": self.verify_ssl,
        }


class BaseFetcher(ABC):
    """Abstract base class that all Scrapling fetcher backends must implement.

    Subclasses should implement :meth:`fetch` to perform the actual HTTP
    request and return a response object compatible with the rest of the
    Scrapling API.
    """

    def __init__(self, config: Optional[BaseConfig] = None):
        self.config = config or BaseConfig()
        self._session: Any = None

    @abstractmethod
    def fetch(self, url: str, **kwargs: Any) -> Any:
        """Fetch the given URL and return a parsed response.

        Parameters
        ----------
        url:
            The target URL to retrieve.
        **kwargs:
            Additional keyword arguments forwarded to the underlying
            HTTP client (e.g. custom headers, cookies).

        Returns
        -------
        Any
            A Scrapling response/page object.

        Raises
        ------
        NotImplementedError
            If the subclass has not implemented this method.
        ValueError
            If ``url`` is an empty string or not a string at all.
        """
        raise NotImplementedError

    def close(self) -> None:
        """Release any resources held by the fetcher (e.g. open sessions)."""
        if self._session is not None:
            try:
                # Some HTTP clients expose a .close() method; others use a
                # context manager. Try .close() first, then fall back silently.
                self._session.close()
            except AttributeError:
                logger.debug(
                    "Session object %r has no close() method; skipping.",
                    self._session,
                )
            finally:
                self._session = None

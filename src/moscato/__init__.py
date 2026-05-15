"""
A drop-in asyncio-compatible replacement for `moto`'s `mock_aws()` function,
for mocking `aiobotocore`
"""

__version__: str = "0.2.0"

__all__ = ["mock_aws"]

from .async_mocker import mock_aws

import pycountry
from typing import Final, Tuple, Iterator

__all__ = ["COUNTRIES_TUPLES", "COUNTRIES_ISO2_TUPLES", "COUNTRIES_ISO3_TUPLES"]

COUNTRIES_ISO3_TUPLES: Final[Iterator[Tuple[str, str]]] = (
    (c.alpha_3, c.name) for c in pycountry.countries
)
"""
A tuple of tuples containing the ISO 3166-1 alpha-3 code and the country name.
"""

COUNTRIES_TUPLES = COUNTRIES_ISO3_TUPLES

COUNTRIES_ISO2_TUPLES: Final[Iterator[Tuple[str, str]]] = (
    (c.alpha_2, c.name) for c in pycountry.countries
)
"""
A tuple of tuples containing the ISO 3166-1 alpha-2 code and the country name.
"""

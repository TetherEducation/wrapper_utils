from typing import Final, Tuple, Iterator
from utils.lookup import all_countries

__all__ = ["COUNTRIES_TUPLES", "COUNTRIES_ISO2_TUPLES", "COUNTRIES_ISO3_TUPLES"]

COUNTRIES_ISO3_TUPLES: Final[Iterator[Tuple[str, str]]] = (
    (c.iso.alpha_3, c.name) for c in all_countries()
)
"""
A tuple of tuples containing the ISO 3166-1 alpha-3 code and the country name.
"""

COUNTRIES_TUPLES = COUNTRIES_ISO3_TUPLES

COUNTRIES_ISO2_TUPLES: Final[Iterator[Tuple[str, str]]] = (
    (c.iso.alpha_2, c.name) for c in all_countries()
)
"""
A tuple of tuples containing the ISO 3166-1 alpha-2 code and the country name.
"""
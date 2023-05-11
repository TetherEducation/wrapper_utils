from iso3166 import countries
from typing import Final, Tuple, Iterator

__all__ = ["COUNTRIES_TUPLES"]

COUNTRIES_TUPLES: Final[Iterator[Tuple[str, str]]] = (
    (c.alpha3, c.name) for c in countries
)

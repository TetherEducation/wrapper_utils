from iso3166 import countries
from typing import Final, Tuple, Iterator

COUNTRIES_TUPLES: Final[Iterator[Tuple[str, str]]] = (
    (c.alpha3, c.name) for c in countries
)

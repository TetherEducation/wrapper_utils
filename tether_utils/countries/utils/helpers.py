from typing import Literal, Union
from pycountry import countries
from pycountry.db import Country
from tether_utils.countries.exceptions import CountryValidationException

__all__ = ["get_pycountry_data", "get_country_code", "validate_country_string"]


def get_pycountry_data(country: Union[str, int]) -> Country:
    try:
        return countries.lookup(country)
    except LookupError:
        return None
        


def get_country_code(country: Union[str, int], iso_format: Literal['alpha_2', 'alpha_3'] = 'alpha_3') -> str:
    """
    Get the country code from the country name

    Args:
        `country (str or int)`: The country name or code as defined in ISO 3166-1
        `iso_format (str)`: The format to return the country code in.

        Valid country fields are:\n
        \t- Alpha-2 code (e.g. "TW")
        \t- Alpha-3 code (e.g. "TWN")
        \t- Numeric code (e.g. "156")
        \t- Name (e.g. "Taiwan, Province of China")
        \t- Apolitical name (e.g. "Taiwan")

    Returns:
        `str`: The country code as defined in ISO 3166-1 alpha-2 or alpha-3 (depending on the `iso_format` parameter)
    """
    country = get_pycountry_data(country)
    if country is None:
        return None
    return getattr(country, iso_format)


def validate_country_string(country: str) -> str:
    """
    Validate that a country code is any valid ISO 3166-1 code

    Args:
        `country (str)`: A string to validate as a country

    Returns:
        `str`: The country code as defined in ISO 3166-1 alpha-3

    Raises:
        `CountryValidationException`: If the country code is invalid
    """
    country_code = get_country_code(country)
    if country_code is None:
        raise CountryValidationException(country)
    return country_code

from typing import Union
from iso3166 import countries
from tether_utils.countries.exceptions import CountryValidationException


def get_country_code(country: Union[str, int]) -> str:
    """
    Get the country code from the country name

    Args:
        `country (str or int)`: The country name or code as defined in ISO 3166-1

        Valid formats are:\n
        \t- Alpha-2 code (e.g. "TW")
        \t- Alpha-3 code (e.g. "TWN")
        \t- Numeric code (e.g. "156")
        \t- Name (e.g. "Taiwan, Province of China")
        \t- Apolitical name (e.g. "Taiwan")

    Returns:
        `str`: The country code as defined in ISO 3166-1 alpha-3
    """
    country = countries.get(country, None)
    if country is None:
        return None
    return country.alpha3


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

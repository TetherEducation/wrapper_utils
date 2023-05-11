from rest_framework.exceptions import ValidationError

__all__ = ["CountryValidationException"]


class CountryValidationException(ValidationError):
    def __init__(self, country: str):
        super().__init__(f"Invalid country code: {country}")

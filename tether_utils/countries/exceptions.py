from rest_framework.exceptions import ValidationError


class CountryValidationException(ValidationError):
    def __init__(self, country: str):
        super().__init__(f"Invalid country code: {country}")

from rest_framework import serializers
from tether_utils.countries.utils import get_country_code


class CountryCharFieldSerializer(serializers.CharField):
    def to_internal_value(self, data: str) -> str:
        country = get_country_code(data)
        if country is None:
            raise serializers.ValidationError(f"Invalid country code: {data}")
        return country

    def to_representation(self, value: str) -> str:
        return value

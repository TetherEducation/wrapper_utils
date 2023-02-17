from .SecretManager import SecretManager


class SecretAccessor(SecretManager):
    def get_sengrid_value(self, origin: str, key: str):
        secrets = self._get_level(key="SENDGRID_TEMPLATES")
        if origin in secrets:
            if key in secrets[origin]:
                return secrets[origin][key]

        if "default" in secrets:
            if key in secrets["default"]:
                return secrets["default"][key]

        return None

    def get_sns_values(self, origin: str, key: str):
        secrets = self._get_level(key="AWS_SNS_VALUES")
        if origin in secrets:
            if key in secrets[origin]:
                return secrets[origin][key]

        if "default" in secrets:
            if key in secrets["default"]:
                return secrets["default"][key]

        return None

    def get_external_key(self, key: str):
        secrets = self._get_level(key="EXTERNAL_API_KEYS")
        if key in secrets:
            return secrets[key]

        if "default" in secrets:
            return secrets["default"]

        return None

import logging

import boto3
import json
from botocore.exceptions import ClientError


class SecretManager:
    def __init__(self, secret_id="cb-service-users", region_name="us-east-1"):
        self.__client = boto3.client(
            "secretsmanager",
            region_name=region_name,
        )
        self.__secret_id = secret_id
        self.__secrets_info = self.__get_secrets()

    def __get_secrets(self) -> dict:

        try:
            credentials = json.loads(
                self.__client.get_secret_value(SecretId=self.__secret_id)[
                    "SecretString"
                ]
            )
            return credentials
        except ClientError as e:
            logging.error(
                e,
                {
                    "index_meta": True,
                    "origin": "SecretManager",
                    "error": e.response["Error"]["Code"],
                },
            )
            if e.response["Error"]["Code"] == "DecryptionFailureException":
                # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response["Error"]["Code"] == "InternalServiceErrorException":
                # An error occurred on the server side.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response["Error"]["Code"] == "InvalidParameterException":
                # You provided an invalid value for a parameter.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response["Error"]["Code"] == "InvalidRequestException":
                # You provided a parameter value that is not valid for the current state of the resource.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response["Error"]["Code"] == "ResourceNotFoundException":
                # We can't find the resource that you asked for.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e

    def _get_level(self, key: str):
        if key in self.__secrets_info:
            return self.__secrets_info[key]
        return None

import uuid
import logging

logger = logging.getLogger(__name__)


class CbValidators:
    @classmethod
    def valid_uuid(cls, value=""):
        if type(value) == str:
            try:
                uuid.UUID(value)
                return True
            except ValueError:
                return False
        return False

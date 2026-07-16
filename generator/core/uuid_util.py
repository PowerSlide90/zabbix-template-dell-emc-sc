from uuid import uuid5

from config import UUID_NAMESPACE


def make_uuid(object_type: str, key: str):

    return str(uuid5(UUID_NAMESPACE, f"{object_type}:{key}"))
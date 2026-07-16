import uuid

from config import UUID_NAMESPACE


def make_uuid(object_type: str, key: str) -> str:
    """
    Генерирует детерминированный UUIDv5.

    Один и тот же object_type + key
    всегда даст одинаковый UUID.
    """

    return str(
        uuid.uuid5(
            UUID_NAMESPACE,
            f"{object_type}:{key}"
        )
    )
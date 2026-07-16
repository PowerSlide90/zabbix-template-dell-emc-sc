import uuid

def make_uuid(object_type: str, key: str) -> str:
    return str(uuid.uuid5(UUID_NAMESPACE, f"{object_type}:{key}"))
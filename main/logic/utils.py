import hashlib


def get_hash_sha256(file: bytes) -> str:
    """Return SHA256 hash of file"""
    hash_id = hashlib.sha256()
    hash_id.update(file)
    return hash_id.hexdigest()


def get_hash_sha1(file: bytes) -> str:
    """Return SHA1 hash of file"""
    hash_id = hashlib.sha1()
    hash_id.update(file)
    return hash_id.hexdigest()

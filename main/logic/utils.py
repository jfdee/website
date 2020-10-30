import hashlib


def get_hash_sha256(file: bytes):
    """Return SHA256 hash of file"""
    hashId = hashlib.sha256()
    hashId.update(file)
    return hashId.hexdigest()


def get_hash_sha1(file: bytes):
    """Return SHA1 hash of file"""
    hashId = hashlib.sha1()
    hashId.update(file)
    return hashId.hexdigest()

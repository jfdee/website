import hashlib


def get_hash_sha256(file):
    """Return SHA256 hash of file"""
    file = file.encode('utf-8')
    return hashlib.sha256(file).hexdigest()


def get_hash_sha1(file):
    """Return SHA1 hash of file"""
    file = file.encode('utf-8')
    return hashlib.sha1(file).hexdigest()
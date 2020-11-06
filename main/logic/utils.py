import hashlib
import re


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


def get_count_leaf_binary_tree(string, count=0) -> int:
    """Return count leaf of binary tree"""
    # Если есть два дочерних листка (Например, [3,3])
    match = re.search(r'\[\d+\,\d+\]', string)
    if match:
        string = string.replace(match[0], '')
        count = count + 2
        return get_count_leaf_binary_tree(string, count)
    else:
        # Если дочерний лист только один (Например, [9])
        match = re.search(r'\[\d+\]', string)
        if match:
            string = string.replace(match[0], '')
            count = count + 1
            return get_count_leaf_binary_tree(string, count)
        else:
            return count

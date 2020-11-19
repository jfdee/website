import hashlib
import re
import json
from lxml import etree
from typing import Optional, Union
from django.core.files.base import ContentFile, BytesIO
from PIL import Image


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


def get_count_leaf_binary_tree(string: str, count: int = 0) -> int:
    """Method for get count leaf of binary tree"""
    KEY_INDEX_FOR_MATCH: int = 0
    AMOUNT_LEAF_IF_TWO_ELEMENTS: int = 2
    AMOUNT_LEAF_IF_ONE_ELEMENTS: int = 1
    # Если есть два дочерних листка (Например, [3,3])
    match: Optional[str] = re.search(r'\[\d+\,\d+\]', string)
    if match is not None:
        string = string.replace(match[KEY_INDEX_FOR_MATCH], '')
        count = count + AMOUNT_LEAF_IF_TWO_ELEMENTS
        return get_count_leaf_binary_tree(string, count)
    else:
        # Если дочерний лист только один (Например, [9])
        match: Optional[str] = re.search(r'\[\d+\]', string)
        if match is not None:
            string = string.replace(match[KEY_INDEX_FOR_MATCH], '')
            count = count + AMOUNT_LEAF_IF_ONE_ELEMENTS
            return get_count_leaf_binary_tree(string, count)
    return count


def xml_to_json(xml: Union[str, BytesIO, ContentFile]) -> str:
    """Method for convert XML to JSON"""
    tree = etree.parse(xml)
    xslt_root = etree.parse("xml2json.xsl")
    transform = etree.XSLT(xslt_root)
    result = transform(tree)
    json_load = json.loads(str(result))
    json_dump = json.dumps(json_load, indent=2)

    return json_dump


def crop_image(path: str) -> Image:
    """Return new cropped image"""
    COUNT_COORDS = 4
    img = Image.open(path)
    coords = map(int, input('Coords:').split()[:COUNT_COORDS])
    cropped = img.crop(coords)
    return cropped


def united_images(*paths) -> Image:
    """Return new united image"""
    COUNT_IMAGES = len(paths)
    img = Image.new('RGB', (500 * COUNT_IMAGES, 500))
    k = 0
    for path in paths:
        imageTemp = Image.open(path)
        img.paste(imageTemp, (500 * k, 0))
        k = k + 1
    return img

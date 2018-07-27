import pytest

import pyhash


def test_city_32(hash_tester):
    hash_tester(hasher_type=pyhash.city_32,
                bytes_hash=1633095781,
                seed_hash=3687200064,
                unicode_hash=3574089775)


def test_city_64(hash_tester):
    hash_tester(hasher_type=pyhash.city_64,
                bytes_hash=17703940110308125106,
                seed_hash=8806864191580960558,
                unicode_hash=7557950076747784205)


def test_city_128(hash_tester):
    hash_tester(hasher_type=pyhash.city_128,
                bytes_hash=195179989828428219998331619914059544201,
                seed_hash=206755929755292977387372217469167977636,
                unicode_hash=211596129097514838244042408160146499227)


def test_city_crc128(hash_tester):
    hash_tester(hasher_type=pyhash.city_crc_128,
                bytes_hash=195179989828428219998331619914059544201,
                seed_hash=206755929755292977387372217469167977636,
                unicode_hash=211596129097514838244042408160146499227)


def test_city_crc256(hash_tester):
    hash_tester(hasher_type=pyhash.city_crc_256,
                bytes_hash=43374127706338803100025155483422426900760284308948611519881759972455588549698,
                seed_hash=43374127706338803100025155483422426900760284308948611519881759972455588549698,
                unicode_hash=106103693879923228777324437129892107726572355760220840777228701216663718411687)

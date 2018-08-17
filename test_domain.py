import pytest
from domain import Domain


@pytest.fixture()
def sample_domain():
    my_domain = Domain(43690, 'Teagan')
    return my_domain


@pytest.fixture(params=[43690, 48059, 52428])
def ids(request):
    return request.param


def test_int_to_hex(sample_domain):
    """Tests if method returns valid hex. Also tests accuracy of example IDs."""
    assert int(sample_domain.int_to_hex(sample_domain.id), 16)
    assert sample_domain.int_to_hex(43690) == 'AAAA'
    assert sample_domain.int_to_hex(48059) == 'BBBB'
    assert sample_domain.int_to_hex(52428) == 'CCCC'


def test_int_to_hex_leading_zeroes(sample_domain):
    """Tests if method returns leading zeroes for 1, 2, and 3 digit decimal IDs"""
    assert sample_domain.int_to_hex(0) == '0000'
    assert sample_domain.int_to_hex() == '0000'
    assert sample_domain.int_to_hex(1) == '0001'
    assert sample_domain.int_to_hex(16) == '0010'
    assert sample_domain.int_to_hex(256) == '0100'


def test_generate_uuid4(sample_domain):
    """Test length and validity of generated uuid version 4."""
    assert len(sample_domain.generate_uuid4()) == 8
    assert int(sample_domain.generate_uuid4(), 16)


def test_format_mac_address(sample_domain):
    """Tests formatted addresses are correctly delimited by a colon."""
    assert sample_domain.format_mac_address('AAAA', 'BBCCDDEE') == 'AA:AA:BB:CC:DD:EE'


def test_domain_functional(ids):
    """
    Tests instantiation of three test domains:
        -checks number of mac addresses generated per instance
        -checks for uniqueness
    """
    my_domain = Domain(ids, 'Functional Domain Test')

    my_domain.generate_mac_address()
    assert len(my_domain.mac_addresses) == 10
    # use set function to determine uniqueness
    assert len(set(my_domain.mac_addresses)) == 10


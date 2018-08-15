import pytest
from domain import Domain


@pytest.fixture()
def sample_domain():
    my_domain = Domain(4096, 'Teagan')
    return my_domain


def test_int_to_hex(sample_domain):
    """Tests if method returns valid hex."""
    assert int(sample_domain.int_to_hex(sample_domain.id), 16)


def test_int_to_hex_leading_zeroes():
    pass


def test_build_mac_address():
    #verify length
    #verify formatting
    pass
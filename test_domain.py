import pytest, uuid
from domain import Domain


@pytest.fixture()
def sample_domain():
    my_domain = Domain(4096, 'Teagan')
    return my_domain


def test_int_to_hex(sample_domain):
    """Tests if method returns valid hex. Also tests accuracy of example IDs."""
    assert int(sample_domain.int_to_hex(sample_domain.id), 16)
    assert sample_domain.int_to_hex(43690) == 'AAAA'
    assert sample_domain.int_to_hex(48059) == 'BBBB'
    assert sample_domain.int_to_hex(52428) == 'CCCC'

def test_int_to_hex_leading_zeroes(sample_domain):
    """Tests if method returns leading zeroes for 1, 2, and 3 digit decimal IDs"""
    assert sample_domain.int_to_hex(0) == '0000'
    assert sample_domain.int_to_hex(1) == '0001'
    assert sample_domain.int_to_hex(16) == '0010'
    assert sample_domain.int_to_hex(256) == '0100'


def test_format_mac_address():
    #verify length
    #verify formatting
    pass


#TODO:  look up text formatting in AtBS
#TODO: consider adding collision resolution
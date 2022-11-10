'''Test if standards contraints for Item values are written properly'''
import pytest
from utils.standards import Standard

@pytest.fixture(scope='module', params=[('milano', 'city'), 
                                        ('district', 'niguarda'),
                                        ('address', 'Via Privata Paolo Rotta') ])

def test_intrinsic_properties(prop: str, field: str):
    standard = Standard(field)
    assert standard.validate(prop), f"{prop} does not respect standard for {field}"
                                    






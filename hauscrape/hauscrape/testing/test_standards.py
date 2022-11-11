'''Test if standards contraints for Item values are written properly'''
import pytest
from utils.standards import Standard

@pytest.fixture(scope='module', params=[('city', 'milano'), 
                                        ('district', 'niguarda'),
                                        ('address', 'via paolo rotta 18'),
                                        ('address', 'via privata paolo rotta 18')
                                        ])
def props(request):
    ''''''
    yield request.param

def test_intrinsic_properties(props):
    '''Test intrinsic properties respect standards'''
    field = props[0]
    value = props[1]
    standard = Standard(field)
    assert standard.validate(value),  '"%s" not "%s"-compliant' % (value, field)


                                    






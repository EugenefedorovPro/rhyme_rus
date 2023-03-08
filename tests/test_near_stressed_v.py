import pytest
from rhyme_rus.seeds.ipa_dicts import IpaDicts
from rhyme_rus.utils.near_stressed_v import get_near_stressed_v

def stress2near(stressed_v):
    return IpaDicts().near_stressed_v_int[stressed_v]

@pytest.mark.parametrize("stressed_v, expected_near", [
    (1, stress2near(1)),
    (76, stress2near(76))
]
                         )
def test_get_near_stressed_v(stressed_v, expected_near):
    actual_near = get_near_stressed_v(stressed_v)
    assert actual_near == expected_near
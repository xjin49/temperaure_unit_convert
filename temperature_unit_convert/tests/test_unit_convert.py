import pytest

from temperature_unit_convert.temperature_unit_convert import k_to_c, c_to_k, temp_from_F, temp_to_F

def test_unit_convert():
    # some known results
    # Verify that the "round trip" conversion from and back to C.
    
    for orig in [10, 20, 30]:
        new = k_to_c(c_to_k(orig))
        assert new == orig
    # Verify that the "round trip" conversion from and back to F.
        
    for orig_F in [100, 90, 95]:
        new = temp_from_F(temp_to_F(orig_F))
        assert new == orig_F    
    
    # now check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        k_to_c(1, 2, 3)

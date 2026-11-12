def test_expected_lab_defects_are_documented():
    # This guards the teaching contract: learners must have data to clean.
    from retailflow.data_generation.generator import CATEGORIES
    assert "electronics " in CATEGORIES

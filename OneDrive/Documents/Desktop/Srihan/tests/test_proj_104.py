"""Assertions Suite for RFC 5322 Email Validation Service"""

def test_validation_suite():
    assert validate_email("user@example.com") is True
    assert validate_email("john.doe@company.org") is True
    
    try:
        validate_email("user..name@example.com")
        assert False, "Should raise ValueError on consecutive dots"
    except ValueError:
        pass

    try:
        validate_email("invalid-address")
        assert False, "Should raise ValueError on bad domain"
    except ValueError:
        pass

test_validation_suite()

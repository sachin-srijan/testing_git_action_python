import script

def test_get_random_password():
    output = script.get_random_password()
    assert len(output) >= 7
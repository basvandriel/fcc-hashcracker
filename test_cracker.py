from cracker import crack_sha1_hash

def test_hash_1():
    actual = crack_sha1_hash("18c28604dd31094a8d69dae60f1bcd347f1afc5a")
    expected = "superman"

    assert actual == expected

def test_hash_2():
    actual = crack_sha1_hash("5d70c3d101efd9cc0a69f4df2ddf33b21e641f6a")
    expected = "q1w2e3r4t5"

    assert actual == expected

def test_hash_3():
    actual = crack_sha1_hash("b80abc2feeb1e37c66477b0824ac046f9e2e84a0")
    expected = "bubbles1"

    assert actual == expected

def test_hash_4():
    actual = crack_sha1_hash("80540a46a2c1a0eae58d9868f01c32bdcec9a010")
    expected = "01071988"

    assert actual == expected
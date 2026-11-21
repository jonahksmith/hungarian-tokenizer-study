from hutok.metrics import fertility

def test_fertility_simple():
    fake_tokenize = lambda text: ["a", "b", "c", "d"]
    assert fertility("one, two", fake_tokenize) == 2.0
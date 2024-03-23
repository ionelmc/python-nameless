from .. import main


def test_main():
    assert main([b"a", b"bc", b"abc"]) == b"abc"

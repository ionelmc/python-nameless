from nameless import main


def test_main():
    assert main(["a", "bc", "abc"]) == "abc"

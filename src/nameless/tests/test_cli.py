import subprocess


def test_main():
    assert subprocess.check_output(["nameless", "foo", "foobar"], text=True) == "foobar\n"

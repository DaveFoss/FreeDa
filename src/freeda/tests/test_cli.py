import subprocess


def test_main():
    assert subprocess.check_output(["freeda", "foo", "foobar"], text=True) == "foobar\n"

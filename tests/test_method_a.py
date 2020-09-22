import pytest


@pytest.fixture
def document():
    from package.someclass import SomeClass
    return SomeClass()


def test_method_a_one(document):
    result = document.method_a("a")[0]
    assert result.string == "a"


def test_method_a_two(document):
    result = document.method_a("b")[0]
    assert result.string == "b"

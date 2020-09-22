import pytest


@pytest.fixture
def someclass():
    from package.someclass import SomeClass
    return SomeClass()


def test_method_a_one(someclass):
    result = someclass.method_a("a")[0]
    assert result.string == "a"


def test_method_a_two(someclass):
    result = someclass.method_a("b")[0]
    assert result.string == "b"
